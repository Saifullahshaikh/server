# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ["mail.thread","mail.activity.mixin"]
    _description = "Hospital Appointment"
    _rec_name = 'patient_id'

    patient_id = fields.Many2one(string='Patient', comodel_name='hospital.patient', ondelete="restrict")
    gender = fields.Selection(related='patient_id.gender')
    appointment_time = fields.Datetime(string= "Appointment Time",default= fields.Datetime.now())
    booking_date = fields.Date(string='Booking Date')
    ref = fields.Char(string="Reference", help="Reference from patient")
    prescription = fields.Html(string='Prescription')
    priority = fields.Selection([
         ("o", "Normal"),
         ("1", "low"),
         ("2", "high"),
         ("3", "very high")], string="Priority",
         help="gives the sequence order when displaying appoinments")
    state = fields.Selection([
         ("draft", "Draft"),
         ("in_consultation", "In Consultation"),
         ("done", "Done"),
         ("cancel", "Cancel")], string="Status",
         help="gives the sequence order when displaying appoinments")
    doctor_id = fields.Many2one("res.users", string="Docter")
    pharmacy_line_ids = fields.One2many('appointment.pharmacy.lines','appointment_id', string='Pharmacy Lines')
    hide_sale_price = fields.Boolean(strign='Hide Sale Price')
    image = fields.Image(string='Image')


    @api.onchange('patient_id')
    def onchange_patient_id(self):
         self.ref = self.patient_id.ref

    def action_test(self):
         print("onclick Butoon...")
         return {
              'effect':{
                   'fadeout':'slow',
                   'message':'Click Successfull',
                   'type':'rainbow_man',
              }
         }
    def unlink(self):
         if self.state != 'draft':
              raise ValidationError("Only appointments in draft state can be deleted !")
         return super(HospitalAppointment, self).unlink()

    def action_in_consultation(self):
         for rec in self:
              rec.state = "in_consultation"

    def action_draft(self):
         for rec in self:
              rec.state = "draft"

    def action_done(self):
         for rec in self:
              rec.state = "done"

    def action_cancel(self):
         for rec in self:
              rec.state = "cancel"

class AppointmentPharmacyLines(models.Model):
     _name = 'appointment.pharmacy.lines'
     _description = 'Appointment Pharmacy Lines'
     #_inherits = {'product.template': 'product_tmpl_id'}


     product_id = fields.Many2one('product.product')
     price_unit = fields.Float(related='product_id.list_price')
     quantity = fields.Integer(string='Quantity',default=1)
     appointment_id = fields.Many2one('hospital.appointment', string='Appointment')

