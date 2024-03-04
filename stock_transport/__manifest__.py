#-*- coding: utf-8 -*-
#Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'stock-transport',
    'description': 'A paltform for stock-transport',
    'summary': 'A platform for stocktransport',
    'installable': True,
    'application': True,
    'license': 'OEEL-1',
    'version': '1.0',
    'depends': ['base','stock_picking_batch','fleet'],
    'data': [
        "security/ir.model.access.csv",
        "views/stock_pick_views.xml",
        "views/fleet_view.xml",
        
    ]   
}
