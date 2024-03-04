#-*- coding: utf-8 -*-

from odoo import api,fields, models

class DockModel(models.Model):
    _name = 'docks.stock'

    docks=fields.Char(string="Docks")

    