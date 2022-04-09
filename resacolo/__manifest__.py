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
  'category': 'Event',
  'version': '0.1',
   'depends': ['base'
               ],
   # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/participants_views.xml',
        'views/creation_sejour_views.xml',
        'views/tuteurs_views.xml',
        #'views/student_views.xml',
        #'views/subject_views.xml',
    ],
   'demo': ['demo.xml'],
}
