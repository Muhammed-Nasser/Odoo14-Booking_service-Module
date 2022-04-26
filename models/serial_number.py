# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools

class SerialNumber(models.Model):
    _inherit = 'stock.production.lot'

    event_id = fields.Many2one('calendar.event')

    events_count = fields.Integer(string='Events', compute='_compute_vents_count')

    def _compute_vents_count(self):
        for rec in self:
            num = rec.env['calendar.event'].search_count([('equipments_ids', '=', rec.id)])
            rec.events_count = num
            print(num)

    def action_open_event(self):
        action = self.env['ir.actions.actions']._for_xml_id('calendar.action_calendar_event')
        # condition
        action['domain'] = [('equipments_ids', '=', self.id)]

        return action
