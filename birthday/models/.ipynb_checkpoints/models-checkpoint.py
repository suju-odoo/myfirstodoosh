# -*- coding: utf-8 -*-

from odoo import models, fields, api


class partner(models.Model):
    _inherit = 'res.partner'
    birthday = fields.Datetime('Date of birth')


