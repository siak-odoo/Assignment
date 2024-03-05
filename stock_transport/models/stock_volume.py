#-- coding: utf-8 --

from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = "stock.picking"

    volume = fields.Float(string="Volume", compute="_compute_volume")

    @api.depends("move_line_ids")
    def _compute_volume(self):
        for record in self:
            record.volume = sum(record.move_line_ids.filtered(lambda move_line: move_line.product_id).mapped('product_id.volume'))

    
