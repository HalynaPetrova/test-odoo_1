from odoo import models, fields, api

class PersonalDoctorHistory(models.Model):
    _name  = 'hospital.personal.doctor.history'

    doctor = fields.Many2one(comodel_name='hospital.doctor', ondelete='cascade')
    patient = fields.Many2one(comodel_name='hospital.patient', ondelete='cascade')
    date = fields.Datetime()



