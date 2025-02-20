# -*- coding: utf-8 -*-
{
    'name': "Libreria",

    'summary': "Modulo de ejemplo SGE",

    'description': """
Modulo de ejemplo SGE <br/>
Gestion de una libreria
    """,

    'author': "IES El Cañaveral",
    'website': "https://www.google.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '17.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/categoria.xml',
        'views/menus.xml',
        'views/libro.xml',
        'views/autor.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    # Quitar filtro aplication
    'application': False, 
    
 
}

