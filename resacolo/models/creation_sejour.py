# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResacoloTCreationSejour(models.Model):
    _name = 'resacolo.creation_sejour'

# Les caractéristiques des véhicules
    nom_sejour = fields.Char('Nom du séjour', required=True)

    # Organisateur
    organisateur =  fields.Many2one(comodel_name='res.partner')

    # Nombre de place + compteur
    nb_place_max = fields.Integer("Nombre de place maximum", required=True)
    nb_place_min = fields.Integer("Nombre de place minimum", required=True)
    compteur_place = fields.Integer("Places réservés", required=True)
    tranche_age_max = fields.Integer()
    tranche_age_min = fields.Integer()

    # Choix des dates
    date_debut_first = fields.Date("Date choix un")
    date_debut_scd = fields.Date("Date choix deux")
    date_debut_thr = fields.Date("Date choix trois")
    date_achat = fields.Date("Date d Achat")
    periode = fields.Selection([
        ('ete', 'Ete'),
        ('hiver', 'Hiver')
        ])
    
    # Ville depart/arrivée
    ville_depart = fields.Char("Ville de depart")
    ville_arrivee = fields.Char("Ville de arrivée")
    
    # Options details
    nom_option = fields.Char("Nom de l'option")
    description_option = fields.Char("Nom de l'option")
    prix_option_un = fields.Float()
    prix_option_deux = fields.Float()
    prix_option_trois = fields.Float()

    # Réference du séjour
    ref_sejour = fields.Integer(String="Référence du séjour")
    
    # Description du séjour
    description_sejour = fields.Text(String="Description du séjour")
    
    # Prix du séjour
    prix_sejour_un = fields.Float()
    prix_sejour_deux = fields.Float()
    prix_sejour_trois = fields.Float()