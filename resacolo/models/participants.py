# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResacoloParticipants(models.Model):
    _name = 'resacolo.participants'

    f_name = fields.Char('Fist name')
    l_name = fields.Char('Last name')
    
    sexe = fields.Selection([
                            ('male','Male'), 
                            ('female','Female')]
                            )    
    phone = fields.Char('Identity card')
    birthday = fields.Date('Birthday')
    registration_date = fields.Datetime('Registration Date')
    email = fields.Char('Email')
    phone = fields.Char()

    adresse_diff = fields.Boolean('Adresse différente ?')
    zip = fields.Char('zip') # attrs="invisible:['adresse_diff' '=', 'True' 
    street : fields.Text('Street')
    city = fields.Char('City')

# class ResacoloAdress(models.Model):
    # _name = 'resacolo.adresse'

    
