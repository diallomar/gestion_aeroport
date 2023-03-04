from odoo import models, fields,api
import random
import string


class Equipage(models.Model):
    _name = 'aeroport.equipage'
    num_social_secur = fields.Char(string='Numero Securite Sociale')
    firstname = fields.Char(string='Prenom')
    lastname = fields.Char(string='Nom')
    address = fields.Char(string='Adresse')
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

    @api.onchange('num_social_secur')
    def get_num_sec_(self):
        letters = string.ascii_uppercase + string.digits
        self.num_social_secur = ''.join(random.choices(letters, k=5))
