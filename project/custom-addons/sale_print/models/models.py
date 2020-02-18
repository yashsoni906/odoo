# -*- coding: utf-8 -*-

from odoo import models, fields, api

class sale_print(models.Model):

    _name='sale.print'


class sale_inheritance(models.Model):
    _inherit='sale.order'
