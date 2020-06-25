#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#Lucía Martín Fernández



import shutil
import argparse
import sys

def carpeta_help(carpeta):

    print("  " + carpeta + "\t\tNo es un argumento válido. \
          \n\t\t\tPor favor introduzca un directorio que contenga" +
          " \n\t\t\tlos genomas bacterianos\n")


def querys_help(querys):

    print("  " + querys + "\t\tNo es un argumento válido. \
          \n\t\t\tPor favor introduzca un fichero tipo fasta que contenga" +
          " \n\t\t\tlas proteínas query\n")


def helpme(parser, name_proy):
    shutil.rmtree(name_proy, ignore_errors=True)
    print("Se ha borrado la carpeta del proyecto " + name_proy)
    parser.print_help()
    sys.exit(1)
