import xmlrpc.client

url = "http://localhost:8069"
db = "odoo"
username = "admin"
password = "1234"   # o una API key

# 1. Conexión al servicio de autenticación
common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")

# 2. Autenticación
uid = common.authenticate(db, username, password, {})

print("UID obtenido:", uid)