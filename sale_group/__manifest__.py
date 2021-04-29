{
    'name': 'Sale Groups',
    'version': '14.0.1.0.0',
    'installable': True,
    'category': 'Sale Groups',
    'author': 'Phanker',
    'website': '#',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'sale_management',
        'sales_team',
    ],
    'data': [
        # Data1

        # Security
        'security/ir.model.access.csv',
        'security/sale_group_security.xml',
        # Data2

        # Views
        'views/crm/crm_team_view.xml',
        'views/crm/sale_group_view.xml',
        'views/sale/sale_order_view.xml',
        # wizard

        # Menu
        'menu/menu.xml',
        #Report

        # Security
    ],
    'application': False,
}
