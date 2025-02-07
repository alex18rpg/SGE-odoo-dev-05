# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Categoria(models.Model):
    _name = 'agc_supermercado.categoria'
    _description = 'Categoria'
    
    name = fields.Char('Nombre', required=True, help='Introduzca nombre de categoria')
    description = fields.Char('Description')  