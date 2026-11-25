# Sistema de Gestión de Jugadores — Club Deportivo

Proyecto académico desarrollado con Django y MySQL/MariaDB para la evaluación de Programación Backend, Unidad 2.

## Funcionalidades
- Página principal con resumen de jugadores.
- Listado y búsqueda de jugadores.
- Crear, editar, consultar y eliminar jugadores (CRUD).
- Validaciones de campos, edad, número de camiseta y correo.
- Persistencia en MySQL/MariaDB.

## 1. Requisitos
- Python 3.10 o superior.
- XAMPP con MySQL iniciado.
- Navegador web.

## 2. Preparar MySQL en XAMPP
1. Abre XAMPP e inicia **MySQL**.
2. Entra a `http://localhost/phpmyadmin`.
3. Selecciona **Nueva** y crea una base de datos llamada `club_deportivo`.
4. Usa cotejamiento `utf8mb4_general_ci` si aparece la opción.
5. En la configuración inicial de XAMPP suele usarse el usuario `root` sin contraseña. Si tu instalación tiene contraseña, agrégala en el archivo `.env`.

## 3. Instalar y ejecutar
Abre una terminal dentro de esta carpeta y ejecuta:

```bash
python -m venv venv
```

Activar entorno:
- Windows: `venv\Scripts\activate`
- macOS/Linux: `source venv/bin/activate`

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Crea el archivo `.env` copiando `.env.example`. En Windows puedes usar:

```powershell
copy .env.example .env
```

En macOS/Linux:

```bash
cp .env.example .env
```

Si tu MySQL usa otros datos, modifica `.env`.

Crear las tablas y ejecutar:

```bash
python manage.py makemigrations jugadores
python manage.py migrate
python manage.py runserver
```

Abre `http://127.0.0.1:8000/`.

## 4. Estructura
```text
Club_Deportivo_Dasne/
├── manage.py
├── requirements.txt
├── .env.example
├── club_deportivo/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── jugadores/
    ├── migrations/
    │   ├── __init__.py
    │   └── 0001_initial.py
    ├── templates/jugadores/
    │   ├── base.html
    │   ├── inicio.html
    │   ├── lista.html
    │   ├── formulario.html
    │   ├── detalle.html
    │   └── confirmar_eliminar.html
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    └── views.py
```

## 5. Prueba del CRUD
1. En la página principal, pulsa **Registrar jugador**.
2. Completa el formulario y guarda.
3. Verifica que aparece en el listado.
4. Entra al detalle y edita un dato.
5. Comprueba que el cambio aparece en la lista.
6. Elimina un registro de prueba y confirma.

## 6. Consideraciones para la entrega
- El proyecto queda configurado para MySQL/MariaDB; debes tener XAMPP iniciado y crear la base de datos indicada.
- No incluye inicio de sesión porque la pauta indica que no se debe desarrollar login ni registro de usuarios.
- Para evidenciar Git/GitHub, crea tu rama personal y realiza commits reales con tus cambios. No inventes commits ni capturas.
- La aplicación debe ejecutarse en el computador donde se hará la presentación. Prueba la conexión antes de la evaluación.

## 7. Equipo de trabajo
- Maria Obando - Desarrollo CRUD, vistas, formularios, plantillas y enrutamiento con namespace `jugadores:`.
- Integrante 2 - Pruebas funcionales del CRUD, validacion de datos y verificacion en MariaDB/phpMyAdmin.
