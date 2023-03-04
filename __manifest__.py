# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Gestion_aeroport',
    'version': '10.0.1',
    'description': '',
    'summary': """Gestion Aeroport
        ====================
Ce module est implémenté pour une société aérienne qui voudrait gérer son système d'information pour une 
meilleure gestion de son transport. L'objectif est d'assurer la gestion, d'une part des 
employés, des vols et des appareils, et d'autre part des clients et des billets.
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
        'data/template_mail.xml',
        'report/aeroport_report_template.xml',
        'report/aeroport_report.xml',
        'report/pilote_template.xml',
        'report/pilote_report.xml',
        'report/equipage_report.xml',
    ],
    'demo': [
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}
