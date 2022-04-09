# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResacoloParticipants(models.Model):
    _name = 'resacolo.participants'

    # Nom
    name_participant = fields.Char('Fist name')
    
    # Email
    email = fields.Char()
    
    # Phone
    phone = fields.Char()
    
    # Age
    birthday = fields.Date('Birthday')
    
    # Genre
    sex = fields.Selection([
                            ('male', 'Male'), 
                            ('female', 'Female')
                            ])
    
    # Adresse (si differente)
    address = fields.Boolean('Address')
    zip = fields.Char('C P')
    street = fields.Char('Street')
    city = fields.Char('City')
    
    # Date d'inscription
    registration_date = fields.Datetime('Registration Date')
