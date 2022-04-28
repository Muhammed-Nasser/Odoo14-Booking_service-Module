# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools


class ProductTemplate(models.Model):
    _inherit = 'hr.employee'

    events_count = fields.Integer(string='Events', compute='_compute_vents_count')
    team_id1 = fields.Many2one('booking.team')

    def _compute_vents_count(self):
        for rec in self:
            num = rec.env['calendar.event'].search_count([('partner_ids', '=', rec.id)])
            rec.events_count = num
            print(num)

    def action_open_event(self):
        action = self.env['ir.actions.actions']._for_xml_id('calendar.action_calendar_event')
        # condition
        action['domain'] = [('partner_ids', '=', self.id)]
        '''to set default value for doctor_id 
                when create new appointment by click on create in doctor's appointments view'''
        # action['context'] = {'default_doctor_id': self.id}
        return action
