from odoo import models, fields


class Avion(models.Model):
    _name = 'aeroport.avion'

    vol_ids = fields.One2many('aeroport.vol','avion_id',string='Avion')
    immatriculation = fields.Char(string='Immatriculation')
    numberOfPlace = fields.Integer(string='Nombre de place')
    mark = fields.Char(string='Marque')
    model = fields.Char(string='Modèle')
