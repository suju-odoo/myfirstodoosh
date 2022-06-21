from xmlrpc import client
import certifi
import ssl

context=ssl.create_default_context(cafile=certifi.where())

url = 'https://sunhyeok1-stage1-5125190.dev.odoo.com' 
db = 'sunhyeok1-stage1-5125190'
username = 'admin'
password = 'a9d8ed2a2f8be084b6a13db460e969b296ef804c'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url), context=context)
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

models = client.ServerProxy('{}/xmlrpc/2/object'.format(url), context=context)

model_access = models.execute_kw(db,uid,password,'academy.session','check_access_rights',
                                 ['write'],{'raise_exception' : False})
print(model_access)

courses = models.execute_kw(db, uid, password,
                            'academy.course',
                            'search_read',
                            [[['level','in',['intermediate','beginner']]]])
print(courses)

# search for record id.
course = models.execute_kw(db, uid, password,
                           'academy.course',
                           'search',
                           [[['name','=','ERP 101']]])
print(course)

# get certain attributes of the field
session_fields = models.execute_kw(db, uid, password, 
                                   'academy.session',
                                   'fields_get',
                                   [], {'attributes' : ['string','type','required']}
                                   )
print(session_fields)

new_session = models.execute(db, uid, password,
                             'academy.session', 'create', 
                             [
                                 {
                                     'course_id' : course[0],
                                     'state': 'open',
                                     'duration': 5,
                                     
                                 }
                             ])
print(new_session)