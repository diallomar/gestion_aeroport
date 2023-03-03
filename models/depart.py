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

    validity = fields.Boolean(string='validite')

    def name_get(self):
        res = []
        for depart in self:
            name = 'Départ du Vol N° ' + depart.vol_id.number
            res.append((depart.id, name))
        return res

    @api.onchange('vol_id')
    def get_validity(self):
        val = self.env['aeroport.vol'].search([])
        self.validity = val.validity

    # @api.model
    # def create(self, vals):
    #     # validit = self.env['aeroport.vol'].search([])
    #     if self.validity == False:
    #         return 'impossible de programmer un depart pour un vol desactive'
    #     return super(Depart, self).create(vals)
