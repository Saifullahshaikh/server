from odoo import api, models, fields


class PatientTag(models.Model):
    _name = 'patient.tag'
    _description = 'Patient Tag'
    

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active', default=True, copy=False)
    color = fields.Integer(string='Color')

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get('name'):
            default['name'] = self.name + "(copy)"
        return super(PatientTag, self).copy(default)

    _sql_constraints = [
        ('unique_tag_name', 'unique (name, active)','Name must be unique' )
    ] 