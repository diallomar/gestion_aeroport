from odoo import models, fields, api


class Reservation(models.Model):
    _name = 'aeroport.reservation'

    date_reservation = fields.Date(string='Date de reservation')
    date_emission = fields.Date(string='Date emission')
    numberOfPlace = fields.Char(string='Numéro de la place')
    ticket_issued = fields.Boolean(string='Billets émis')
    depart_id = fields.Many2one('aeroport.depart')
    num_passager = fields.Many2one('aeroport.passager')

    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('waiting', 'En attente d\'émission de billet'),
        ('issued', 'Billet émis'),
        ('cancel', 'Annulé'),
    ], string='Statut', default='draft')


    def name_get(self):
        res = []
        for reservation in self:
            name = 'Passager N° ' + reservation.num_passager.num_passager
            res.append((reservation.id, name))
        return res


    def issue_ticket(self):
        for reservation in self:
            reservation.write({'state': 'issued', 'ticket_issued': True})

    @api.model
    def _issue_ticket(self, vals):
        return self.env['aeroport.reservation'].browse(vals.get('reservation_id')).issue_ticket()

    _transitions = [
        ('waiting', 'issued', 'Émettre billet', '_issue_ticket'),
    ]
