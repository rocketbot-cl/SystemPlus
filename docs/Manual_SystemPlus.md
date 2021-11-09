



# System++
  
Módulo para exportar tus variables a un archivo .txt  
  
![banner](https://i.imgur.com/YxnrHRy.jpg)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de rocketbot.

## Descripción de los comandos

### Exportar variables a archivo
  
Exporta variables de Rocketbot a un archivo de texto
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta del archivo donde se guardara las variables.||C:/User/Usuario/Folder/file.txt|

### Asignar Multiples Variables
  
Asigna un valor a multiples variables desde un objeto iterable
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato |Dato a asignar en las variables||
|Asignar variables |Variables a asignar separadas por comas|var1,var2,var|

### Realizar Backup
  
Con este comando podrás limpiar elarchivo app.log y realizar un backup
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |

### Limpiar variable(s)
  
Ingrese las variables a limpiar separadas por coma
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Variables|Variables a limpiar sin {} y separadas por coma|Variable|

### Random
  
Comando para usar librería random
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Seleccione metodo|Método de la librería con el cual se desea trabajar.||
|Valor|Argumento para el método (random.randrange(argumento)).|5,9|
|Variable|Variable donde se guardara el resultado|Variable|

### App en Primer Plano
  
Con este comando podrás traer una aplicación a primer plano.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de aplicación|Nombre de la aplicación que se quiere traer a primer plano.|test.xlsx - Excel|

### Obtener Handle de ventanas abiertas
  
Devuelve una lista con tuplas que contienen el nombre y handle de las ventanas abiertas
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Variable|Nombre de la variable donde se guardará el resultado|Variable|

### Contador
  
Devuelve un numero de contador
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Variable|Nombre de la variable donde se guardara el resultado|Variable|

### Obtener Argumentos
  
Obtiene los argumentos previamente dados al iniciar Rocketbot.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Argumentos requeridos|Argumentos que se requieren para iniciar Rocketbot.|['-start', 'id', '-db']|
|Asignar resultado a variable|Nombre de la variable donde se guardará el resultado.|Variable|

### Lanzar robot
  
Con este comando puedes lanzar un robot especificando su nombre y, en caso de que sea una db externa, indicando la ruta 
de esa db.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre del robot|Se debe indicar el nombre del robot a ejecutar|ExcelBot|
|DB Exportada|Activar el checkbox si la db donde esta el robot fue exportada. Si se encuentra en robots.db no se debe activar|Checkbox|
|Seleccionar un archivo|Si se trata de una db exportada, aca debemos indicar la ruta a esa db|Ruta a db|
