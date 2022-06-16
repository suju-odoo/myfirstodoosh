# -*- coding : utf-8 -*_
{
    'name': 'Odoo Academy',
    'summary' : """Academy app to manage Training """,
    'description' : """
        Academy Module to manage training:
        - courses
        - sessions
        - attendees
    """,
    
    'author' : 'Odoo',
    
    'website': 'https://www.odoo.com',
    
    'category' : 'Training',
    
    'version' : '0.2',
    
    'depends' : ['sale'], 
    # ['base']
    'data' : [
        'data/academy_demo.xml',
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/sale_views_inherit.xml'
        
    ],
    
    'demo' : [
#         'demo/academy_demo.xml'
    ]
}