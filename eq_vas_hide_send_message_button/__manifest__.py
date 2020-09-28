# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright 2019 EquickERP
#
##############################################################################
{
    'name': "Hide Send Message Button",
    'category': 'Tools',
    'version': '13.0.1.0',
    'author': 'Equick ERP',
    'description': """
        Hide Send Message Button
        * Ref No: S00054
    """,
    'summary': """Hide Send Message Button""",
    'depends': ['base', 'web', 'mail'],
    'license': 'OPL-1',
    'website': "",
    'data': [
        'views/model_view.xml',
    ],
    'qweb': [
        'static/src/xml/chatter.xml',
    ],
    'images': ['static/description/main_screenshot.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: