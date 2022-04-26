# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools


class BookingTeam(models.Model):
    _name = 'booking.team'

    name = fields.Char(string="Team Name", required=True)
    team_leader = fields.Many2one('hr.employee', string='Team Leader', required=True)
    employee_ids = fields.One2many('hr.employee', 'team_id1', string="Employees", required=True)
    orders_ids = fields.One2many('sale.order', 'team_id2', string="Employees", required=True)
    equipment_ids = fields.One2many('product.template', 'team_id3', string="Equipments",
                                    domain="[('is_equipment', '=', True)]", required=True)
