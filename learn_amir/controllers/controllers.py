# -*- coding: utf-8 -*-
# from odoo import http


# class LearnAmir(http.Controller):
#     @http.route('/learn_amir/learn_amir/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/learn_amir/learn_amir/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('learn_amir.listing', {
#             'root': '/learn_amir/learn_amir',
#             'objects': http.request.env['learn_amir.learn_amir'].search([]),
#         })

#     @http.route('/learn_amir/learn_amir/objects/<model("learn_amir.learn_amir"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('learn_amir.object', {
#             'object': obj
#         })
