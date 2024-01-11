{    
    'name':'Logo Print Extension',
    'category': 'Website/Website',
    'version': '1.1',
    'author': 'kobros-tech (Mohamed Moustafa Alkobrosli)',
    'website':'http://www.kobros-tech.com',
    'summary': "Custom module for frontend & backend shop website, and backend system.",
    'sequence': 1,

    'description':"""
    This module enables us to store the chosen submitted logos by customers in a stand-alone model.\n
    In addition to that, the administrator can upload the collection of logo positions on the website.
    """,

    'category':'Website',
    'depends': [
        'mail',
        'sale_management',
        'website_sale',
    ],
    'data': [
        'security/logo_print_security.xml',
        'security/ir.model.access.csv',
        'data/product_attribute.xml',
        'views/logo_library_view.xml',
        'views/positions_view.xml',
        'views/printing_collection.xml',
        'views/logo_library_menus.xml',
        'views/template.xml',
        'views/order_logos.xml',
    ],
    'assets': {
        'web.assets_frontend':[            
            'logo_print/static/src/js/validate.js',
            'logo_print/static/**/*',
        ],  
    }
}