from odoo import models, fields, api

class PersonMixin(models.AbstractModel):
    _name  = 'hospital.person.mixin'
    _rec_name = 'full_name'
    
    first_name = fields.Char()
    last_name = fields.Char()
    surname = fields.Char()
    gender = fields.Selection([('male', 'Male'),('female', 'Female')])
    phone = fields.Char()
    mail = fields.Char()
    full_name = fields.Char(compute='_compute_full_name')


    @api.depends('first_name', 'last_name')
    def _compute_full_name(self):
        for obj in self:
            obj.full_name = f"{obj.first_name} {obj.last_name}"


