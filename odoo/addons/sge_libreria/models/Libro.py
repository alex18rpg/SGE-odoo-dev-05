# -*- coding: utf-8 -*-

from odoo import models, fields

class Libro(models.Model):
    _name = 'sge_libreria.libro'
    _description = 'Libro'

    nombre = fields.Char('Titulo', required=True, help='Introduce el titulo del libro')
    precio = fields.Float('Precio', required=True,help='Introduce el precio del libro')
    ejemplares = fields.Integer('Ejemplares', required=True, help='Introduce el numero de ejemplares')
    fecha_compra = fields.Date('Fecha de Compra', required=True, help='Introduzca la fecha de compra')
    segunda_mano = fields.Boolean('Segunda mano', required=True, help='Es de segunda mano')
    estado = fields.Selection([
        ('N', 'Nuevo'),
        ('B', 'Bueno'),
        ('R', 'Regular'),
        ('M', 'Malo')
    ], string='Estado', default='N')