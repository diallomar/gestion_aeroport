from odoo import models, fields


class Passager(models.Model):
    _name = 'aeroport.passager'

    num_passager = fields.Char(string='Numéro passager')
    firstName = fields.Char(string='Prénom')
    lastName = fields.Char(string='Nom')
    phoneNumber = fields.Char(string='Numéro de téléphone')
    address = fields.Char(string='Adresse')
    function = fields.Char(string='Profession')
    reservation_ids = fields.One2many(
        'aeroport.reservation', 'num_passager', string='Numéro du passager')
