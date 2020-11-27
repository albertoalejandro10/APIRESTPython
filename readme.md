# API REST DESARROLLADA EN PYTHON CON FLASK

Este repositorio contiene una API desarrollada con Python y Flask, utilizamos una estructura JSON extraida mediante Scraping de la pagina web https://garminstore.cl/wearables/productos/todos.html,  utilizamos las librerias jsonify para manejar las estructuras de datos JSON y Request para lograr completar las operaciones CRUD para enviar nuevos productos mediante POST, modificar mediante PUT o eliminar mediante DELETE algun producto.

## Instalación

No subí la carpeta venv/, debes instalarla y luego instalar los paquetes requeridos

- Instalar el entorno venv

```bash
python3 -m venv venv
```

- Instalar Flask
```bash
pip install flask
```
- Instalar los paquetes necesarios
```bash
pip install jsonify request
```

## Uso

Una vez realizada la instalacion, procedemos a utilizar el proyecto el sistema estara corriendo en el puerto 4000 con Debugger.
- Ejecutar el servidor desde la consola de Ubuntu:
```bash
python3 app.py
```
Ya el servidor debe estar corriendo desde la consola, ya solo debes utilizar algun programa como Postman o Insomnia para traer, enviar, modificar o eliminar los productos de la API.
- HTTP GET - Tipos de metodo para traer productos, por ejemplo:

```bash
http://localhost:4000/products
```

```bash
http://localhost:4000/products/Serie_Instinct
```

```bash
http://localhost:4000/products/prices/100000&999999
```
- HTTP POST: Enviar un nuevo producto al servidor:
```bash
http://localhost:4000/products
{
	"name":"reloj_casio",
	"description": "a prueba balas",
	"price": 1000000
}
```

- HTTP PUT: Modificar un producto existente:
```bash
http://localhost:4000/products/reloj_casio
{
	"name":"reloj_casioTest",
	"description": "a prueba balas",
	"price": 1000000
}
```
- HTTP DELETE: Eliminar un producto existente:
```bash
http://localhost:4000/products/reloj_casio

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)