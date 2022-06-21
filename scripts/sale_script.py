from xmlrpc import client
import certifi
import ssl
from datetime import date
context=ssl.create_default_context(cafile=certifi.where())

url = 'https://sunhyeok1-stage1-5125190.dev.odoo.com' 
db = 'sunhyeok1-stage1-5125190'
username = 'admin'
password = 'a9d8ed2a2f8be084b6a13db460e969b296ef804c'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url), context=context)
uid = common.authenticate(db, username, password, {})
print(uid)

models = client.ServerProxy('{}/xmlrpc/2/object'.format(url), context=context)

model_access = models.execute_kw(db,uid,password,'sale.order','check_access_rights',
                                 ['write'],{'raise_exception' : False})
print(model_access)

print("HERE")

today = date.today()
d1 = today.strftime("%Y-%m-%d")

expired_quotes_ids = models.execute_kw(db, uid, password,
                                 'sale.order', 'search',
                                 [[['validity_date','<=',d1]]])
models.execute_kw(db, uid, password, 'sale.order', 'unlink', [expired_quotes_ids])
print(models.execute_kw(db, uid, password, 'sale.order', 'search', [[['id', 'in', expired_quotes_ids]]]))
    

# draft_quotes = models.execute_kw(db, uid, password, 
#                                  'sale.order', 'read',)

# draft_quotes = models.execute_kw(db, uid, password, 'sale.order', 'search_read', [[]],
#                   {'fields': ['name', 'validity_date'], 'limit': 5})

# print(draft_quotes)

# # Following line will confirm draft_quotes
# if_confirmed = models.execute_kw(db, uid, password,
#                                  'sale.order', 'action_confirm',
#                                  [draft_quotes])

# print(if_confirmed)

print('------------------')

# id1 = models.execute_kw(db, uid, password, 'ir.model', 'create', [{
#     'name': "Custom Model",
#     'model': "x_custom3",
#     'state': 'manual',
# }])
# print(id1)
# models.execute_kw(db, uid, password, 'ir.model.fields', 'create', [{
#     'model_id': 665,
#     'name': 'ww',
#     'ttype': 'char',
#     'state': 'manual',
#     'required': True,
# }])
# record_id = models.execute_kw(db, uid, password, 'x_custom3', 'create', [{'x_name1': "test record"}])
# record_ids = models.execute_kw(db, uid, password, 'x_custom3', 'search_read', [[['x_name1','=','test record']]], {'fields': ['create_date']})
# print(record_ids)