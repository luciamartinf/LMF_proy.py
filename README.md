# LMF_proy.py

Este programa sirve para buscar y analizar unas proteínas determinadas query en una serie de genomas bacterianos.


Para ello, realiza una serie de tareas: 

 - BLASTP: Va a comparar las secuencias de nuestras proteínas con las proteínas de los genomas bacterianos. De esta forma, obtendremos como resultado solo aquellas proteínas del genoma que tienen una cierta similitud con la proteína query.
 
 - Árbol filogenético: Utilizando MUSCLE, se van a alinear las secuencias y se va a generar un árbol filogenético Neighbor-Joining (N-J) para cada proteína query.
 
 - Búsqueda de dominios: Encuentra los dominios proteicos presentes en las secuencias obtenidas en el BLASTP.
 

Por cada proteína query, se van a crear una serie de archivos que se guardarán dentro de la carpeta "resultados" de la carpeta del proyecto:

- blast_{query}.tsv : El resultado del BLASTP con los datos de evalue, identidad y cobertura además del nombre y secuencia de las proteínas subject

- {query}.fasta : Un fichero tipo fasta con todos los hits del BLASTP, incluidos la secuencia y el identificador de la query

- align_{query}.fa : Las secuencias de las proteínas alineadas mostradas en formato fasta

- tree_{query}.nw : Árbol filogenético tipo N-J como fichero de texto preparado para ser introducido en programas como iTOL que lo dibujan.

- dominios_{query}.txt : Fichero de texto con información sobre los dominios de PROSITE encontrados en las secuencias de los hits del BLASTP.
