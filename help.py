#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# Author: Lucía Martín Fernández, jun 2020


import shutil
import argparse
import sys



def carpeta_help(carpeta):
    
    """
        Indica que el argumento que está fallando es la carpeta
    """

    print("  " + carpeta + "\t\tNo es un argumento válido. \
          \n\t\t\tPor favor introduzca un directorio que contenga" +
          " \n\t\t\tlos genomas bacterianos\n")

    

def querys_help(querys):
    
    """
        Indica que el argumento que está fallando es la query
    """

    print("  " + querys + "\t\tNo es un argumento válido. \
          \n\t\t\tPor favor introduzca un fichero tipo fasta que contenga" +
          " \n\t\t\tlas proteínas query\n")

    

def helpme(parser, name_proy):
    
    """
        Elimina la carpeta del proyecto, imprime la ayuda del script 
        y termina la ejecución del programa
    """
    
    shutil.rmtree(name_proy, ignore_errors=True)
    print("Se ha borrado la carpeta del proyecto " + name_proy)
    
    parser.print_help()
    
    sys.exit(1)
    
    
    
def check_proyecto(name_proy):

    """
        Es una función recursiva. 
        Comprueba que no exista una carpeta con el mismo nombre
        de proyecto introducido. 
    """
    
    if os.path.isdir(name_proy):
        
        print("Ya existe una carpeta con el nombre del proyecto \
        dado anteriormente.")
        print("Si no desea eliminarla, podrá introducir \
        un nombre diferente para el proyecto")

        check = input("¿Desea eliminar la carpeta existente (s/n)?" )

        if (check.lower() == "s"):
            shutil.rmtree(name_proy, ignore_errors=True)
            
        elif (check.lower() == "n"):
            name_proy = input("Introduzca un nombre para el proyecto \
            diferente (sin blancos): ")
            check_proyecto(name_proy)
            
        else:
            print("No se ha introducido una opción válida, por favor \
                  vuelva a ejecutar el programa")
            sys.exit(1)
