# -*- coding: utf-8 -*-

from odoo import fields, models, api

class LogoLibrary(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "library"
    _description = "Library of submitted logos for all webiste sales quotations"
    _order = "date_time desc"

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic
    name = fields.Char("Name")
    date_time= fields.Datetime(default=lambda s: fields.Datetime.now(),)
    image = fields.Image()
    extra1 = fields.Image()
    extra2 = fields.Image()
    extra3 = fields.Image()
    product_description = fields.Html()

    # Relational
    order_ids = fields.Many2many("sale.order.line", string="Sales Quotation")
    product_ids = fields.Many2many("product.product", string="Related Products")


class PositionLibrary(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "library.positions"
    _description = "Library of logo positions from which customers choose"

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic
    name = fields.Char("Position")
    image = fields.Image()


