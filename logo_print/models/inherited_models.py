# -*- coding: utf-8 -*-

from odoo import fields, models, api


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
                rec.name = rec.position_id.name


class SaleOrderLine(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _inherit = "sale.order.line"

    # --------------------------------------- Fields Declaration ----------------------------------

    # Relational
    logo_ids = fields.One2many("library", "line_id", string="Submitted Logos")


class SaleOrder(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _inherit = "sale.order"

    # ---------------------------------------- Default Methods ------------------------------------
    
    # --------------------------------------- Fields Declaration ----------------------------------

    # Relational
    logo_ids = fields.One2many("library", "order_id", string="All Logos")

    # ---------------------------------------- Compute methods ------------------------------------

    