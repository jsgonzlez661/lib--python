# lib--python

> Coleccion de codigo de python 3 para GAMESS 

## Clases (Herarquia):
    1. documento
        * Shielding


## Clase documento:

Permite abrir el archivo .log ya se por medio del nombre que se guarda en una variable o por el explorador que proporciona tkinter (sin necesidad de crear una interfaz completa). 

### Metodos: 

    **abrir_docexp()**: cargar el documento por el explorador; publico 
    **abrir_doc()**: cargar el documento por el nombre (debe estar en la misma carpeta que el programa .py); publico
    **cerrar_doc()**: cerrar el documento si ya se ha cargado; publico
    **_convert_lista(*lista*)**: recibe una lista y transforma sus valores de _string_ a _float_ (todos deben ser valores numericos en forma de _string_); protegido

## Clase Shielding:

Permite buscar los valores de Shielding (escudo) en el archivo .log si existen (debe estar previamente cargado el documento). 

### Metodos: 

    **look_shielding()**: Buscar los valores de shielding de hidrogeno y carbono en el archivo .log; publico
    **__identificar_atom()**: Correccion de la identificacion de atomos de hidrogeno y carbono; privado
    **save_shd(): guardar en un archivo .txt valores encontrados tanto de carbono como hidrogeno; publico