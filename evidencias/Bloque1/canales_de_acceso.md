# BLOQUE 1 – Identificación de canales de acceso al ERP
## 1. Acceso web
- Protocolo: HTTP / HTTPS
    - Herramienta: Navegador web
    - Puerto: 8069
    - Autenticación: usuario y contraseña de Odoo
---
## 2. Acceso a base de datos
- Protocolo: PostgreSQL TCP/IP
    - Puerto: 5432
    - Herramienta: psql / DBeaver / PgAdmin
    - Autenticación: usuario y contraseña PostgreSQL
---
## 3. Acceso administración servidor
- Protocolo: SSH
    - Puerto: 22
    - Herramienta: terminal SSH
    - Autenticación: contraseña o clave SSH
---
## 4. Acceso API del sistema
- Protocolo: HTTP / HTTPS (XML-RPC / JSON-RPC)
    - Herramienta: aplicaciones externas o scripts
    - Autenticación: usuario + contraseña o API key
  
# Canales de Acceso posibles

| Canal           | Protocolo | Herramienta        | Tipo de autenticación | Observaciones                 |
|-----------------|-----------|------------------|---------------------|-------------------------------|
| Web             | HTTPS     | Navegador        | Usuario/Contraseña  | Odoo sesiones activas         |
| Base de datos   | TCP/IP    | psql / DBeaver   | Usuario/Contraseña  | Roles y permisos revisados    |
| Administración  | SSH       | Terminal / PuTTY | Contraseña / Key    | Usuarios Linux y sudoers      |
| API             | HTTPS     | Postman / curl   | Token / Usuario     | Claves API configuradas       |