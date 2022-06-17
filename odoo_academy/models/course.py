# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class Course(models.Model):
    
    _name = 'academy.course'
    _description = 'Course Info'
    

    name = fields.Char(string='Title', required = True)
    description = fields.Text(string="Description")
    
    level = fields.Selection(string = "Level", 
                            selection=[('beginner', 'Beginner'), 
                                       ('intermediate','Intermediate'),
                                       ('advanced', 'Advanced')],
                             copy=False
                        
                            )
    
    active = fields.Boolean(string="Active", default=True)
    
    base_price = fields.Float(string="Base Price", default=0.00)
    
    additional_fee = fields.Float(string="Additional Fee", default=10.00)
    
    total_price = fields.Float(string="Total Price", compute = '_onchange_total_price', store=True)

    session_ids = fields.One2many(comodel_name="academy.session",
    inverse_name="course_id",
    string="Sessions")
    
#   this method will be called whenever 'base_price' and 'additional_fee' are changed.
# onchange vs depends => use depends everytime.

    @api.depends('base_price','additional_fee')
    def _onchange_total_price(self):
        for record in self:
            if record.base_price < 0.00:
                raise UserError('Base price cannot be set lower than 0')
            record.total_price = record.base_price + record.additional_fee
        
    # done at run time 
    @api.constrains('additional_fee')
    def _check_additional_fee(self):
        for record in self:
            if record.additional_fee < 10.00:
                raise ValidationError('Additional Fees cannot be less than 10: %s' % record.additional_fee)
                
                