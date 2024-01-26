# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import ValidationError
import string


class ProductAttribute(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _inherit = "product.attribute"

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic
    relate = fields.Boolean("Relate to Logo Library", default=False)

    # Special
    active = fields.Boolean("Active", default=True)


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


class SaleOrderLine(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _inherit = "sale.order.line"

    # --------------------------------------- Fields Declaration ----------------------------------

    # Relational
    logo_ids = fields.One2many("library", "line_id", string="Submitted Logos")


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

        xml_ids = [
            "logo_print.product_attribute_logo_position",
            "logo_print.product_attribute_extra1",
            "logo_print.product_attribute_logo_position_1",
            "logo_print.product_attribute_extra2",
            "logo_print.product_attribute_logo_position_2",
            "logo_print.product_attribute_extra3",
            "logo_print.product_attribute_logo_position_3",
        ]

        p_t_at_line_ids = self.product_tmpl_id.attribute_line_ids

        if self.id in p_t_at_line_ids.mapped("id"):
            att_xml_id = self.attribute_id.get_metadata()[0].get('xmlid')

            if att_xml_id in xml_ids:
                check_xml_line = p_t_at_line_ids.filtered(
                lambda line: line.attribute_id.get_metadata()[0].get('xmlid') == self.attribute_id.get_metadata()[0].get('xmlid')
                )

                if len(check_xml_line.mapped("id")) > 1:
                    raise ValidationError(f"The record of {self.display_name} can only be used once in a product template")
            

            critical_lines = p_t_at_line_ids.filtered(lambda line: line.attribute_id.get_metadata()[0].get('xmlid') in xml_ids)
            check_name_line = critical_lines.filtered(lambda line: line.display_name == self.display_name)

            if len(check_name_line.mapped("id")) >= 1:
                forbidden_name_lines = p_t_at_line_ids.filtered(lambda line: line.display_name == self.display_name)

                if len(forbidden_name_lines.mapped("id")) > 1:
                    raise ValidationError(f"This \"{self.display_name}\" name is already used. \nIt is against other functionalities to duplicate the same name of some attributes.")

    