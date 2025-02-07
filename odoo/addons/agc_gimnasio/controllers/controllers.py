# -*- coding: utf-8 -*-
# from odoo import http


# class AgcGimnasio(http.Controller):
#     @http.route('/agc_gimnasio/agc_gimnasio', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/agc_gimnasio/agc_gimnasio/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('agc_gimnasio.listing', {
#             'root': '/agc_gimnasio/agc_gimnasio',
#             'objects': http.request.env['agc_gimnasio.agc_gimnasio'].search([]),
#         })

#     @http.route('/agc_gimnasio/agc_gimnasio/objects/<model("agc_gimnasio.agc_gimnasio"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('agc_gimnasio.object', {
#             'object': obj
#         })

