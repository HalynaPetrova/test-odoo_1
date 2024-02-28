from odoo import models, fields, api

class Patient(models.Model):
    _name  = 'hospital.patient'
    _inherit = 'hospital.person.mixin'

    age = fields.Integer(compute='_compute_age')
    date_of_birth = fields.Date('Date of birthday')
    passport = fields.Char()
    contact_person = fields.Many2one(comodel_name='hospital.contact.person', ondelete='cascade')
    personal_doctor = fields.Many2one(comodel_name='hospital.doctor', ondelete='cascade')


    @api.depends('age')
    def _compute_age(self):
        for obj in self:
            if obj.date_of_birth:
                today = fields.Date.today()
                obj.age = today.year - obj.date_of_birth.year
                if obj.date_of_birth.month >= today.month and obj.date_of_birth.day > today.day:
                    obj.age -= 1
            else: obj.age = 0


    def write(self, vals):
        print(self, vals)
        if 'personal_doctor' in vals:
            self.env['hospital.personal.doctor.history'].create({'patient': self.id, 'doctor': vals['personal_doctor'], 'date': fields.Datetime.now()})
        return super().write(vals)
