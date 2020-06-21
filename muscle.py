#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import subprocess
import sys
from Bio import Seq
from Bio import SeqIO

#input = sys.argv[1] #output_blast
#fasta = sys.argv[2] #PBP1_...

def prep_muscle(output_blast, fasta, input_muscle):

    handle = open(input_muscle, "w")

    with open(fasta, "r") as query_handle:
        for record in SeqIO.parse(query_handle, "fasta"):
            protein_id = record.id
            seq = record.seq

            print(">{}\n{}\n".format(protein_id,seq), file=handle)

    subprocess.run(['/usr/bin/awk','{print ">"$1; print $5}', output_blast],
                     stdout=handle)

    handle.close()

    return input_muscle


def muscle(input_muscle, align):

    muscle_fa = subprocess.Popen(['muscle', '-in', input_muscle,
                                  '-out', align],
                                  stderr=subprocess.DEVNULL)

    return align

def muscle_tree(align, tree):

    subprocess.run(['muscle', '-maketree',
                     '-in', align,
                     '-out', tree,
                     '-cluster', 'neighborjoining'],
                    stderr=subprocess.DEVNULL)

    return tree

#sacar el arbol con phylo
#prep_muscle(input, fasta)
#muscle()
