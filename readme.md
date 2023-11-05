## Finarden

### Objetivo:
Este un proyecto para la materia de emprendimiento en el cual se busca crear un MVP lo mas rapido posible, usando la menor cantidad de codigo

### Concepto:
Finarden surge como una plataforma para llevar registros de los ingresos/gastos de una persona de forma que pueda sacar reportes de estos

### Tecnologias 
![python](https://img.shields.io/badge/-python%20-yellow?logo=python)   ![django](https://img.shields.io/badge/-django%20-green?logo=django)


## Instalacion

Para instalar en local siga los siguientes pasos 

1. Clone el repositorio 
2. Cree un entorno virtual de python con 
```sh
python3 -m venv env && source env/bin/activate
```
3. Instale las depenencias
```sh
pip install -r requirements.txt
```
4. Cree la Base de datos
```sh
python manage.py migrate
```
5. Cree un super usuario
```sh
python manage.py createsuperuser
```
6. Ingrese a  [http://127.0.0.1:8000/home](http://127.0.0.1:8000/home) con el usuario que acaba de crear
7. En Groups cree un grupo llamado 'app_user' el cual solo debe tener permisos sobre la app de expends
8. Listo para probar , cree usuarios en [http://127.0.0.1:8000/users](http://127.0.0.1:8000/users)

## Consideraciones
- La app es un MVP y no esta pensado para escalar
