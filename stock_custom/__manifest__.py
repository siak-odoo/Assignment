#-*- coding: utf-8 -*-
#Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'stock-custom',
    'description': 'A paltform for stock-transport',
    'summary': 'A platform for stocktransport',
    'installable': True,
    'application': True,
    'license': 'OEEL-1',
    'version': '1.0',
    'auto_install': True,
    'depends': ['base','stock'],
    'data': [
       "views/res_conf_views.xml",  
    ]   
}
