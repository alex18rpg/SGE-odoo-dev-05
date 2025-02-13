# -*- coding: utf-8 -*-
from odoo import models, fields

class Equipo(models.Model):
    _name = 'agc_gimnasio.equipo'
    _description = 'Equipo'

    name = fields.Char('Nombre')
    apodo = fields.Char('Apodo')
    numero_miembros = fields.Binary('Nº de miembros')