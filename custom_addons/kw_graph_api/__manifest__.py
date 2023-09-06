{
    'name': 'Facebook Graph Api',
    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',
    'version': '16.0.1.0.1',

    'license': 'Other proprietary',
    'category': 'Extra Tools',

    'depends': ['crm', 'website'],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/ir_cron_long_token.xml',
        'views/meny_views.xml',
        'views/res_config_settings_view.xml',
        'views/facebook_app_view.xml',
        'views/facebook_page_view.xml',
        'views/log_viewer_template.xml',
        'wizard/facebook_webhook_view.xml',
    ],

    'application': True,
}
