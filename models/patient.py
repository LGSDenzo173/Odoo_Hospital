# -*- coding: utf-8 -*-

from odoo import models, fields, api


class hospitalpatient(models.Model):
    _name = 'hospital.patient'
    _description = 'hospital.patient'

    name = fields.Char(string='Name', required=True)
    age= fields.Integer(string='Age')
    is_married = fields.Boolean(string='is Married ?')
    gender=fields.Selection([('male','Male'),('female','Female'),('other','Other')],string='Gender')
    
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
