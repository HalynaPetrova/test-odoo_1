from odoo import models, fields, api

class DoctorIntern(models.Model):
    _inherit = 'hospital.doctor'
    
    doctor_mentor = fields.Many2one('hospital.doctor')


    @api.onchange('doctor_mentor')
    def doctor_filter(self):
        res = {}

        print(type(self.doctor_mentor))


        # if self.patient.first_name == 'Oleksandr' and self.doctor.first_name == 'Doctor1' :
        #     res['warning'] = {'title': _('Error!'), 'message': _('You cannot disable this setting.') }
        return res

    

