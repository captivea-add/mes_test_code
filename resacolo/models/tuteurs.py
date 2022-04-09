# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResacoloTuteurs(models.Model):
    _name = 'resacolo.tuteurs'

    f_name = fields.Char('Fist name')
    l_name = fields.Char('Last name')
    
    identity_card = fields.Char('Phone')
    birthday = fields.Date('Birthday')
    choix_date = fields.Datetime(' Choix date')
    email = fields.Char('Email')
    phone = fields.Char('Phone')

    zip = fields.Char('zip')
    street : fields.Text('Street')
    city = fields.Char('City')

# class ResacoloAdress(models.Model):
    #_name = 'resacolo.adresse'
    