import random
import string
from odoo import models, fields, api


class Pilote(models.Model):
    _name = 'aeroport.pilote'
    _rec_name = 'fullname'
    num_social_secur = fields.Char(
        string='Numéro Sécurite Sociale', readonly=True)
    firstname = fields.Char(string='Prenom')
    lastname = fields.Char(string='Nom')
    address = fields.Char(string='Adresse')
    salary = fields.Float(string='Salaire')
    civility = fields.Selection([
        ('Monsieur', 'Mr'),
        ('Madame', 'Mme')],
        string='civilite',
        required=True)
    language = fields.Selection([
        ('Français', 'Français'),
        ('Englais', 'Englais'),
        ('Espagnol', 'Espagnol'),
        ('Wolof', 'Wolof'),
        ('Pulaar', 'Pulaar')],
        string='Langue',
        multiple=True)
    licence = fields.Char(string='Licence', readonly=True)

    depart_ids = fields.One2many(
        'aeroport.depart', 'pilote_id', string='Pilote')
    depart1_ids = fields.One2many(
        'aeroport.depart', 'copilote_id', string='Copilote')

    fullname = fields.Char(string='Nom Complet',
                           compute='_compute_full_name', store=True)

    @api.depends('firstname', 'lastname')
    def _compute_full_name(self):
        for record in self:
            record.fullname = record.firstname + ' ' + record.lastname

    def name_get(self):
        res = []
        for pilote in self:
            name = pilote.licence
            res.append((pilote.id, name))
        return res

    @api.onchange('licence')
    def get_licence_(self):
        letters = string.ascii_uppercase + string.digits
        self.licence = ''.join(random.choices(letters, k=10))

    @api.onchange('num_social_secur')
    def get_num_sec_(self):
        letters = string.ascii_uppercase + string.digits
        self.num_social_secur = ''.join(random.choices(letters, k=5))
