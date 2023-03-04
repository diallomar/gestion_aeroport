from odoo import models, fields


class Passager(models.Model):
    _name = 'aeroport.passager'

    num_passager = fields.Char(string='Numéro passager')
    firstName = fields.Char(string='Prénom')
    lastName = fields.Char(string='Nom')
    phoneNumber = fields.Char(string='Numéro de téléphone')
    address = fields.Char(string='Adresse')
    function = fields.Char(string='Profession')
    email = fields.Char(string='Email')
    reservation_ids = fields.One2many(
        'aeroport.reservation', 'num_passager', string='Numéro du passager')

    def action_cours_send(self):
        template = self.env.ref('gestion_aeroport.email_template_aeroport')
        self.env['mail.template'].browse(template.id).sudo().send_mail(self.id, force_send=True)
        self.env['mail.mail'].sudo().process_email_queue()
