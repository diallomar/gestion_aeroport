from odoo import models, fields


class Aeroport(models.Model):
    _name = 'aeroport.aeroport'

    name = fields.Char(string='Nom')
    town = fields.Char(string='Ville')
    country = fields.Char(string='Pays')
    language = fields.Selection(
        [('arabe', 'ARABE'), ('français', 'FRANCAIS'), ('anglais', 'ANGLAIS'), ('wolof', 'WOLOF')],
        string='Langues courantes')
    ligne_ids = fields.One2many('aeroport.ligne', 'aeroport_depart', string='Aéroport de départ')
    ligne1_ids = fields.One2many('aeroport.ligne', 'aeroport_arrivee', string='Aéroport d\'arrivée')
