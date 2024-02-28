from odoo import models, fields

class ContactPerson(models.Model):
    _name  = 'hospital.contact.person'
    _inherit = 'hospital.person.mixin'


    
