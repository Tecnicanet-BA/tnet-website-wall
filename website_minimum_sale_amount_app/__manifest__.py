# -*- coding: utf-8 -*-
{
    'name': 'Website Minimum Order Amount',
    "author": "Edge Technologies",
    'version': '15.0.1.2',
    'description': """ 
        Website minimum cart value app
    """,
    "summary" : 'Website minimum cart value website minimum order value website minimum sale amount website minimum product amount shop minimum order amount shop minimum sale amount cart minimum amount order min amount odoo shop minimum order value website minimum amount.',
    'live_test_url': "https://youtu.be/7QnedjqXM2Y",
    "images":["static/description/main_screenshot.png"],
    "license" : "OPL-1",
    'depends': ['base','website_sale','website','sale_management','sale','web'],
    'data': [ 
        'views/res_company.xml',
        'views/res_config_settings.xml',
        'views/template.xml',
        'views/assets.xml',
            ],
    'installable': True,
    'auto_install': False,
    'price': 10,
    'currency': "EUR",
    'category': 'Website',
    'assets': {
        'web.assets_frontend': [
            'website_minimum_sale_amount_app/static/src/js/sale_min_amounts.js',
        ],
    },
}
