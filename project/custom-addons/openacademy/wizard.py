# -*- coding: utf-8 -*-

from odoo import models, fields, api
import xlwt
import base64
from io import BytesIO
from io import StringIO


class Wizard(models.TransientModel):
    _name = 'openacademy.wizard'
    _description = "Wizard: Print in excel"

    order_id = fields.Many2one('sale.order',
        string="Order Display", required=True)

    # @api.depends('order_id')
    def print_xls(self):

        # data=self.order_id.browse()
        wb1 = xlwt.Workbook(encoding='utf-8')
        ws1 = wb1.add_sheet('Sales Order Report')
        fp = BytesIO()
        ws1.write(0,0,'yash')
        ws1.write(2,2,'sjdfjf')
        wb1.save(fp)
        fp.seek(0)
        data = base64.encodestring(fp.read())
        attach_vals = {
            'name':'%s.xls' % ('sale_order_report'),
            'datas':data,
            'datas_fname':'%s.xls' % ('sale_order_report'),
            }
        doc_id = self.env['ir.attachment'].create(attach_vals)
        return {
            'type': 'ir.actions.act_url',
            'url':'web/content/%s?download=true' % (doc_id.id),
            'target': 'self',
            }

# class sale_print(models.Model):
#     _inherit='sale.order'
#     order_id=fields.Char(string='Order ID')