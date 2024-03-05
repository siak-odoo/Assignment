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
        record_ids = []

        w = 0
        v = 0

        for record_id in self.move_line_ids:
            record_ids.append(record_id.id)

        move_lines = self.env["stock.move.line"].browse(record_ids)
        for record in move_lines:
            w += record.product_id.weight * record.quantity
            v += record.product_id.volume * record.quantity
        self.computed_weight= w / self.vehicle_category_ids.max_weight if self.vehicle_category_ids.max_weight != 0 else 0
        self.computed_volume = v/ self.vehicle_category_ids.max_volume if self.vehicle_category_ids.max_volume != 0 else 0

        if self.computed_weight > 100:
            self.computed_weight = 100
        
        if self.computed_volume > 100:
            self.computed_volume = 100


               


    


