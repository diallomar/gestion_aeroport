from odoo import models, fields


class Vol(models.Model):
    _name = 'aeroport.vol'

    number = fields.Char(string='Numéro Vol')
    type_courier = fields.Selection(
        [('court', 'COURT'), ('moyen', 'MOYEN'), ('long', 'LONG')], string='Type de Courier')
    start_validity = fields.Date(string='Début de Validité')
    end_validity = fields.Date(string='Fin de Validité')
    validity = fields.Boolean(string='Validité')
    ligne_id = fields.Many2one('aeroport.ligne')
    avion_id = fields.Many2one('aeroport.avion')
    depart_ids = fields.One2many('aeroport.depart', 'vol_id', string="vol")
