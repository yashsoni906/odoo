from odoo import models, fields, api
import xlwt
import base64
from io import BytesIO
from io import StringIO


class Wizard(models.TransientModel):
    _name = 'sale_print.wizard'
    _description = "Wizard: Print in excel"

    order_id = fields.Many2many('sale.order',
        string="Quotation number", required=True)

    # @api.depends('order_id')

    def print_xls(self):
        # import pdb; pdb.set_trace()
        row = 0
        col = 0
        wb1 = xlwt.Workbook(encoding='utf-8')
        ws1 = wb1.add_sheet('Sales Order Report')
        style = xlwt.XFStyle()
        font = xlwt.Font()
        font.bold=True
        font.height = 240
        style.font = font
        ws1.write(row,col,'Quotation number',style)
        ws1.write(row,col+1,'Order Date',style)
        ws1.write(row,col+2,'Total',style)
        fp = BytesIO()
        for data in self.order_id:
            row = row+1
            ws1.write(row,col,data.name)
            ws1.write(row,col+1,data.date_order)
            ws1.write(row,col+2,data.amount_total)
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