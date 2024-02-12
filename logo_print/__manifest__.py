# -*- coding: utf-8 -*-
#############################################################################
#
#    kobros-tech Pvt. Ltd.
#
#    Copyright (C) 2020-TODAY kobros-tech(<https://www.linkedin.com/in/mohamed-alkobrosly/>).
#    Author: Mohamed Alkobrosli(<https://www.linkedin.com/in/mohamed-alkobrosly/>)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (GPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU GENERAL PUBLIC LICENSE (GPL v3) for more details.
#
#    You should have received a copy of the GNU GENERAL PUBLIC LICENSE
#    (GPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

{
    'name':'Logo Print Extension',
    'category': 'Website/Website',
    'version': '16.0.0.0.1',
    'author': 'kobros-tech (Mohamed Moustafa Alkobrosli)',
    'company': 'kobros-tech',
    'contributors': [
        'Mohamed Moustafa Alkobrosli <alkobroslymohamed@gmail.com>', 
        'kobros-tech Pvt. Ltd. <info@kobros-tech.com>'
    ],
    'maintainer': 'Mohamed Moustafa Alkobrosli',
    'website':'http://odoo.kobros-tech.com',
    'license': 'GPL-3 or any later version',
    'summary': "Custom module for frontend & backend shop website, and backend system.",
    'sequence': 1,

    'description':"""
    This module enables us to store the chosen submitted logos by customers in a stand-alone model.\n
    In addition to that, the administrator can upload the collection of logo positions on the website.
    """,

    'images': ['static/description/banner.png'],
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
        'views/template2.xml',
        'views/order_logos.xml',
    ],
    'assets': {
        'web.assets_frontend':[            
            'logo_print/static/src/js/validate.js',
            # 'logo_print/static/**/*',
            'logo_print/static/src/css/logo_dialog.css',
        ],  
    }
}