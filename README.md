# lib--python

> Coleccion de codigo de python 3 para GAMESS

## Clase documento

Permite abrir el archivo .log ya se por medio del nombre que se guarda en una variable o por el explorador que proporciona tkinter (sin necesidad de crear una interfaz completa).

### Métodos

_**abrir_docexp( )**_: cargar el documento por el explorador; publico

_**abrir_doc( )**_: cargar el documento por el nombre (debe estar en la misma carpeta que el programa .py); publico

_**cerrar_doc( )**_: cerrar el documento si ya se ha cargado; publico

_**convert_lista**_(_lista_): recibe una lista y transforma sus valores de _string_ a _float_ (todos deben ser valores numericos en forma de _string_); protegido

## Clase Shielding

Permite buscar los valores de Shielding (escudo) en el archivo .log si existen (debe estar previamente cargado el documento).

### Metodos

_**look_shielding( )**_: Buscar los valores de shielding de hidrogeno y carbono en el archivo .log; publico

_**identificar_atom( )**_: Correccion de la identificacion de atomos de hidrogeno y carbono; privado

_**save_shd( )**_: guardar en un archivo .txt valores encontrados tanto de carbono como hidrogeno; publico
