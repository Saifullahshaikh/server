from odoo import api, models, fields
from odoo.exceptions import ValidationError
import datetime

class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'
    

    @api.model
    def default_get(self, fields):
        res = super(CancelAppointmentWizard, self).default_get(fields)
        res['date_cancel'] = datetime.date.today()
        print("...context", self.env.context)
        return res

    appointment_id = fields.Many2one('hospital.appointment', string="Appoinment", domain=[('state','=','draft'),('priority','in',('1','0',False))])
    reason = fields.Text(string='Reason')
    date_cancel = fields.Date(string="Cancellation Date")


    def action_cancel(self):
        if self.appointment_id.booking_date == fields.Date.today():
            raise ValidationError("Sorry, cancellation is not allowed on same day of booking !")
        return