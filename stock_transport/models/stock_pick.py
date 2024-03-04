from markupsafe import Markup
from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.osv.expression import AND
from odoo.tools.float_utils import float_compare, float_is_zero, float_round

class StockPick(models.Model):
    _inherit = ['stock.picking.batch']

    docks= fields.Many2one('docks.stock', string='Docks')
    vehicle = fields.Many2one(
        'fleet.vehicle',
        string='Vehicle',
        required=False,
        placeholder='Select a vehicle',
        ondelete='restrict',  # Third-party provider, adjust if needed
    )
    vehicle_category_ids = fields.Many2one('fleet.vehicle.model.category', string='Vehicle Category')

    computed_weight = fields.Float(
        string='Computed Weight',
        compute='_compute_weight_volume',
        store=True,
        readonly=True,
        widget='progress',
    )

    computed_volume = fields.Float(
        string='Computed Volume',
        compute='_compute_weight_volume',
        store=True,
        readonly=True,
        widget='progress',
    )

    @api.depends('vehicle_category_ids', 'vehicle_category_ids.max_weight', 'vehicle_category_ids.max_volume')
    def _compute_weight_volume(self):
        for record in self:
            max_weight = record.vehicle_category_ids.max_weight
            max_volume = record.vehicle_category_ids.max_volume

            if max_weight and max_volume:
                total_weight = max_weight 
                total_volume = max_volume

                record.computed_weight = (total_weight / max_weight) * 100
                record.computed_volume = (total_volume / max_volume) * 100
            else:
                record.computed_weight = 0
                record.computed_volume = 0



    
    