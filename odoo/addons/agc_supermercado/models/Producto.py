# -*- coding: utf-8 -*-

from odoo import models, fields

class Producto(models.Model):
    _name = 'agc_supermercado.Producto'
    _description = 'Producto'

    name = fields.Char('Nombre', required=True, help='Introduce el nombre del producto')
    
    
    
    