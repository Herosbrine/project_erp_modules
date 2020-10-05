# -*- coding: utf-8 -*-
{
    'name': "project_document",

    'summary': """
        gestion de project pour les missions Raoul Follereau au moyent orient""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Fondation Raoul Follereau",
    'website': "https://www.raoul-follereau.org/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Documents',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'document.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}
