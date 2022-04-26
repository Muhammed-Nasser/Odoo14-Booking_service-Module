# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class SalesOrder(models.Model):
    _inherit = "sale.order"

    is_booking = fields.Boolean(string="Is a booking")

    team_id2 = fields.Many2one('booking.team', string='Team')
    team_leader = fields.Many2one('hr.employee', string='Team Leader', related='team_id2.team_leader', store=True, readonly=False)
    employee_ids = fields.One2many('hr.employee', 'team_id', string="Employees", related='team_id2.employee_ids', store=True,
                                   readonly=False)
    equipment_ids = fields.One2many('product.template', 'team_id', string="Equipments",
                                    domain="[('is_equipment', '=', True)]", related='team_id2.equipment_ids', store=True,
                                    readonly=False)
