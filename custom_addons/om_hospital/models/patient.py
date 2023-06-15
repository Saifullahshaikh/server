# -*- coding: utf-8 -*-
from odoo import api, fields, models
from datetime import date
from odoo.exceptions import ValidationError
class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread","mail.activity.mixin"]
    _description = "Hospital Patient"

    name = fields.Char(string='Name', tracking=True)
    ref = fields.Char(string="Reference", tracking=True)
    dob = fields.Date(string="Date of Birth")
    age = fields.Integer(string='Age', compute= '_compute_age',tracking=True)
    gender = fields.Selection([('male', 'Male'),('female','Female')], string='Gender', tracking=True)
    active = fields.Boolean(string="Active", default=True)
    appointment_id = fields.Many2one(string='Appointment', comodel_name='hospital.appointment')
    tag_ids = fields.Many2many('patient.tag', string="Tag")
    appointment_count = fields.Integer(string="Appointment Count",compute="_compute_appointment_count",stored=True )
    appointment_ids = fields.One2many('hospital.appointment','patient_id', string='Appointments')
    parent = fields.Char(string="Parent")
    martial_status = fields.Selection([('single',"Single"),('married','Married' )], string="Martial Status")
    partner_name = fields.Char(string="Partner Name")
    @api.model
    def create(self,vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient,self).create(vals)

    def write(self,vals):
        if not self.ref:
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient,self).write(vals)

    @api.constrains('dob')
    def _check_date_of_birth(self):
        for rec in self:
            if rec.dob and rec.dob > fields.Date.today():
                raise ValidationError("Entered date of birth is not accepted")
    @api.depends('dob')
    def _compute_age(self):
        for rec in self:
            today=  date.today()
            if rec.dob:
                rec.age = today.year - rec.dob.year
            else:
                rec.age = 1
    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        for rec in self:
            rec.appointment_count = self.env["hospital.appointment"].search_count([('patient_id','=',rec.id)])

    # def name_get(self):
    #     patient_list = []
    #     for record in self:
    #         name = record.ref + ' ' + record.name
    #         patient_list.append((record.id,name))
    #     return patient_list

    # by list comprehension
    
    def name_get(self):
        return [(record.id, "%s:%s"% (record.ref,record.name)) for record in self]