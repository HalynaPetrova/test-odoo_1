from odoo import models, fields, api

class Doctor(models.Model):
    _name  = 'hospital.doctor'
    _inherit = 'hospital.person.mixin'
    
    speciality = fields.Char()
    state = fields.Selection([('male', 'Male'),('female', 'Female')])
    

