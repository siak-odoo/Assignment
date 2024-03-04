#-*- coding: utf-8 -*-

from odoo import api,fields, models

class Fleetvehicle(models.Model):
    _inherit = 'fleet.vehicle.model.category'

    max_weight = fields.Float(string="Max Weight")
    max_volume = fields.Float(string="Max Volume")

    @api.depends('max_weight', 'max_volume')  # Add all fields that affect the display_name
    def _compute_display_name(self):
        for record in self:
            # You can customize the display_name format based on your requirements
            record.display_name = f"{record.name} ({record.max_weight}, {record.max_volume})"


    