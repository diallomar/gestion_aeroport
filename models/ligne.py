from odoo import models, fields


class Ligne(models.Model):
    _name = 'aeroport.ligne'

    aeroport_depart = fields.Many2one('aeroport.aeroport')
    aeroport_arrivee = fields.Many2one('aeroport.aeroport')
    vol_ids = fields.One2many('aeroport.vol', 'ligne_id', string='Trajet')
    active = fields.Boolean(string='Active')
