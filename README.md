# Curso de FastAPI: Introducción, Operaciones, Validaciones y Autenticación

Este curso hace parte de los encontrado en platzi.


## Comandos
Para le ejecución y despliegue en nuestra máquina de la Api usamos:
* uvicorn **\<name main file\>**:**\<name app in code\>**
Algunos comandos que se pueden usar a través de la terminal son:
* --reload, permite que la api se actualice a medida que hago cambios en el código
* --port **\<number\>**, permite elegir el puerto en el que deseo exponer la api.
* --host 0.0.0.0, permite convertir mi pc en un host de la red a la que se conecta, por lo que
se puede abrir desde otros dispositivos.

## Documentación FastApi

FastApi hace uso de swagger para generar una documentación de nuestra app. Para ver esta le añadimos a
nuestra url /docs, allí encontramos un json con los objetos que se tienen en el navegador. Dentro de esta
dirección encontraremos nuestros endopoints, sus parémetros y la forma de hacer peticiones en estos.