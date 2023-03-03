import random
import string
from odoo import models, fields, api


class Vol(models.Model):
    _name = 'aeroport.vol'
    number = fields.Char(string='Numéro Vol', readonly=True)
    type_courier = fields.Selection(
        [('court', 'COURT'), ('moyen', 'MOYEN'), ('long', 'LONG')], string='Type de Courier')
    start_validity = fields.Date(string='Début de Validité')
    end_validity = fields.Date(string='Fin de Validité')
    validity = fields.Boolean(string='Validité')
    ligne_id = fields.Many2one('aeroport.ligne')
    avion_id = fields.Many2one('aeroport.avion')
    depart_ids = fields.One2many('aeroport.depart', 'vol_id', string="Vol")

    def name_get(self):
        res = []
        for vol in self:
            name = 'Vol N° ' + vol.number
            res.append((vol.id, name))
        return res

    @api.model
    def create(self, vals):
        letters = string.ascii_uppercase + string.digits
        rand1 = ''.join(random.choices(letters, k=5))
        vals['number'] = rand1
        return super(Vol, self).create(vals)
    