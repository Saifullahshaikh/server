# -*- coding: utf-8 -*-
from odoo import api, fields, models

class PlayGround(models.Model):
    _name = "play.ground"
    _description = "Play Ground"

    DEFAULT_ENV_VARIABLES = """# Available variables:
    # - self: Current Object
    # 
    # 
    # 
    # 
    # """
    model_id = fields.Many2one('ir.model', string="Model")
    code = fields.Text(string="Code", default=DEFAULT_ENV_VARIABLES)
    result = fields.Text(string="Result")

    def action_execute(self):
        try:
            if self.model_id:
                model = self.env[self.model_id.model]
            else:
                model = self
            self.result = safe_eval(self.code.strip(),{'self':model})
        except Exception as e:
            self.result = str(e)

