# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class learn_amir(models.Model):
#     _name = 'learn_amir.learn_amir'
#     _description = 'learn_amir.learn_amir'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
