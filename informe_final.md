# INFORME FINAL – PRÁCTICA DE SEGURIDAD EN ERP-CRM (ODOO 18)

## 1. Introducción

En esta práctica se ha realizado el análisis y configuración básica de la seguridad de un sistema ERP-CRM basado en **Odoo 18**, ejecutado en un entorno compuesto por **Ubuntu Server, PostgreSQL y contenedores Docker**.

El objetivo de la práctica ha sido:

- identificar los canales de acceso al sistema ERP
- analizar los componentes de seguridad del sistema
- crear una estructura básica de usuarios y roles
- verificar que los accesos están correctamente configurados

Esta actividad permite comprender cómo se controla el acceso a la información dentro de un sistema ERP.

---

# 2. Entorno tecnológico utilizado

| Componente | Descripción |
|---|---|
| Sistema operativo | Ubuntu Server |
| ERP | Odoo 18 |
| Base de datos | PostgreSQL |
| Plataforma de contenedores | Docker |
| Método de acceso | Navegador web |

El sistema se ejecuta mediante contenedores Docker y permite acceso al ERP a través de un navegador web.

---

# 3. Pasos realizados en la práctica

## 3.1 Identificación de canales de acceso

Se analizaron los diferentes canales mediante los cuales se puede acceder al sistema ERP.

Los accesos identificados fueron los siguientes:

| Canal de acceso | Protocolo | Herramienta | Tipo de autenticación |
|---|---|---|---|
| Acceso web | HTTP | Navegador web | Usuario y contraseña |
| Acceso base de datos | PostgreSQL TCP/IP | psql / herramientas SQL | Usuario PostgreSQL |
| Administración del servidor | SSH | Terminal | Usuario del sistema |
| API del sistema | HTTP API | Scripts / aplicaciones externas | Usuario + contraseña |

Este análisis permite identificar las posibles **vías de acceso al sistema** y aplicar medidas de seguridad adecuadas.

---

## 3.2 Componentes de seguridad del ERP

Se analizaron los mecanismos que utiliza Odoo para controlar el acceso al sistema.

Los principales componentes de seguridad identificados fueron:

### Sistema de autenticación

Odoo utiliza autenticación basada en **usuario y contraseña**.  
Las credenciales se verifican en la tabla de usuarios del sistema.

### Control de sesiones

Cuando un usuario inicia sesión, el sistema crea una **sesión activa** que permite utilizar el ERP sin necesidad de autenticarse en cada acción.

### Roles del sistema

Los roles se gestionan mediante **grupos de seguridad**, que definen qué módulos y acciones puede utilizar cada usuario.

### Gestión de usuarios

Los usuarios se crean y gestionan desde el panel de administración del ERP.

La estructura de seguridad sigue la relación:
usuarios -> grupos -> permisos

---

# 4. Creación de usuarios y roles

Se configuró una estructura básica de roles para simular el funcionamiento de una empresa.

## Roles creados

| Rol | Función |
|---|---|
| Administración | Gestión completa del sistema |
| Ventas | Gestión comercial |
| Contabilidad | Gestión financiera |
| Soporte | Gestión de incidencias |

## Usuarios creados

| Usuario | Rol asignado |
|---|---|
| administrador | administración |
| comercial | ventas |
| contable | contabilidad |
| soporte | soporte |

Cada usuario tiene acceso únicamente a los módulos necesarios para su función dentro de la organización.

---

# 5. Verificación de accesos

Se realizaron pruebas de acceso iniciando sesión con cada uno de los usuarios creados.

El objetivo fue comprobar:

- que cada usuario puede acceder al sistema
- que solo puede acceder a los módulos correspondientes a su rol

## Resultados de la verificación

| Usuario | Acceso al sistema | Módulos visibles | Módulos restringidos |
|---|---|---|---|
| administrador | Correcto | Todos los módulos | Ninguno |
| comercial | Correcto | CRM, Ventas | Contabilidad, Configuración |
| contable | Correcto | Contabilidad | Ventas, Configuración |
| soporte | Correcto | Helpdesk | Ventas, Contabilidad |

Los resultados confirman que los permisos se aplican correctamente según los roles asignados.

---

# 6. Problemas detectados

Durante la realización de la práctica se identificaron algunos aspectos importantes:

- una asignación incorrecta de grupos puede otorgar permisos innecesarios
- algunos módulos pueden aparecer visibles si el usuario pertenece a varios grupos
- es necesario verificar siempre los accesos después de realizar cambios en los permisos

Estos problemas se solucionaron revisando la configuración de los grupos y los usuarios.

---

# 7. Configuración final del sistema

La configuración final del sistema quedó definida de la siguiente manera:

| Usuario | Rol | Acceso |
|---|---|---|
| administrador | administración | acceso completo al sistema |
| comercial | ventas | gestión de clientes y pedidos |
| contable | contabilidad | gestión de facturas y pagos |
| soporte | soporte | gestión de incidencias |

La configuración sigue el principio de seguridad conocido como:

**principio de mínimo privilegio**

Cada usuario dispone únicamente de los permisos necesarios para realizar su trabajo.

---

# 8. Conclusión

La práctica permitió comprender los mecanismos básicos de seguridad de un sistema ERP basado en Odoo.

Se identificaron los diferentes canales de acceso al sistema, se analizaron los componentes de seguridad del ERP y se configuró una estructura básica de usuarios y roles.

Las pruebas realizadas confirmaron que el sistema controla correctamente el acceso a los módulos según el rol asignado a cada usuario.

La correcta gestión de usuarios, roles y permisos es fundamental para garantizar la seguridad y el correcto funcionamiento de un sistema ERP-CRM.
