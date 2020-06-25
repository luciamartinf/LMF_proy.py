#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from Bio.ExPASy import Prosite,Prodoc
import re
from Bio import Seq
from Bio import SeqIO


"""
    Para la ejecución de este paquete es necesario el fichero "prosite.dat"
    en la carpeta desde la que se está ejecutando el programa
"""


def create_dic_dominios():

    """
        Crea un diccionario con los patrones de la base de datos de
        prosite transformados para que pueda utilizarlos el módulo re
        y el accession correspondiente a cada patrón

    """

    dic_dominios = {}

    with open("prosite.dat","r") as handle:

        records = Prosite.parse(handle)

        for record in records:

            accession = record.accession
            pattern = record.pattern

            if pattern == "":
                continue
            else:
                pattern = pattern.replace('{', '[^')
                pattern = pattern.replace('}', ']')
                pattern = pattern.replace('(', '{')
                pattern = pattern.replace(')', '}')
                pattern = pattern.replace('-', '')
                pattern = pattern.replace('x', '.')
                pattern = pattern.replace('>', '$')
                pattern = pattern.replace('<', '^')

            dic_dominios[pattern] = accession


    return dic_dominios



def search_pattern(dic, input, output):

    """
        Busca cada patrón que encuentra en el diccionario en las
        secuencias proteicas que encuentra en el fasta que hace de input.
        Devuelve un fichero tipo txt con información sobre los dominios
        encontrados en cada una de las proteínas.
    """

    with open(input, "r") as input_handle:

        with open(output, "w") as output_handle:

            for record in SeqIO.parse(input_handle, "fasta"):

                prot_id = record.id
                prot = str(record.seq)

                print("\n>"+prot_id+"\n", file = output_handle)

                for pattern in dic:

                    accession = dic[pattern]

                    if re.search(pattern, prot):

                        with open("prosite.dat","r") as handle:

                            records = Prosite.parse(handle)

                            for record in records:

                                if (record.accession == accession):

                                    name = record.name
                                    description = record.description
                                    pattern_2 = record.pattern

                                    print("\tDominio: " + name
                                          + " | " + accession, 
                                          file = output_handle)
                                    print("\tDescripción: " + description,
                                          file = output_handle)
                                    print("\tPatrón: " + pattern_2,
                                          file = output_handle)

                                    match = re.finditer(pattern, prot)

                                    for m in match:
                                        start = m.start()
                                        end = m.end()
                                        base = m.group()

                                        print("\t- " + base + " - Posición: "
                                              + str(start) + " - " + str(end),
                                              file = output_handle)

                                    print("", file = output_handle)


    return output
