from odoo import api, fields, models
from odoo.exceptions import ValidationError

class CustomSaleOrderLines(models.Model):
   _inherit = "sale.order.line"

