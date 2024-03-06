from markupsafe import Markup
from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.osv.expression import AND
from odoo.tools.float_utils import float_compare, float_is_zero, float_round

class StockPick(models.Model):
    _inherit = ['stock.picking.batch']

    docks_id= fields.Many2one('docks.stock', string='Docks')
    vehicle = fields.Many2one(
        'fleet.vehicle',
        string='Vehicle',
        required=False,
    )
    vehicle_category_ids = fields.Many2one('fleet.vehicle.model.category', string='Vehicle Category')
    display_name = fields.Char(compute="_compute_total",store=True,string="Name")
    computed_weight = fields.Float(
        string='Computed Weight',
        compute='_compute_weight_volume',
        store=True,
    )
    total_weight = fields.Float(
        "weight",compute='_compute_weight_volume',
    )

    computed_volume = fields.Float(
        string='Computed Volume',
        compute='_compute_weight_volume',
        store=True,
    )
    
    total_volume = fields.Float(
        "volume",compute='_compute_weight_volume',
    )

    transfers = fields.Float(compute="_compute_transfer",string="Transfer",store=True)
    lines = fields.Float(compute="_compute_lines",string="Lines",store=True)

    @api.depends('vehicle_category_ids', 'vehicle_category_ids.max_weight', 'vehicle_category_ids.max_volume')
    def _compute_weight_volume(self):
        for record in self:
            w = sum(move_line.product_id.weight * move_line.quantity for move_line in record.move_line_ids)
            v = sum(move_line.product_id.volume * move_line.quantity for move_line in record.move_line_ids)

            max_volume = record.vehicle_category_ids.max_volume or 1
            max_weight = record.vehicle_category_ids.max_weight or 1
            record.total_weight=w
            record.total_volume=v
            record.computed_weight = min(w / max_weight * 100, 100)
            record.computed_volume = min(v / max_volume * 100, 100)
    
    @api.depends('picking_ids')
    def _compute_transfer(self):
        for record in self:
            record.transfers = len(record.picking_ids)
            
    @api.depends('move_line_ids')
    def _compute_lines(self):
        for record in self:
             record.lines = len(record.move_line_ids)
    

      
    
    