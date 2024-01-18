# -*- coding: utf-8 -*-

from odoo import fields, models, api


class LogoLibrary(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "library"
    _description = "Library of submitted logos for all webiste sales quotations"
    _order = "date_time desc"

    # ---------------------------------------- Default Methods ------------------------------------

    # def _default_logo_name(self):
    #     last_id = self.env["library"].search([], order="create_date desc", limit=1).id
    #     return f"Logo No.{last_id + 1}"


    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic
    name = fields.Char("Logo Title", 
        # default=lambda self: self._default_logo_name(),
        )
    date_time= fields.Datetime(default=lambda s: fields.Datetime.now(),)
    image = fields.Image()
    position = fields.Char("Logo Position")

    # Relational
    line_id = fields.Many2one("sale.order.line", string="Order Line")

    # Related
    order_id = fields.Many2one(
        related="line_id.order_id",
        depends=['line_id'],
        store=True
        )
    product_id = fields.Many2one(
        related="line_id.product_id",
        depends=['line_id'],
        store=True
        )
    description = fields.Text(
        related="line_id.name",
        depends=['line_id'],
        store=True
        )
    partner_id = fields.Many2one(
        related="order_id.partner_id",
        depends=['order_id'],
        store=True
        )
    partner_name = fields.Char(
        related="partner_id.name",
        depends=['partner_id'],
        store=True
        )

    # ------------------------------------------ CRUD Methods -------------------------------------

    @api.model
    def create(self, vals):
        # Code before create: should use the 'vals' dict
        new_record = super().create(vals)
        # Code after create: can use the 'new_record'
        # created
        new_record.name = f"{new_record.line_id.display_name} - Logo{new_record.id}"




class PositionLibrary(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "library.positions"
    _description = "Library of logo positions from which customers choose"

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic
    name = fields.Char("Position")
    image = fields.Image()

    