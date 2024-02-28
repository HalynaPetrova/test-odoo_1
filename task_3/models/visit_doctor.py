from odoo import models, fields, api

class VisitDoctor(models.Model):
    _name  = 'hospital.visit.doctor'
    doctor = fields.Many2one('hospital.doctor', ondeelte='cascade')
    patient = fields.Many2one('hospital.patient', ondeelte='cascade')
    appointment_date = fields.Datetime('Date')
    diagnos = fields.Char()
    recomendation = fields.Text()





