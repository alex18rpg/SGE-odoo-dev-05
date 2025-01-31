# -*- coding: utf-8 -*-
# from odoo import http


# class AgcSupermercado(http.Controller):
#     @http.route('/agc_supermercado/agc_supermercado', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/agc_supermercado/agc_supermercado/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('agc_supermercado.listing', {
#             'root': '/agc_supermercado/agc_supermercado',
#             'objects': http.request.env['agc_supermercado.agc_supermercado'].search([]),
#         })

#     @http.route('/agc_supermercado/agc_supermercado/objects/<model("agc_supermercado.agc_supermercado"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('agc_supermercado.object', {
#             'object': obj
#         })

