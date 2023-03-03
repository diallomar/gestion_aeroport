from odoo import models, fields, api


class Avion(models.Model):
    _name = 'aeroport.avion'
   
    vol_ids = fields.One2many('aeroport.vol', 'avion_id', string='Avion')
    immatriculation = fields.Char(string='Immatriculation', required=True)
    numberOfPlace = fields.Integer(string='Nombre de place', required=True)
    mark = fields.Char(string='Marque', required=True)
    model = fields.Char(string='Modèle', required=True)

    

    def name_get(self):
        res = []
        for avion in self:
            name = avion.mark + ' ' + avion.model
            res.append((avion.id, name))
        return res
