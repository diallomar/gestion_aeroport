from odoo import models, fields


class Equipage(models.Model):
    _name = 'aeroport.equipage'
    num_social_secur = fields.Char(string='Securite Sociale')
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
        string='Langue',
        multi=True)
    fonction = fields.Selection([
        ('Hotesse', 'Hotesse'),
        ('Stewart', 'Stewart')],
        string='Fonction')
    depart_ids = fields.One2many(
        'aeroport.depart', 'equipage_id', string='Membre Equipage 1')
    depart1_ids = fields.One2many(
        'aeroport.depart', 'equipage1_id', string='Membre Equipage 2')
