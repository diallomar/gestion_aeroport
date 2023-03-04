import random
import string
from odoo import models, fields, api


class Pilote(models.Model):
    _name = 'aeroport.pilote'
    num_social_secur = fields.Char(
        string='Numéro Sécurite Sociale')
    firstname = fields.Char(string='Prenom')
    lastname = fields.Char(string='Nom', required=True)
    address = fields.Char(string='Adresse')
    email = fields.Char(string='Email')
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
    licence = fields.Char(string='Licence', readonly=True,
                          )

    depart_ids = fields.One2many(
        'aeroport.depart', 'pilote_id', string='Pilote')
    depart1_ids = fields.One2many(
        'aeroport.depart', 'copilote_id', string='Copilote')

    fullname = fields.Char(string='Nom Complet',
                           compute='_compute_full_name', store=True)

    def name_get(self):
        res = []
        for pilote in self:
            name = pilote.lastname+' '+pilote.licence
            res.append((pilote.id, name))
        return res

    @api.model
    def create(self, vals):
        mod = 'PLT'
        letters = string.ascii_uppercase + string.digits
        rand = ''.join(random.choices(letters, k=7))
        vals['licence'] = mod+rand
        mod1 = 'NUSS'
        rand1 = ''.join(random.choices(letters, k=3))
        vals['num_social_secur'] = mod1+rand1
        return super(Pilote, self).create(vals)
