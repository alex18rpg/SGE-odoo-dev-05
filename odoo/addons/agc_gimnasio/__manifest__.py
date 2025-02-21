# -*- coding: utf-8 -*-
{
    'name': "agc_gimnasio",

    'summary': "Modulo de gestion de un Gimnasion Pokemon",

    'description': """
Modulo de Gestion de Gimansin Pokemon para SGE <br/>
Gestion de un gimnasion pokemon
    """,

    'author': "Alex Gabriel Chirascu",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/equipo.xml',
        'views/lider.xml',
        'views/subdito.xml',
        'views/menus.xml',
        'views/entrenador.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'icon': 'static/description/icono.png'
}

