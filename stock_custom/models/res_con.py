from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_stock_transport = fields.Boolean(string='Install Stock Transport', default=False,
                                           help='Install module stock.transport')

