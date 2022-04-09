# -*- coding: utf-8 -*-
from tkinter import Widget
from typing import Sequence
from odoo import models, fields, api

class ResacoloSejour(models.Model):
    _name = 'resacolo.sejours'

    nom = fields.Char('Nom du séjour')
    description = fields.Text('Description du séjour')
    organisateur = fields.Many2one(comodel_name='res.partner')
    reference = fields.Integer('Référence séjour', Sequence=([1,1]))

    creation_date = fields.Date('Date de mise en ligne')
    date_depart_un = fields.Date('Date depart un')
    date_retour_un = fields.Date('Date retour un')
    date_depart_deux = fields.Date('Date depart deux')
    date_retour_deux = fields.Date('Date retour deux')
    date_depart_trois = fields.Date('Date depart trois')
    date_retour_trois = fields.Date('Date retour trois')

    prix_un = fields.Float(Widget='Monetary')
    prix_deux = fields.Float(Widget='Monetary')
    prix_trois = fields.Float(Widget='Monetary')
    prix_option_un = fields.Float(Widget='Monetary')
    prix_option_deux = fields.Float(Widget='Monetary')
    prix_option_trois = fields.Float(Widget='Monetary')

    nom_option_un = fields.Char('Nom option un')
    nom_option_deux = fields.Char('Nom option un')
    nom_option_trois = fields.Char('Nom option un')
    description_option_un = fields.Text('Description option un')
    description_option_deux = fields.Text('Description option un')
    description_option_trois = fields.Text('Description option un')

    place_max = fields.Integer('Nombre de place max')
    compteur_participants = fields.Integer('Nombre de place réservés')

#class ResacoloSejourDate(models.Model):
    #_name = 'resacolo.dates'

# class ResacoloSejourPrix(models.Moedl):
    #_name = 'resacolo.prix'

    

# class ResacoloSejourOption(models.Moedl):
    #_name = 'resacolo.options'


# class ResacoloSejourCompteur(models.Model):
   # _name = 'resacolo.compteur'


    