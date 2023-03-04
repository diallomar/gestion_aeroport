import random
import string

from odoo import models, fields, api


class Equipage(models.Model):
    _name = 'aeroport.equipage'
    num_social_secur = fields.Char(string='Securite Sociale', readonly=True)
    firstname = fields.Char(string='Prenom', required=True)
    lastname = fields.Char(string='Nom', required=True)
    address = fields.Char(string='Adresse')
    email = fields.Char(string='Email')
    salary = fields.Float(string='Salaire')
    civility = fields.Selection([
        ('Monsieur', 'Mr'),
        ('Madame', 'Mme')],
        String='civilite')
    language = fields.Selection([
        ('Français', 'Français'),
        ('Englais', 'Englais'),
        ('Espagnol', 'Espagnol'),
        ('Wolof', 'Wolof'),
        ('Pulaar', 'Pulaar')],
        string='Langue')
    fonction = fields.Selection([
        ('Hotesse', 'Hotesse'),
        ('Stewart', 'Stewart')],
        string='Fonction')
    depart_ids = fields.One2many(
        'aeroport.depart', 'equipage_id', string='Membre Equipage 1')
    depart1_ids = fields.One2many(
        'aeroport.depart', 'equipage1_id', string='Membre Equipage 2')

    def name_get(self):
        res = []
        for membre in self:
            name = membre.firstname+' '+membre.lastname
            res.append((membre.id, name))
        return res

    @api.model
    def create(self, vals):
        letters = string.ascii_uppercase + string.digits
        mod1 = 'NUSS'
        rand1 = ''.join(random.choices(letters, k=3))
        vals['num_social_secur'] = mod1+rand1
        return super(Equipage, self).create(vals)
