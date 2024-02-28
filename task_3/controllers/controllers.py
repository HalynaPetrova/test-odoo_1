# -*- coding: utf-8 -*-
# from odoo import http


# class Task3(http.Controller):
#     @http.route('/task_3/task_3', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/task_3/task_3/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('task_3.listing', {
#             'root': '/task_3/task_3',
#             'objects': http.request.env['task_3.task_3'].search([]),
#         })

#     @http.route('/task_3/task_3/objects/<model("task_3.task_3"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('task_3.object', {
#             'object': obj
#         })
