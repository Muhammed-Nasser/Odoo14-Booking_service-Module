# -*- coding: utf-8 -*-
from datetime import timedelta, datetime

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class SalesOrder(models.Model):
    _inherit = "sale.order"

    is_booking = fields.Boolean(string="Is a booking")

    team_id2 = fields.Many2one('booking.team', string='Team')
    team_leader = fields.Many2one('hr.employee', string='Team Leader', related='team_id2.team_leader', store=True,
                                  readonly=False)
    employee_ids = fields.One2many('hr.employee', 'team_id1', string="Employees", related='team_id2.employee_ids',
                                   readonly=False)
    equipment_ids = fields.One2many('product.template', 'team_id3', string="Equipments",
                                    domain="[('is_equipment', '=', True)]", related='team_id2.equipment_ids',

                                    readonly=False,
                                    )
    booking_start = fields.Datetime(string="Booking Start", default=datetime.now())
    booking_end = fields.Datetime(string="Booking End", compute='_default_booking_end', readonly=False)

    @api.onchange('booking_start')
    def _default_booking_end(self):
        self.booking_end = self.booking_start + timedelta(hours=1)

    def check_action(self):
        for rec in self:
            # print(rec.employee_ids)

            employees = []
            events_name = []
            if rec.team_leader:
                if rec.env['calendar.event'].search(
                        [('partner_ids', '=', rec.team_leader.id)]):
                    events = rec.env['calendar.event'].search(
                        [('partner_ids', '=', rec.team_leader.id)])
                    for i in events:
                        if rec.booking_start >= i.start and rec.booking_start < i.stop:
                            employees.append(rec.team_leader.name)
                            events_name.append(i.name)
                            # print(events)
            if rec.equipment_ids:
                for x in rec.equipment_ids:
                    if rec.env['calendar.event'].search(
                            [('equipments_ids.product_id', '=', i.id)]):
                        events = rec.env['calendar.event'].search(
                            [('equipments_ids.product_id', '=', i.id)])
                        for i in events:
                            if rec.booking_start >= i.start and rec.booking_start < i.stop:
                                employees.append(x.name)
                                events_name.append(i.name)
                                # print(events)
            if rec.employee_ids:
                for x in rec.employee_ids:
                    if rec.env['calendar.event'].search(
                            [('partner_ids', '=', i.id)]):
                        events = rec.env['calendar.event'].search(
                            [('partner_ids', '=', i.id)])
                        for i in events:
                            if rec.booking_start >= i.start and rec.booking_start < i.stop:
                                employees.append(x.name)
                                events_name.append(i.name)
                                # print(events)
            else:
                raise ValidationError("add team")

            if employees:
                raise ValidationError(f"{employees},{set(events_name)}")

            else:
                # valid.append(1)
                # if valid:
                #     print(valid)
                raise ValidationError("Everyone is available for the booking!")
