from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import pager

class MyController(http.Controller):

    @http.route('/sh_helpdesk/get_records', type='http', auth='public')
    def get_records(self, page=1, per_page=1):
        record_model = request.env['ticket.daskboard']
        offset = (page - 1) * per_page
        total_records = record_model.search_count([])
        page_detail = pager(url='/sh_helpdesk/get_records',
                            total=total_records,
                            page=page,
                            step=1,
                            
        )
        records = record_model.search([], offset=page_detail["offset"], limit=1)
        vals = {'tickets':records,'page_name':'tickets_dashboard','pager':page_detail}
        return {
            'records': records.read(),
            'total_records': len(records),
        }
