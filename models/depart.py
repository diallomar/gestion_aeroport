from datetime import datetime
from odoo import models, fields, api


class Depart(models.Model):
    _name = 'aeroport.depart'
    date = fields.Datetime(string="Date Depart")
    vol_id = fields.Many2one('aeroport.vol', required=True)
    pilote_id = fields.Many2one('aeroport.pilote')
    copilote_id = fields.Many2one('aeroport.pilote')
    equipage_id = fields.Many2one('aeroport.equipage')
    equipage1_id = fields.Many2one('aeroport.equipage')
    reservation_ids = fields.One2many(
        'aeroport.reservation', 'depart_id', 'Décolage')

    # message_template_id = fields.Many2one(
    #     'mail.template', string='Message Template')

    # validity = fields.Boolean(string='validite')

    def name_get(self):
        res = []
        for depart in self:
            name = 'Départ du Vol N° ' + depart.vol_id.number
            res.append((depart.id, name))
        return res

    # @api.onchange('vol_id')
    # def get_validity(self):
    #     val = self.env['aeroport.vol'].search([])
    #     self.validity = val.validity

    @api.model
    def create(self, vals):
        depart = super(Depart, self).create(vals)

        if depart.pilote_id:
            template = self.env.ref('aeroport.message_depart')
            self.env['mail.template'].browse(
                template.id).sudo().send_mail(depart.id, force_send=True)
            self.env['mail.mail'].sudo().process_email_queue()

            # template.send_mail(depart.id, force_send=True, email_values={
            #     'email_from': 'consultationpatient@gmail.com',
            #     'email_to': depart.pilote_id.email,
            #     'subject': 'Nouveau départ',
            #     'body_html': 'Bonjour {},<br/>Un nouveau départ a été créé pour le vol {} du {} <br/>.'.format(depart.pilote_id.name, depart.vol_id.number, depart.date),
            # })
        return depart
