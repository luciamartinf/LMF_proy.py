#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import subprocess
import sys
from Bio import Seq
from Bio import SeqIO

fasta = sys.argv[1] #query
multifasta = sys.argv[2] #subject


def blast(fasta, multifasta, output_blast, coverage=str(50), identity=str(30)):

    with open(output_blast, "w") as salida:

        command_line = ['blastp', '-query', fasta,
                        '-subject', multifasta,
                        '-evalue', '0.000001',
                        '-outfmt', '6 sseqid pident qcovs evalue sseq']
        blastp = subprocess.Popen(command_line,
                                  stdout=subprocess.PIPE)
        #"awk -v identity=identity '$2 > identity {print}'"

        awk = subprocess.Popen(['/usr/bin/awk','-v','identity='+identity,
                                '$2 >= identity {print}'],
                               stdin=blastp.stdout,
                               stdout=subprocess.PIPE)

        awk2=subprocess.Popen(['/usr/bin/awk','-v','coverage='+coverage,
                               '$3 >= coverage {print}'],
                              stdin=awk.stdout,
                              stdout=salida)
        awk2.wait()

    return output_blast


#try:
    #identity = sys.argv[4]
    #coverage = sys.argv[3]
    #blastp(fasta, multifasta, coverage, identity)
#except:
    #try:
        #identity = sys.argv[4]
        #blastp(fasta, multifasta, identity, coverage=str(50))
    #except:
        #try:
            #coverage = sys.argv[3]
            #blastp(fasta, multifasta, coverage, identity=str(30))
        #except:
            #blastp(fasta, multifasta, coverage=str(50), identity=str(30))

#probar a poner los try dentro de blastp





#seqs = ['P00519', 'P05480', 'P12931']

#for seq in seqs:
      #command_line = ['blastp','-query',
                #seq + '.fasta','-out',
                #seq + '_blout', '-outfmt',
                #'6','-db','nr.00']
