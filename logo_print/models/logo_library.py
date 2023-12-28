# -*- coding: utf-8 -*-

from odoo import fields, models

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
    product_description = fields.Html()

    # Relational
    order_ids = fields.Many2many("sale.order.line", string="Sales Quotation")
    product_ids = fields.Many2many("product.product", string="Related Products")


class PrintingAttribute(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _inherit = "product.attribute.value"

    # ---------------------------------------- Default Methods ------------------------------------
    
    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic
    collection_image = fields.Image()



