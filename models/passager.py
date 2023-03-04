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

    def name_get(self):
        res = []
        for passager in self:
            name = 'Passager N° ' + passager.num_passager
            res.append((passager.id, name))
        return res

    @api.model
    def create(self, vals):
        letters = string.ascii_uppercase + string.digits
        mod1 = 'PASS'
        rand1 = ''.join(random.choices(letters, k=10))
        vals['num_passager'] = mod1+rand1
        return super(Passager, self).create(vals)

    def action_cours_send(self):
        template = self.env.ref('gestion_aeroport.email_template_aeroport')
        self.env['mail.template'].browse(
            template.id).sudo().send_mail(self.id, force_send=True)
        self.env['mail.mail'].sudo().process_email_queue()
