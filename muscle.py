#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import subprocess
import sys
from Bio import Seq
from Bio import SeqIO
import os



def prep_muscle(output_blast, fasta, input_muscle, output_gbk):

    """
        Crea un fichero tipo fasta a partir del blast para poder hacer
        el alineamiento con muscle.
        El fichero contiene las secuencias subject que fueron hits del blast
        y la secuencia query.
    """

    handle = open(input_muscle, "w")


    with open(fasta, "r") as query_handle:
        for record in SeqIO.parse(query_handle, "fasta"):
            protein_id = record.id
            seq = record.seq

            print(">{}\n{}\n".format(protein_id,seq), file = handle)

    local = "borra.txt"
    l = open(local, "w")
    subprocess.run(['/usr/bin/awk','{print $1}', output_blast],
                   stdout = l)
    l.close()

    l2 = open(local, "r")
    filetext = l2.read()
    l2.close()

    with open(output_gbk, "r") as secuencias:
        for record in SeqIO.parse(secuencias, "fasta"):
            protein_id = record.id
            seq = record.seq

            if protein_id in filetext:
                print(">{}\n{}\n".format(protein_id,seq), file = handle)


    handle.close()

    os.remove(local)


    return input_muscle



def muscle(input_muscle, align):

    """
        Crea un fichero tipo fasta con las secuencias alineadas
    """

    subprocess.run(['muscle', '-in', input_muscle,
                    '-out', align],
                   stderr = subprocess.DEVNULL)


    return align



def muscle_tree(align, tree):

    """
        Crea un fichero tipo nw a partir del cuál se puede graficar un árbol
        filogenético
    """

    subprocess.run(['muscle', '-maketree',
                    '-in', align,
                    '-out', tree,
                    '-cluster', 'neighborjoining'],
                   stderr = subprocess.DEVNULL)


    return tree
