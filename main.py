#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# Author: Lucía Martín Fernández, Jun 2020


import sys
import os
from Bio import Seq
from Bio import SeqIO
import shutil
import argparse
from distutils.dir_util import copy_tree

from gbk_fasta import gbk_to_fasta, create_dic_org, lee_carpeta
from blastp import blast
from muscle import muscle, prep_muscle, muscle_tree
from rename import renom
from myprosite import create_dic_dominios, search_pattern
from help import carpeta_help, querys_help, helpme, check_proyecto




def main():

    """
        Función principal del proyecto.
        Coge de primer argumento el nombre de la carpeta donde se encuentra
        los genbank y de segundo argumento el fichero con las query.
        Realiza el control de argumentos a la vez que se van ejecutando 
        alguna de las funciones de los módulos
    """
    
    
    #CONTROL DE ARGUMENTOS:
    
    
    parser = argparse.ArgumentParser(description = "Este programa sirve para \
                                     buscar y analizar unas proteínas \
                                     determinadas query en una serie de \
                                     genomas bacterianos",
                                     epilog = "Se requiere que el archivo \
                                     \"prosite.dat\" se encuentre en la \
                                     carpeta desde la que se ejecuta el \
                                     programa")
    
    parser.add_argument("carpeta", help = "Contiene los genomas bacterianos en \
                        formato genbank")
    parser.add_argument("query", help = "Fichero tipo fasta que contiene las \
                        proteínas que se quieren buscar en los genomas \
                        bacterianos")
    parser.add_argument("-p", "--proyecto", help = "Nombre del proyecto \
                        (sin blancos)")
    parser.add_argument("-c", "--coverage", help = "Por defecto se define como \
                        50", type=int, default=50)
    parser.add_argument("-i", "--identity", help = "Por defecto se define como \
                        30", type=int, default=30)

    
    args = parser.parse_args()

    carpeta = args.carpeta
    querys = args.query
    name_proy = args.proyecto
    cov = str(args.coverage)
    ident = str(args.identity)
    
    
     
    #Control de argumento name_proy
    
    if name_proy == None:
        name_proy = input("Nombre del proyecto (sin blancos): ")
        
    check_proyecto(name_proy)
        
    #Creación de carpetas:
    
    os.mkdir(name_proy)

    results = "{}/resultados".format(name_proy)
    os.mkdir(results)

    data = "{}/data".format(name_proy)
    os.mkdir(data)

    secuencias_fasta = "{}/secuencias.fasta".format(data)
    
    
    #CONTROL DE ARGUMENTOS CARPETA Y QUERY

    help_query = False
    help_carp = False
    
    
    #Control de argumento carpeta

    try:
        dic_org = lee_carpeta(carpeta, secuencias_fasta)
    except:
        help_carp = True
        
    if os.path.isfile(secuencias_fasta) == False:
        help_carp = True
    else:
        if (os.stat(secuencias_fasta).st_size == 0):
            help_carp = True
            
            
    #Control de argumento query
    
    f = open(querys, "r")
    
    if f :
        lineas = f.read()
        f.close()
    else:
        help_query = True

    if lineas[0][0] != ">":
        help_query = True
        

    #Ejecución de comandos de ayuda: 
    
    if help_carp == True:
        if help_query == True:
            carpeta_help(carpeta)
            querys_help(querys)
            helpme(parser, name_proy)
        elif help_query == False:
            carpeta_help(carpeta)
            helpme(parser, name_proy)
    elif help_query == True:
        querys_help(querys)
        helpme(parser, name_proy)
        

    print("Por favor espere, el proceso puede tardar unos minutos")
    

    copy_tree(carpeta, data)

    dic_dominios = create_dic_dominios()

    

    with open(querys, "r") as query_handle:

        for record in SeqIO.parse(query_handle, "fasta"):

            seq = record.seq
            id = record.id


            folder = "{}/{}".format(results, id)

            if os.path.isdir(folder) == True:
                shutil.rmtree(folder, ignore_errors=True)

            os.mkdir(folder)


            query = "{}/{}.fasta".format(folder, id)

            with open(query, "w") as q:

                print(">{}\n{}\n".format(id,seq), file = q)


            output_blast = "{}/blast_{}.tsv".format(folder, id)


            blast(query, secuencias_fasta, output_blast, cov, ident)


            input_muscle = "{}/muscle_{}.fa".format(folder, id)
            prep_muscle(output_blast, query, input_muscle, secuencias_fasta)


            align = "{}/align_{}.fa".format(folder, id)
            muscle(input_muscle, align)

            tree = "{}/tree_{}.nw".format(folder, id)
            muscle_tree(align, tree)

            dominios = "{}/dominios_{}.txt".format(folder, id)
            search_pattern(dic_dominios, input_muscle, dominios)


            renom(dic_org, input_muscle)
            renom(dic_org, align)
            renom(dic_org, tree)
            renom(dic_org, dominios)

            
            print(" - Se ha completado el análisis de la proteína " + id)
            

            
    shutil.copy(querys, data)
    

    print("El proceso ha terminado")
    
    

    return dominios



if __name__=="__main__":
    main()
