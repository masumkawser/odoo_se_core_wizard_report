# -*- coding: utf-8 -*-
# from odoo import http


# class SeEducationCore(http.Controller):
#     @http.route('/se_education_core/se_education_core', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/se_education_core/se_education_core/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('se_education_core.listing', {
#             'root': '/se_education_core/se_education_core',
#             'objects': http.request.env['se_education_core.se_education_core'].search([]),
#         })

#     @http.route('/se_education_core/se_education_core/objects/<model("se_education_core.se_education_core"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('se_education_core.object', {
#             'object': obj
#         })
