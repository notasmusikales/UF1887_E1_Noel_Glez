# BLOQUE 2 – Componentes de seguridad del ERP
## 1. Sistema de autenticación
### El sistema utiliza autenticación basada en usuario y contraseña gestionada por Odoo.
### El usuario introduce sus credenciales en la página de login:
- http://localhost:8069/web/login
Odoo verifica las credenciales en la tabla res_users.
---
## 2. Control de sesiones
- Después de autenticarse el sistema crea una sesión activa.
La sesión se mantiene mediante cookies en el navegador.
Esto permite que el usuario navegue por el ERP sin volver a autenticarse en cada acción.
---
## 3. Roles del sistema
- Los roles en Odoo se gestionan mediante grupos de seguridad.
Cada grupo define permisos sobre módulos y datos.
Ejemplos de roles:
- Administrador
  - Usuario interno
  - Usuario de ventas
  - Usuario contable
---
## 4. Usuarios existentes
- Los usuarios se gestionan desde:
Settings → Users & Companies → Users
- Cada usuario tiene configurado:
  - login
  - contraseña
  - email
  - grupos asignados
  
- Los permisos del usuario dependen de los grupos asignados.