from odoo import api, models, fields


class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'
    

    appointment_id = fields.Many2one('hospital.appointment', string="Appoinment")
    reason = fields.Text(string='Reason')


    def action_cancel(self):
        return