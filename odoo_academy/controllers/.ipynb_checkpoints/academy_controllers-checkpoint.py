# -*- coding : utf-8 -*-
from odoo import http

class Academy(http.Controller):
    @http.route('/academy/', auth='public', website=True)
    def index(self, **kw):
        return "Hello, World"
    
    @http.route('/academy/courses', auth='public', website=True)
    def courses(self, **kw):
        courses = http.request.env['academy.course'].search([])
        return http.request.render('academy.course_website', {
            'courses': courses
        })