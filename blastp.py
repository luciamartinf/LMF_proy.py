#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# Author: Lucía Martín Fernández, jun 2020

import subprocess
import sys
from Bio import Seq
from Bio import SeqIO


def blast(fasta, multifasta, output_blast, coverage=str(50), identity=str(30)):

    """
        Ejecuta blastp con un evalue predeterminado de 0.00001
        Después filtra el resultado con la cobertura y la identidad predeterminadas
        como 50 y 30 respectivamente aunque pueden ser definidas por el usuario.
        Devuelve un fichero tipo tsv con el resultado del blast que por cada hit con la query incluye:
        - identificador secuencia subject
        - identidad
        - cobertura
        - evalue
        - secuencia subject
    """

    with open(output_blast, "w") as salida:

       
        command_line = ['blastp', '-query', fasta,
                        '-subject', multifasta,
                        '-evalue', '0.00001',
                        '-outfmt', '6 sseqid pident qcovs evalue sseq']
        blastp = subprocess.Popen(command_line,
                                  stdout = subprocess.PIPE)
       
        
        awk = subprocess.Popen(['/usr/bin/awk','-v','identity=' + identity,
                                '$2 >= identity {print}'],
                               stdin = blastp.stdout,
                               stdout = subprocess.PIPE)

        awk2 = subprocess.Popen(['/usr/bin/awk',
                                 '-v','coverage=' + coverage,
                                 '$3 >= coverage {print}'],
                                stdin = awk.stdout,
                                stdout = salida)
        
        awk2.wait() #Espera a que termine el último subprocess


    return output_blast
