# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name":"Helpdesk",
    "author":"Softhealer Technologies",
    "website":"https://www.softhealer.com",
    "support":"support@softhealer.com",
    "category":"Discuss",
    "license":"OPL-1",
    "summary":"Flexible HelpDesk Customizable Help Desk Service Desk HelpDesk With Stages Help Desk Ticket Management Helpdesk Email Templates Helpdesk Chatter manage customer support ticket system ticket portal support Timesheet Email Alias Email Apps for purchase Material Requisitions Request  purchase product Requisitions Request Material Requisition for tender Material Requisition for manufacturing order Product Request on RFQ Product Request on Tender Product Request on manufacturing order Odoo",
    "description":"""Are you looking for a fully flexible and customizable helpdesk in odoo? Our this apps almost contain everything you need for Service Desk, Technical Support Team, Issue Ticket System which include service request to be managed in Odoo backend. The support ticket will send by email to the customer and admin. Customer can view their ticket from the website portal and easily see the stage of the reported ticket. This desk is fully customizable clean and flexible. """,
    "version":"16.0.6",
    "depends": ["mail","portal","product","resource",],
    "data": [
        "security/sh_helpdesk_security.xml",
        "security/ir.model.access.csv",
        "data/sh_helpdesk_email_data.xml",
        "data/sh_helpdesk_data.xml",
        "data/sh_helpdesk_cron_data.xml",
        "data/sh_helpdesk_stage_data.xml",
        "views/sh_helpdesk_menu.xml",
        "views/sh_helpdesk_sla_policies.xml",
        "views/sh_helpdesk_alarm.xml",
        "data/sh_helpdesk_reminder_cron.xml",
        "data/sh_helpdesk_reminder_mail_template.xml",
        "data/sh_helpdesk_ticket_stage_overdue.xml",
        "views/sh_helpdesk_team_view.xml",
        "views/sh_helpdesk_ticket_type_view.xml",
        "views/sh_helpdesk_subject_type_view.xml",
        "views/sh_helpdesk_tags_view.xml",
        "views/sh_helpdesk_stages_view.xml",
        "views/sh_helpdesk_category_view.xml",
        "views/sh_helpdesk_subcategory_view.xml",
        "views/sh_helpdesk_priority_view.xml",
        "views/sh_helpdesk_config_settings_view.xml",
        "views/sh_helpdesk_ticket_view.xml",
        "views/sh_report_helpdesk_ticket_template.xml",
        "views/sh_helpdeks_report_portal.xml",
        "views/sh_report_views.xml",
        "views/sh_ticket_feedback_template.xml",
        "views/sh_ticket_dashboard_templates.xml",
        "views/res_users.xml",
        "views/sh_helpdesk_merge_ticket_action.xml",
        "views/sh_helpdesk_ticket_multi_action_view.xml",
        "views/sh_helpdesk_ticket_update_wizard_view.xml",
        "views/sh_helpdesk_ticket_portal_template.xml",
        "views/sh_helpdesk_ticket_task_info.xml",
        "views/sh_helpdesk_ticket_megre_wizard_view.xml",
        "views/sh_helpdesk_sla_analysis.xml",
        "wizard/mail_compose_view.xml",
    ],
    'assets': {
        'web.assets_backend': [
            'sh_helpdesk/static/src/xml/**/*',
            'sh_helpdesk/static/src/js/helpdesk_ticket_kanban_examples.js',
            # 'sh_helpdesk/static/src/js/action_manager_act_window.js',
            'sh_helpdesk/static/src/js/ticket_dashboard.js',
            'sh_helpdesk/static/src/css/ticket_dashboard.css',
            'sh_helpdesk/static/src/js/helpdesk_ticket_dasboard.js'
            'sh_helpdesk/static/src/js/dashboard_pagination.js'
        ],
        'web.assets_frontend': [
            'sh_helpdesk/static/src/css/feedback.scss',
            'sh_helpdesk/static/src/js/portal.js',
            'sh_helpdesk/static/src/css/bootstrap-multiselect.min.css',
            'sh_helpdesk/static/src/js/bootstrap-multiselect.min.js',
        ],
    },
    "images": [
        'static/description/background.png',
    ],
    "application":
    True,
    "auto_install":
    False,
    "installable":
    True,
    "price":
    "40",
    "currency":
    "EUR"
}
