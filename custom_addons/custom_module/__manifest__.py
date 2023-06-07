{
    'name': 'Custom Module',
    'version': '1.0',
    'summary': 'Custom module to change field name',
    'author': 'Your Name',
    'depends': ['base', 'account'],  # Add any other module dependencies here
    'data': [
        'views/custom_view.xml',
    ],
    'installable': True,
    'application': True,
}
