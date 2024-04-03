# Kata_ohce
Tarea fundamentos testing TDD

Este proyecto se encarga de saludar al usuario dependiendo de la hora del dia, ademas de revertir palabras, detectar palindromos y despedirse de usuario.


# Instalacion

Para utilizar este programa en primer lugar es tener python instalado en el sistema

luego clone el repositorio usando

git clone <URL>

ingreselo en el directorio de su preferencia y ejecute el comando 

pip install -r requirements.txt

para obtener todas las librerias necesarias para la ejecucion del programa


# USO

El codigo esta dividido en 2 partes principales "ohce.py" y "test_ohce.oy"

para la ejecucion de cada uno ejecute en terminal

python ohce.py 

El programa esperara un input, los dejara pasar hasta que el input inicial sea una Palabra seguida de ohce, luego entrara en el ciclo de procesamiento de inputs, donde los nuevos input, retornaran como su version reversa y en caso de ser palindromos te mencionara lo bonita que es tu palabra, puede repetir este proceso infinitamente hasta entregar el input "Stop!" donde el programa se despedira del usuario y cerrará.

pytest test_ohce.py

La ejecucion de este codigo tiene como funcion, testear las funciones dentro de ohce.py y verificar si son correctas en sus resultados o no, este programa funciona basicamente igual al anterior, al ejecutarse esperara algun input comenzando con ohce, luego puedes probar y recibir resultados, pero al ejecutar "Stop!" el programa aparte de terminar, te entregara los resultados de testeos de cada una de las pruebas proporcionadas, en este caso 8