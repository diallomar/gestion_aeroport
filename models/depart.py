from datetime import datetime
from odoo import models, fields, api

from odoo.exceptions import ValidationError


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

    def name_get(self):
        res = []
        for depart in self:
            name = 'Départ du Vol N° ' + depart.vol_id.number
            res.append((depart.id, name))
        return res

    @api.model
    def create(self, vals):
        depart = super(Depart, self).create(vals)

        if depart.pilote_id:
            template = self.env.ref('aeroport.message_depart')
            self.env['mail.template'].browse(
                template.id).sudo().send_mail(depart.id, force_send=True)
            self.env['mail.mail'].sudo().process_email_queue()

        return depart

    @api.constrains('pilote_id', 'copilote_id')
    def _check_different_pilots(self):
        for record in self:
            if record.pilote_id and record.copilote_id and record.pilote_id == record.copilote_id:
                raise ValidationError(
                    "Le pilote et le copilote doivent être différents.")

    @api.constrains('equipage1_id', 'equipage_id')
    def _check_different_pilots(self):
        for record in self:
            if record.equipage_id and record.equipage1_id and record.equipage_id == record.equipage1_id:
                raise ValidationError(
                    "Les deux membres d'equipage doivent être différent.")
