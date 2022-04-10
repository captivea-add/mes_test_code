# -*- coding: utf-8 -*-
{
'name': 'resacolo',
'summary': "Gestion d’une agence de réservation de séjours",
'description': """
Gestion d’une agence de réservation de séjours
==============
Description relative à la gestion d’une agence de réservation de séjours .
""",
  'author': "Toutchy kipik",
  'website': "",
  'category': 'event',
  'version': '0.1',
   'depends': ['base'
               ],
   # always loaded
    'data': [
        'static/css/style.css'
        # 'security/ir.model.access.csv',
        'views/participants_views.xml',
        'views/creation_sejour_views.xml',
        'views/tuteurs_views.xml',
        'views/templates.xml',
        #'views/subject_views.xml',
    ],
    
        "assets": {
        "web.assets_backend": ["resacolo/static/src/css/style.css"],
    },
   'demo': ['demo.xml'],
}
