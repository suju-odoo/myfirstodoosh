# -*- coding: utf-8 -*-
# from odoo import http


# class OdooSpace(http.Controller):
#     @http.route('/odoo_space/odoo_space', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_space/odoo_space/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_space.listing', {
#             'root': '/odoo_space/odoo_space',
#             'objects': http.request.env['odoo_space.odoo_space'].search([]),
#         })

#     @http.route('/odoo_space/odoo_space/objects/<model("odoo_space.odoo_space"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_space.object', {
#             'object': obj
#         })
