# -*- coding: utf-8 -*-
from odoo import api, fields, models
from datetime import date

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

    @api.depends('dob')
    def _compute_age(self):
        for rec in self:
            today=  date.today()
            if rec.dob:
                rec.age = today.year - rec.dob.year
            else:
                rec.age = 1

    