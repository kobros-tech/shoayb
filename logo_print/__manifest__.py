{    
    'name':'Logo Printing Extension Module',
    'version': '1.1',
    'author': 'kobros-tech (Mohamed Moustafa Alkobrosli)',
    'website':'https://www.kobros-tech.com',
    'summary': "Custom Website Portal",
    'sequence': 1,

    'description':"""Custom module for frontend & backend shop website ,and backend system.
    This module is enabling to store the choosen submitted logos by customers in a stand alone model.\n
    In addition to that, 
    the administrator is able to upload the collection of logo positions on website""",

    'category':'Website',
    'depends': [
        'mail',
        'sale_management',
        'website_sale',
    ],
    'data': [
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