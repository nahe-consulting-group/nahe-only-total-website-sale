# -*- coding: utf-8 -*-
{
    'name': "Nähe custom JM",

    'summary': """ 
        Editar vista del carrito para no mostrar subtotal""",

    'description': """
     
    """,

    'author': "Nähe Consulting Group",
    'website': "http://www.nahe.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/webiste_sale_total.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
       
    ],
}
