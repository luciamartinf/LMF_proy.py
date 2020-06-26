# LMF_proy.py

Este programa sirve para buscar y analizar unas proteínas determinadas query en una serie de genomas bacterianos.

### USO:

`usage: main.py [-h] [-p PROYECTO] [-c COVERAGE] [-i IDENTITY] carpeta query`

#### Argumentos posicionales, obligatorios

| **Argumento**                           | **Descripcion**                                                                                                 |                                                   
|:----------------------------------------|:----------------------------------------------------------------------------------------------------------------|
|`carpeta`                                | Directorio que contiene los genomas bacterianos en formato genbank                                              |                  
|`query`                                  | Fichero tipo fasta que contiene las proteíans que se quieren buscar en los genomas bacterianos                  |                                      

#### Argumentos opcionales 

| **Argumento**                           | **Descripción**                                                                                                 |
|:----------------------------------------|:----------------------------------------------------------------------------------------------------------------|
|`-h, --help`                             | Muestra el mensaje de ayuda y termina el proceso                                                                |
|`-p   PROYECTO, --proyecto PROYECTO`     | Nombre del proyecto                                                                                             |
|`-c COVERAGE, --coverage COVERAGE`       | Por defecto se define como 50                                                                                   |
|`-i IDENTITY,  --identity IDENTITY`      | Por defecto se define como 30                                                                                   |


### TAREAS: 

Para ello, realiza una serie de tareas: 

 - BLASTP: Va a comparar las secuencias de nuestras proteínas con las proteínas de los genomas bacterianos. De esta forma, obtendremos como resultado solo aquellas proteínas del genoma que tienen una cierta similitud con la proteína query.
 
 - Árbol filogenético: Utilizando MUSCLE, se van a alinear las secuencias y se va a generar un árbol filogenético Neighbor-Joining (N-J) para cada proteína query.
 
 - Búsqueda de dominios: Encuentra los dominios proteicos presentes en las secuencias obtenidas en el BLASTP.
 
### FICHEROS Y CARPETAS QUE CREA:  

Se va a crear una carpeta con el nombre del proyecto que contiene una carpeta "resultados" y una carpeta "data"

#### Carpeta Resultados

Por cada proteína query, se van a crear una serie de archivos que se guardarán dentro de la carpeta "resultados": 

- blast_{query}.tsv : El resultado del BLASTP con los datos de evalue, identidad y cobertura además del nombre y secuencia de las proteínas subject

- {query}.fasta : Un fichero tipo fasta con todos los hits del BLASTP, incluidos la secuencia y el identificador de la query

- align_{query}.fa : Las secuencias de las proteínas alineadas mostradas en formato fasta

- tree_{query}.nw : Árbol filogenético tipo N-J como fichero de texto preparado para ser introducido en programas como iTOL que lo dibujan.

- dominios_{query}.txt : Fichero de texto con información sobre los dominios de PROSITE encontrados en las secuencias de los hits del BLASTP.

#### Carpeta Data:

Va a copiar los archivos con los genomas bacterianos que se han utilizado para correr el script y el archivo con las proteínas query. Además, también se creará la genoteca tipo fasta con todos los genomas bacterianos. 

### INSTALACIÓN: 

Requiere la instalación de BLAST y BIOPYTHON

### OTROS:

Se requiere la presencia del fichero "prosite.dat" en la carpeta desde la que se ejecuta el programa

