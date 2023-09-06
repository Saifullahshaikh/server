# -*- coding: utf-8 -*-

{
    'name': 'Sale Order Line Sub Menu',
    'version': '1.0.0',
    'category': 'sales',
    'author':'odolution',
    'sequence': -100,
    'summary': 'Custom sale order sub menu',
    'description': """Custom sale order sub menu""",
    'depends': ['base','sale'],
    'data': [
        # 'views/order_line_menu.xml',
        'views/order_line_view.xml'
        
        ],
    'demo': [],
    'application':True,
    'installable': True,
    'assets': {},
    #'post_init_hook': '_synchronize_cron',
    'license': 'LGPL-3',
}
