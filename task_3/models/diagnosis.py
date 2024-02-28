from odoo import models, fields, api

class Diagnosis(models.Model):
    _name  = 'hospital.diagnosis'
    
    doctor = fields.Many2one(comodel_name='hospital.doctor', ondelete='cascade')
    patient = fields.Many2one(comodel_name='hospital.patient', ondelete='cascade')
    disease = fields.Char()
    recommendations = fields.Text()
    date = fields.Datetime(default = lambda self: fields.Datetime.now())
        

    @api.onchange('doctor')
    def doctor_filter(self):
        res = {}
        if self.patient.first_name == 'Oleksandr' and self.doctor.first_name == 'Doctor1' :
            res['warning'] = {'title': _('Error!'), 'message': _('You cannot disable this setting.') }
        return res
        # if self.patient.first_name == 'Oleksandr':
        #     return {'domain': {'doctor': [('gender', '!=', 'Female')]}}
        # else:
        #     return {'domain': {'doctor': []}}
     
            
            
            


    
    


