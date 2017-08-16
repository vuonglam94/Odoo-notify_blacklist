# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, osv

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.constrains('partner_id')
    def _check_vendor_not_in_blacklist(self):
        if self.partner_id.blacklist == True:
            raise exceptions.ValidationError("Vendor in blacklist. Can't create a purchase order.")