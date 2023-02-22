# Proyecto de Idiomas UT

Este proyecto es un sitio web monolítico desarrollado con Django y utilizando el template Metronic. 
Es un proyecto de grado realizado para culminar la fase tecnológica y permite la administración de los usuarios que se inscriben
en uno de los idiomas ofrecidos por la Universidad.

## Instalación

Clonar el repositorio:
```bash
git clone https://github.com/Danielmc09/idiomasut.git
```
Crear un entorno virtual:
```bash
python -m venv env
```
Activar el entorno virtual:
```bash
source env/bin/activate  # para Linux/MacOS
env\Scripts\activate  # para Windows
```
Instalar las dependencias:
```bash
pip install -r requirements.txt
```
Crear las migraciones:
```bash
python manage.py makemigrations
```
Aplicar las migraciones:
```bash
python manage.py migrate
```
Crear un superusuario:
```bash
python manage.py createsuperuser
```
Ejecutar el servidor local:
```bash
python manage.py runserver
```

Una vez instalado y ejecutando el servidor local, se puede acceder a la página de inicio en la URL http://localhost:8000/.
Desde allí, se puede acceder a las diferentes funcionalidades del sitio web y administrar los usuarios que se inscriben
en los idiomas ofrecidos por la Universidad.

## Contribución

Si deseas contribuir al proyecto, puedes hacer lo siguiente:

- Haz un fork del repositorio.

Crea una rama con la nueva funcionalidad o arreglo de errores:
```bash
git checkout -b nueva-funcionalidad
```
Haz los cambios necesarios y haz commit:
```bash
git commit -am "Agregada nueva funcionalidad"
```
Envía tus cambios a tu repositorio fork:
```bash
git push origin nueva-funcionalidad
```
Haz una Pull Request para solicitar que tus cambios se fusionen con la rama principal del repositorio original.
## Licencia
Este proyecto está bajo la Licencia MIT.
