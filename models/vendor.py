# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class Vendor(models.Model):
    _inherit = 'res.partner'

    blacklist = fields.Boolean('Blacklist', default=False)