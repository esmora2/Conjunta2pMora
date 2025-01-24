# Conjunta2pMora

Este repositorio contiene un proyecto desarrollado en Django y MySQL, que incluye funcionalidades de gestión de inventarios, análisis de calidad de código con SonarQube, pruebas de recuperación y regresión, y simulación de cargas concurrentes.

## Repositorio
[Conjunta2pMora - GitHub](https://github.com/esmora2/Conjunta2pMora.git)

## Tecnologías Utilizadas
- **Django**: Framework para desarrollo web.
- **MySQL**: Base de datos para almacenamiento de datos.
- **SonarQube**: Análisis de calidad de código y detección de vulnerabilidades.
- **Apache JMeter**: Herramienta para pruebas de estrés.
- **Python**: Lenguaje de programación principal.

## Características
1. **Gestión de Inventarios**:
   - Tablas relacionadas para productos, categorías, y bodegas.
   - Relación entre productos y categorías con validaciones de integridad referencial.
   - Capacidad de registrar ventas y asociarlas con productos.

2. **Análisis de Calidad del Código**:
   - Configuración y uso de SonarQube para identificar problemas de seguridad y buenas prácticas en el código.
   - Ejemplo: Detección y recomendación para ocultar claves secretas sensibles de Django.

3. **Pruebas de Recuperación y Regresión**:
   - Simulación de fallos en la base de datos y restauración desde copias de seguridad.
   - Verificación de que los cambios recientes no afecten las funcionalidades existentes.

4. **Pruebas de Estrés**:
   - Simulación de 500 solicitudes concurrentes al endpoint de ventas durante 4 minutos.
   - Generación de métricas clave como tiempo de respuesta promedio, tasa de error, y throughput.

## Requisitos del Proyecto
1. **Dependencias**:
   - Python 3.x
   - Django 4.x
   - MySQL Server 8.x
   - Apache JMeter
   - SonarQube
2. **Configuraciones**:
   - Claves sensibles deben manejarse mediante variables de entorno.
   - Asegúrate de que el servidor MySQL esté ejecutándose y configurado correctamente.

## Instalación
### Clonar el Repositorio
```bash
$ git clone https://github.com/esmora2/Conjunta2pMora.git
$ cd Conjunta2pMora
```

### Configuración del Entorno Virtual
```bash
$ python -m venv venv
$ source venv/bin/activate   # Linux/MacOS
$ venv\Scripts\activate    # Windows
```

### Instalar Dependencias
```bash
$ pip install -r requirements.txt
```

### Configuración de la Base de Datos
1. Crea la base de datos MySQL:
   ```sql
   CREATE DATABASE inventariotest;
   ```
2. Configura las credenciales de acceso en `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'inventariotest',
           'USER': 'root',
           'PASSWORD': 'admin',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

### Migraciones
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

### Ejecutar el Servidor
```bash
$ python manage.py runserver
```

## Uso
1. Accede al panel de administración de Django:
   - URL: `http://localhost:8000/admin`
   - Credenciales: Crear con `python manage.py createsuperuser`
2. Prueba los endpoints API para productos, categorías, y ventas:
   - Base URL: `http://localhost:8000/api/`

## Pruebas
### Pruebas de Recuperación
1. Generar un backup de la base de datos:
   ```bash
   mysqldump -u root -p inventariotest > backup.sql
   ```
2. Restaurar el backup:
   ```bash
   mysql -u root -p inventariotest < backup.sql
   ```

### Pruebas de Estrés
1. Configura Apache JMeter para enviar solicitudes concurrentes.
2. Analiza los resultados generados (tiempo promedio, errores, throughput).

## Contribuciones
1. Realiza un fork del repositorio.
2. Crea una rama para tu funcionalidad:
   ```bash
   $ git checkout -b feature/nueva-funcionalidad
   ```
3. Realiza un pull request detallando los cambios.

## Licencia
Este proyecto está bajo la Licencia MIT.

---

**Autor:** Erick Mora
