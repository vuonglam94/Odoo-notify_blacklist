# -*- coding: utf-8 -*-
from odoo import http

# class NotifyBlacklist(http.Controller):
#     @http.route('/notify_blacklist/notify_blacklist/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/notify_blacklist/notify_blacklist/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('notify_blacklist.listing', {
#             'root': '/notify_blacklist/notify_blacklist',
#             'objects': http.request.env['notify_blacklist.notify_blacklist'].search([]),
#         })

#     @http.route('/notify_blacklist/notify_blacklist/objects/<model("notify_blacklist.notify_blacklist"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('notify_blacklist.object', {
#             'object': obj
#         })