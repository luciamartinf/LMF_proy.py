#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

def help():

    """
        Ayuda del programa
    """

    print("Este programa sirve para buscar y analizar unas proteínas \
    determinadas query en una serie de genomas bacterianos.")

    print("Para ello, realiza una serie de tareas: ")
    print(" - BlastP: Va a comparar las secuencias de nuestras proteínas \
    con las proteínas de los genomas bacterianos. De esta forma, obtendremos \
    como resultado solo aquellas proteínas del genoma que tienen una cierta \
    similitud con la proteína query.")
    print(" - Árbol filogenético: ")
    print(" - Búsqueda de dominios: ")

    print("Por cada proteína query, se van a crear una serie de archivos que \
    se guardarán dentro de la carpeta \"resultados\" de la carpeta del \
    proyecto: ")
    print(" - blast_{query}.tsv : El resultado del Blastp con los datos \
    de evalue, identidad y cobertura además del nombre y secuencia de las \
    proteínas subject" )
    print(" - {query}.fasta : Un fichero tipo fasta con todas los hits del \
    BlastP, incluídos la secuencia y el identificador de la query")
    print(" - align_{query}.fa : ")
    print(" - tree_{query}.nw : ")
    print(" - dominios_{query}.txt : ")


    print("ayuda porque no se que poner en la ayuda")
    print("usage: ")
