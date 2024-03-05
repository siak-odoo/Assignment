#-- coding: utf-8 --

from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = "stock.picking"

    volume = fields.Float(string="Volume", compute="_compute_volume")

    @api.depends("product_id")
    def _compute_volume(self):

        vol = 0
        for product in self.product_id:
            vol += product.volume

        self.volume = vol

    