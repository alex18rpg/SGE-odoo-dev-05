# -*- coding: utf-8 -*-
from odoo import models, fields

class Subdito(models.Model):
    _name = 'agc_gimnasio.subdito'
    _description = 'Subdito'

    name = fields.Char('Nombre')
    nivel = fields.Integer('Nivel')
    numero_objetos = fields.Integer('Nº de objetos')
    legendario = fields.Boolean('Legendario')