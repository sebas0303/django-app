# Proyecto Unidad 04 [Aula 06]
Este es un proyecto de Silabuz Academy del Curso MPTE Backend de la Unidad 04.

## Autor ✒️
- **Sebastian Arquinigo Flores** - [sebas0303](https://github.com/sebas0303)


## Pre-requisitos 📋
Para que el proyecto funcione correctamente, se deben tener en cuenta varios aspectos:
- Contar con una versión de Python y PIP dentro del sistema
- Contar con un módulo de entornos virtuales (virtualenv recomendado)


## Instalación
Iniciar creando el entorno virtual para el despliegue
```py
pip install virtualenv
```

Crear y activar entorno virtual
```bash
virtualenv env

Linux:
source env/bin/activate

Windows:
env\Scripts\activate.bat
```

Instalar requirements.txt
```py
pip install -r requirements.txt
```

Crear archivo <code>SQLite3</code> para la base de datos dentro de <code>django_portfolio</code>
```bash
touch db.sqlite3
```

Crear archivo <code>.env</code> en la carpeta <code>zproject</code> para configurar las variables de entorno
```bash
touch .env
```

Agregue una clave secreta en el archivo <code>.env</code>, como se hace en el ejemplo siguiente
```
SECRET_KEY=This_is_the_password
```

Realice las migraciones correspondientes para las bases de datos
```bash
python manage.py makemigrations
python manage.py migrate
```