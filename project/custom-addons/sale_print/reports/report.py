from odoo import models



class report(models.AbstractModel):
    _name = 'report.sale_print.report_saleorder'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xls_report(self, workbook, data, lines):

        sheet = workbook.add_worksheet('sale orders')

        sheet.write(0,0,'yash')