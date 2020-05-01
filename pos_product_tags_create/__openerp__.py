# -*- coding: utf-8 -*-
# Copyright (C) 2018 Artem Shurshilov <shurshilov.a@yandex.ru>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'POS product tags create from pos',
    'summary': """Adds functional create tags in POS""",
    'description': """
                    This extension for the POS module allows you to search
                     for products by category, see videos and screenshots 
                     for a better understanding
                   """,
    'author': 'Shurshilov Artem',
#    "website": "https://vk.com/id20132180",
    'website': "http://www.eurodoo.com",
    
    # Categories can be used to filter modules in modules listing
    'category': "Tools",
	'version': '1.0',
    # any module necessary for this one to work correctly
    'depends': ['web','point_of_sale','product_tags_fork'],    
    "license": "AGPL-3",
    'price': 15,
    'currency': 'EUR',
    # always loaded
    'images':[
            'static/description/tags_Create.png',
	        'static/description/product.png',
	        'static/description/search_new.png',
    ],
    'data': [ 'views/pos_product_tags_search.xml', ],   
    'qweb': ['static/src/xml/pos.xml'],
    #'qweb': [ 'static/src/xml/image.xml', ],
    'installable': True,
    'application': False,
    # If it's True, the modules will be auto-installed when all dependencies
    # are installed
    'auto_install': False,
}