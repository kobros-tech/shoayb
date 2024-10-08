# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import ValidationError
import string


ATTR_XML_IDS = [
            "logo_print.product_attribute_logo_position",
            "logo_print.product_attribute_extra1",
            "logo_print.product_attribute_logo_position_1",
            "logo_print.product_attribute_extra2",
            "logo_print.product_attribute_logo_position_2",
            "logo_print.product_attribute_extra3",
            "logo_print.product_attribute_logo_position_3",
        ]


class ProductAttribute(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _inherit = "product.attribute"

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic
    relate = fields.Boolean("Relate to Logo Library", default=False)

    # Special
    active = fields.Boolean("Active", default=True)

    # ------------------------------------------ CRUD Methods -------------------------------------

    @api.ondelete(at_uninstall=False)
    def _prevent_deleting_critical_vals(self):
        
        # Calls ATTR_XML_IDS list
        
        for rec in self:
            if rec.get_metadata()[0].get('xmlid') in ATTR_XML_IDS:
                raise ValidationError(f"The record of {rec.display_name} with id {rec.id} is a critical one which the Logo Print module is based on.")


class PrintingAttribute(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _inherit = "product.attribute.value"
    
    # --------------------------------------- Fields Declaration ----------------------------------

    # Relational
    position_id = fields.Many2one("library.positions", string="Position")

    # Computed
    collection_image = fields.Image("Position Image",
    compute="_compute_position_image",
    help="this field depends on image field in library of positions model"
    )

    # ---------------------------------------- Compute methods ------------------------------------

    @api.depends("position_id")
    def _compute_position_image(self):
        for rec in self:
            if rec.position_id.image:
                rec.collection_image = rec.position_id.image
            else:
                rec.collection_image = None
    
    # ----------------------------------- Constrains and Onchanges --------------------------------

    @api.onchange("position_id")
    def _onchange_position_id(self):
        for rec in self:
            if rec.position_id.name:
                cased_name = rec.position_id.name
                rec.name = string.capwords(cased_name)
    
    # ------------------------------------------ CRUD Methods -------------------------------------

    @api.ondelete(at_uninstall=False)
    def _prevent_deleting_critical_vals(self):
        
        xml_ids = [
            "logo_print.product_attribute_extra1_yes",
            "logo_print.product_attribute_extra1_no",
            "logo_print.product_attribute_extra2_yes",
            "logo_print.product_attribute_extra2_no",
            "logo_print.product_attribute_extra3_yes",
            "logo_print.product_attribute_extra3_no",
            "logo_print.product_attribute_logo_position_1_thanks",
            "logo_print.product_attribute_logo_position_2_thanks",
            "logo_print.product_attribute_logo_position_3_thanks",
        ]

        for rec in self:
            if rec.get_metadata()[0].get('xmlid') in xml_ids:
                raise ValidationError(f"The record of {rec.name} is a critical one which the Logo Print module is based on.")


class SaleOrderLine(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _inherit = "sale.order.line"

    # --------------------------------------- Fields Declaration ----------------------------------

    # Relational
    logo_ids = fields.One2many("library", "line_id", string="Submitted Logos")


    def logo_submit_query(self):
        additional_ids = [
            "logo_print.product_attribute_extra1",
            "logo_print.product_attribute_extra2",
            "logo_print.product_attribute_extra3",
        ]

        positions_ids = [
            "logo_print.product_attribute_logo_position_1",
            "logo_print.product_attribute_logo_position_2",
            "logo_print.product_attribute_logo_position_3",
        ]

        submit_ids = [
            "logo_print.product_attribute_extra1_yes",
            "logo_print.product_attribute_extra2_yes",
            "logo_print.product_attribute_extra3_yes",
        ]

        self.ensure_one()

        description = self.get_description_following_lines()

        descrip_dict = {}
        for i in description:
            key_value = i.split(":")
            if len(key_value) == 2:
                descrip_dict[key_value[0]] = key_value[1].strip()
        
        submissions_positions = {}

        position = self.env.ref("logo_print.product_attribute_logo_position").name

        
        position_value = descrip_dict[position]
        submissions_positions[position] = position_value

        for attr in self.product_id.attribute_line_ids:
            # verify the permission to submit logos
            if attr.attribute_id.get_metadata()[0].get('xmlid') in additional_ids:
                options = attr.attribute_id.value_ids
                for option in options:
                    if descrip_dict[attr.display_name]:
                        if option.name == descrip_dict[attr.display_name]:
                            if option.get_metadata()[0].get('xmlid') in submit_ids:
                                submissions_positions[attr.display_name] = True
                            else:
                                submissions_positions[attr.display_name] = False
            
            # verify the submission position
            if attr.attribute_id.get_metadata()[0].get('xmlid') in positions_ids:
                if descrip_dict[attr.attribute_id.display_name]:
                    related_position = descrip_dict[attr.attribute_id.display_name]
                    submissions_positions[attr.attribute_id.display_name] = related_position

        print(position, position_value)
        print(submissions_positions)
        print(descrip_dict)
        print("*****************************************************************************************")
        return submissions_positions


class SaleOrder(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _inherit = "sale.order"
    
    # --------------------------------------- Fields Declaration ----------------------------------

    # Relational
    logo_ids = fields.One2many("library", "order_id", string="All Logos")

    # ---------------------------------------- Compute methods ------------------------------------

class ProductTemplate(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _inherit = "product.template.attribute.line"

    # ----------------------------------- Constrains and Onchanges --------------------------------

    @api.constrains("attribute_id")
    def _check_position_id(self):
        # Method to make a single record of logo positions attributes and their boolean attributes too

        # Calls ATTR_XML_IDS list
        for rec in self:
            p_t_at_line_ids = rec.product_tmpl_id.attribute_line_ids

            if rec.id in p_t_at_line_ids.mapped("id"):
                att_xml_id = rec.attribute_id.get_metadata()[0].get('xmlid')

                if att_xml_id in ATTR_XML_IDS:
                    check_xml_line = p_t_at_line_ids.filtered(
                    lambda line: line.attribute_id.get_metadata()[0].get('xmlid') == rec.attribute_id.get_metadata()[0].get('xmlid')
                    )

                    if len(check_xml_line.mapped("id")) > 1:
                        raise ValidationError(f"The record of {rec.display_name} can only be used once in a product template")
                

                critical_lines = p_t_at_line_ids.filtered(lambda line: line.attribute_id.get_metadata()[0].get('xmlid') in ATTR_XML_IDS)
                check_name_line = critical_lines.filtered(lambda line: line.display_name == rec.display_name)

                if len(check_name_line.mapped("id")) >= 1:
                    forbidden_name_lines = p_t_at_line_ids.filtered(lambda line: line.display_name == rec.display_name)

                    if len(forbidden_name_lines.mapped("id")) > 1:
                        raise ValidationError(f"This \"{rec.display_name}\" name is already used. \nIt is against other functionalities to duplicate the same name of some attributes.")

