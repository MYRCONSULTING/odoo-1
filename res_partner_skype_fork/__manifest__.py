# -*- coding: utf-8 -*-
{
    "name": "Skype field in partner form odoo 12 and 13",
    "version": "12.0.0.0",
    "author": "Shurshilov Artem",
    'license': 'LGPL-3',
    "category": "Tools",
    'website': "http://www.eurodoo.com",
#    "website": "https://vk.com/id20132180",
    #'price': 9.00,
    #'currency': 'EUR',
    "depends": ['web'],
    "images": [
	    'static/description/module.png',
	    'static/description/field.png'
	    'static/description/skype.png'
    ],
    "data": [
        'views.xml',
        'data.xml',
    ],
    "qweb": [
        'static/src/xml/base.xml',
    ],
    'installable': True,
}
