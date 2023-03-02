from odoo import models, fields


class Depart(models.Model):
    _name = 'aeroport.depart'
    date = fields.Datetime(string="Date Depart")
    vol_id = fields.Many2one('aeroport.vol')
    pilote_id = fields.Many2one('aeroport.pilote')
    copilote_id = fields.Many2one('aeroport.pilote')
    equipage_id = fields.Many2one('aeroport.equipage')
    equipage1_id = fields.Many2one('aeroport.equipage')
    reservation_ids = fields.One2many(
        'aeroport.reservation', 'depart_id', 'Décolage')
