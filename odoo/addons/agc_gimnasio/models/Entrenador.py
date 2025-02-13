# -*- coding: utf-8 -*-
from odoo import models, fields

class Enrtenador(models.Model):
    _name = 'agc_gimnasio.entrenador'
    _description = 'Entrenador'

    name = fields.Char('Nombre')
    numero_objetos = fields.Integer('Nº de objetos')
    legendario = fields.Boolean('Legendario')