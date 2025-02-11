# -*- coding: utf-8 -*-
from odoo import models, fields

class Subdito(models.Model):
    _name = 'agc_gimnasio.subdito'
    _description = 'Subdito'

    name = fields.Char('Nombre')