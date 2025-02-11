# -*- coding: utf-8 -*-
from odoo import models, fields

class Lider(models.Model):
    _name = 'agc_gimnasio.lider'
    _description = 'Lider'

    name = fields.Char('Nombre', required=True)
    tipo = fields.Selection([
        ('1', 'Acero'),
        ('2', 'Agua'),
        ('3', 'Bicho'),
        ('4', 'Dragon'),
        ('5', 'Eléctrico'),
        ('6', 'Fantasma'),
        ('7', 'Fuego'),
        ('8', 'Hada'),
        ('9', 'Hielo'),
        ('10', 'Lucha'),
        ('11', 'Normal'),
        ('12', 'Planta'),
        ('13', 'Psíquico'),
        ('14', 'Roca'),
        ('15', 'Siniestro'),
        ('16', 'Tierra'),
        ('17', 'Veneno'),
        ('18', 'Volador'),
    ], string='Tipo')
    nivel = fields.Integer('Nivel')
    numero_subditos = fields.Integer('Nº de Subditos')
    numero_objetos = fields.Integer('Nº de Objetos')
    legendario = fields.Boolean('Legendario')