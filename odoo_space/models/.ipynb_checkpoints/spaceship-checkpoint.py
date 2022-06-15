# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Spaceship(models.Model):
    _name = 'space.spaceship'
    _description = 'Spaceship'
    
    name = fields.Char(string='Ship Name', required = True)
    ship_dimensions = fields.Float()
    fuel_type = fields.Selection(string = "Fuel Type",
                                 selection=[('gasoline','Gasoline'),
                                            ('diesel','Diesel')],
                                 copy=False
                                 )
    ship_type = fields.Selection(string = "Ship Type",
                                 selection=[('flyby','Flyby'),
                                            ('orbiter','Orbiter')],
                                 copy=False
                                 )
    number_of_passengers = fields.Integer()
    active = fields.Boolean(string="Active", default=True)
