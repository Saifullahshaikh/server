from odoo import models, fields,api

class SaleOrderCustom(models.Model):
    _inherit = 'sale.report'

    custom_field = fields.Integer(related='order_id.order_line.id',string='New Field')

   
