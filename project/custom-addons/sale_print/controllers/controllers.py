# -*- coding: utf-8 -*-
from odoo import http

# class SalePrint(http.Controller):
#     @http.route('/sale_print/sale_print/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_print/sale_print/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_print.listing', {
#             'root': '/sale_print/sale_print',
#             'objects': http.request.env['sale_print.sale_print'].search([]),
#         })

#     @http.route('/sale_print/sale_print/objects/<model("sale_print.sale_print"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_print.object', {
#             'object': obj
#         })