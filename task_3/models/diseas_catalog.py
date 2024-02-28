from odoo import models, fields

class DiseasCatalog(models.Model):
    _name  = 'hospital.diseas.catalog'
    _parent_name = 'parent_id'
    _parent_store = True

    name = fields.Char('Name', index=True, required=True)
    parent_id = fields.Many2one('hospital.diseas.catalog', 'Parent Catalog', index=True, ondelete='cascade')
    parent_path = fields.Char(index=True)
    child_id = fields.One2many('hospital.diseas.catalog', 'parent_id', 'Child Categories')
    patient = fields.Many2one('hospital.patient', index=True, ondelte='cascade')    
    importance = fields.Selection([('Important', 'Important'),('noImportant', 'No Important')])
