<<<<<<< HEAD
import random
import string

from odoo import models, fields, api
=======
from odoo import models, fields,api
import random
import string
>>>>>>> 1dc228a2768c9599e410882f2e26861880242871


class Equipage(models.Model):
    _name = 'aeroport.equipage'
<<<<<<< HEAD
    num_social_secur = fields.Char(string='Securite Sociale')
    firstname = fields.Char(string='Prenom', required=True)
    lastname = fields.Char(string='Nom', required=True)
=======
    num_social_secur = fields.Char(string='Numero Securite Sociale')
    firstname = fields.Char(string='Prenom')
    lastname = fields.Char(string='Nom')
>>>>>>> 1dc228a2768c9599e410882f2e26861880242871
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

<<<<<<< HEAD

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
=======
    @api.onchange('num_social_secur')
    def get_num_sec_(self):
        letters = string.ascii_uppercase + string.digits
        self.num_social_secur = ''.join(random.choices(letters, k=5))
>>>>>>> 1dc228a2768c9599e410882f2e26861880242871
