from odoo import fields, models, _, api


class CreateEventWizard(models.TransientModel):
    _name = 'create.event.wizard'
    _description = 'Create Event Wizard'

    def check(self):
        id = self._context.get('active_id')
        active_id = self.env['sale.order'].search([('id', '=', id)])
        active_id.check_action()

    def action_create_event(self):
        id = self._context.get('active_id')
        active_id = self.env['sale.order'].search([('id', '=', id)])
        equipments = (self.env['stock.production.lot'].search([('product_id', '=', '0')]))

        for i in active_id.equipment_ids:
            equipments += (self.env['stock.production.lot'].search([('product_id', '=', i.id)]))

        vals = {
            'name': active_id.name,
            'partner_ids': active_id.employee_ids,
            'equipments_ids': equipments,
            'start': active_id.booking_start,
            'stop': active_id.booking_end,
        }
        self.env['calendar.event'].create(vals)






