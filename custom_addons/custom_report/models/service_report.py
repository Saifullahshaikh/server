from typing import Self
from odoo import api, fields, models

class CustomReportTemplate(models.Model):
    _inherit="purchase.order"
    # word_num = fields.Char(string = "Amount In Words:", compute = '_amount_in_word')
    # def _amount_in_word(self): 
    #     for rec in self: 
    #         rec.word_num = str(rec.currency_id.amount_to_text(rec.amount_total))

    def product_quantity(self):
        product_check = []
        final_order_line = []


        for order in self:
                for line in order.order.line:
        # for d in purchase.order.lines:
                    temp_dict = {'product_name' : None,
                                'quantity': 0,
                    }
                    
                    if line['name'] not in product_check:
                        product_check.append(line['name'])
                        temp_dict['product_name'] = line['name']
                        temp_dict['quantity'] = line["product_qty"]
                        temp_dict['sku'] = line['sku']
                        
                        final_order_line.append(temp_dict)
                    
                    else:
                        index = product_check.index(line['name'])
                        final_order_line[index]['quantity'] += line["product_qty"]
                        
                for i in final_order_line:
                    print("self.env['purchase.order.line'].create({'product_id':"+i['product_name']+"})")
        print(final_order_line)