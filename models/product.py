# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_equipment = fields.Boolean(string='Is an equipment')
    team_id3 = fields.Many2one('booking.team')


