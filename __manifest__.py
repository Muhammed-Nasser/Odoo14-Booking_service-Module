# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Booking Service',
    'version': '1.0',
    'author': 'Muhammad Nasser',
    'summary': 'Booking Service',
    'sequence': 10,
    'description': """ To allow users to create bookings for employees and equipments """,
    'category': 'Productivity',
    'depends': ['base',
                'sale',
                'stock',
                'calendar',

                ],
    'data': [
        # orders security => data => wizard => views => report
        'security/ir.model.access.csv',
        'views/product.xml',
        'views/calendar_event.xml',
        'views/hr_employee.xml',
        'views/serial_number.xml',
        'views/team_view.xml',
        'views/sale.xml',
        'views/booking_order.xml',
        'views/menu.xml',

    ],
    'demo': [],
    'qweb': [],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
