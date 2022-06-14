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
    
    'depends' : ['base'],
    
    'data' : [
        'data/academy_demo.xml'
    ],
    
    'demo' : [
#         'demo/academy_demo.xml'
    ]
}