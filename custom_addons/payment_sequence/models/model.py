from odoo import fields, models, api, _
from datetime import datetime ,date ,timedelta
from odoo.exceptions import UserError


class payment_inherit(models.Model):
    _inherit ='account.payment'
    inbound_code = fields.Integer(default=0)
    outbound_code = fields.Integer(default=0)
    payment_type = fields.Selection([
    ('outbound', 'Send'),
    ('inbound', 'Receive')],
    string='Payment Type', required=True, default='inbound')

    @api.model
    def create(self, vals):
        
        payment_inbound = 'inbound'
        # raise UserError(f'{vals["inbound_code"]} = {vals["outbound_code"]}')
        codes = self.env['account.payment'].search(['|', ('inbound_code', '!=', False), ('outbound_code', '!=', False)])
        inbound_codes = []
        outbound_codes = []

        for code in codes:
            if code.payment_type == payment_inbound:
                inbound_codes.append(str(code.inbound_code))
            else:
                outbound_codes.append(str(code.outbound_code))

        if len(outbound_codes) == 0:
            outbound_codes.append(0)
        if len(inbound_codes) == 0:
            inbound_codes.append(0)

        company_id = self.env.company.id
        # Custom logic for other Company IDs
        self.Generate_Payement_name(vals=vals,company_id=company_id,inbound_codes=inbound_codes,outbound_codes=outbound_codes)       

        # # Call the original create() method to perform the default behavior
        return super(payment_inherit, self).create(vals)
    @api.model
    def _get_default_payment_type(self):
        return 'outbound'

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):

        if self._context.get('payment_type') == 'outbound':
            args += [('payment_type', '=', 'outbound')]
        if self._context.get('payment_type') == 'inbound':
            args += [('payment_type', '=', 'inbound')]
            

        return super(payment_inherit, self).search(args, offset=offset, limit=limit, order=order, count=count)
    
    def Generate_Payement_name(self,vals,company_id,inbound_codes,outbound_codes):
        payment_inbound = 'inbound'
        company_literals = ['TAP','TA',str(self.env.company.name[0:3])]
        payment_type_literals = ['PV','PRV']

        if company_id >=len(company_literals):
            company_id = len(company_literals)-1

        if vals['payment_type'] == payment_inbound:         
            vals['inbound_code'] = int(max(inbound_codes))+1
            vals['name'] = f"{company_literals[company_id-1]}-{payment_type_literals[1]}-{str(vals['inbound_code'])}"
            
           
        else:
            vals['outbound_code'] = int(max(outbound_codes))+1
            vals['name'] = f"{company_literals[company_id-1]}-{payment_type_literals[0]}-{str(vals['outbound_code'])}"
            
            

#    TAP SOURCING
# Receive : TAP-PRV-1
# send : TAP-PV-1

# TA Trader
# Receive: TA-PRV-1
# Send: TA-PV-1