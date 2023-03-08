# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Gestion_aeroport',
    'version': '10.0.1',
    'description': '',
    'summary': """Gestion d'une compagnie aérienne
        """,
    'category': 'Gestion',
    'images': [],
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/equipage_views.xml',
        'views/pilote_views.xml',
        'views/depart_views.xml',
        'views/reservation_views.xml',
        'views/passager_views.xml',
        'views/vol_views.xml',
        'views/ligne_views.xml',
        'views/avion_views.xml',
        'views/aeroport_views.xml',
        'data/template_auto_mail.xml',
        'report/aeroport_report_template.xml',
        'report/aeroport_report.xml',

        'data/template_mail.xml',
    ],
    'demo': [
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}
