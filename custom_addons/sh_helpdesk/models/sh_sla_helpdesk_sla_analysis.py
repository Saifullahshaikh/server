# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
from odoo import models, fields


class HelpdeskSlaAnalysis(models.Model):
    _name = "sh.helpdesk.sla.analysis"
    _description = "Helpdesk SLA Analysis"
    _rec_name = 'sh_sla_id'
    
    sh_sla_status_id = fields.Many2one(string='SLA Status', comodel_name='sh.helpdesk.sla.status')

    sh_sla_status_deadline = fields.Datetime('Deadline')

    sh_sla_status_reached = fields.Datetime('Reached')

    sh_helpdesk_ticket_id = fields.Many2one(
        'sh.helpdesk.ticket', string='Ticket')

    sh_reached_duration = fields.Float('Reached Duration')

    sh_late_duration = fields.Float('Late Duration')

    sh_sla_id = fields.Many2one('sh.helpdesk.sla',string="SLA")

    sh_ticket_stage_id = fields.Many2one('helpdesk.stages', string='Ticket Stage')