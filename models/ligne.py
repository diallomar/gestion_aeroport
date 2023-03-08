from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Ligne(models.Model):
    _name = 'aeroport.ligne'

    aeroport_depart = fields.Many2one('aeroport.aeroport')
    aeroport_arrivee = fields.Many2one('aeroport.aeroport')
    vol_ids = fields.One2many('aeroport.vol', 'ligne_id', string='Trajet')
    active = fields.Boolean(string='Active')

    def name_get(self):
        res = []
        for ligne in self:
            name = ligne.aeroport_depart.name + ' => ' + ligne.aeroport_arrivee.name
            res.append((ligne.id, name))
        return res

    @api.constrains('aeroport_depart', 'aeroport_arrivee')
    def _check_different_pilots(self):
        for record in self:
            if record.aeroport_arrivee and record.aeroport_depart and record.aeroport_arrivee == record.aeroport_depart:
                raise ValidationError(
                    "L'aeroport d'arrivée doit être de celle du départ.")
