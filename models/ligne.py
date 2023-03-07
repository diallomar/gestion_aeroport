from odoo import models, fields


class Ligne(models.Model):
    _name = 'aeroport.ligne'

    aeroport_depart = fields.Many2one('aeroport.aeroport')
    aeroport_arrivee = fields.Many2one('aeroport.aeroport')
    vol_ids = fields.One2many('aeroport.vol', 'ligne_id', string='Trajet')
    active = fields.Boolean(string='Active')



    def name_get(self):
        res = []
        for ligne in self:
            name = ligne.aeroport_depart.name + '=>' + ligne.aeroport_arrivee.name
            res.append((ligne.id, name))
        return res