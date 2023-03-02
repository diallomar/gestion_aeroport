from odoo import models, fields


class Reservation(models.Model):
    _name = 'aeroport.reservation'

    date_reservation = fields.Date(string='Date de reservation')
    date_emission = fields.Date(string='Date emission')
    numberOfPlace = fields.Char(string='Numéro de la place')
    ticket_issued = fields.Boolean(string='Billets émis')
    depart_id = fields.Many2one('aeroport.depart')
    num_passager = fields.Many2one('aeroport.passager')