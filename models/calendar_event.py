# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    partner_ids = fields.Many2many(
        'hr.employee', 'hr_employee_id', default="")
    equipments_ids = fields.One2many('stock.production.lot', 'event_id', string='Equipments')



