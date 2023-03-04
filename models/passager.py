import random
import string
from odoo import models, fields, api


class Passager(models.Model):
    _name = 'aeroport.passager'
    num_passager = fields.Char(string='Numéro passager', readonly=True)
    firstName = fields.Char(string='Prénom')
    lastName = fields.Char(string='Nom')
    phoneNumber = fields.Char(string='Numéro de téléphone')
    address = fields.Char(string='Adresse')
    email = fields.Char(string='Email')
    function = fields.Char(string='Profession')
    email = fields.Char(string='Email')
    reservation_ids = fields.One2many(
        'aeroport.reservation', 'num_passager', string='Numéro du passager')
