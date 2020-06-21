#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from Bio.ExPASy import Prosite,Prodoc
import re
from Bio import Seq
from Bio import SeqIO

def create_dic_dominios():
    dic_dominios={}

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
                #print(pattern)
                #print(accession)

            dic_dominios[pattern] = accession

    return dic_dominios


#accesion=dic_dominios[pattern]
#accesion=dic_dominios.get(accesion,None)
#patrones=dic_dominios.keys()

def search_pattern(dic, input, output):
    #file = open(input, "r")
    #filetext = file.read()
    #file.close()
    with open(input, "r") as input_handle:
        with open(output, "w") as output_handle:
            for record in SeqIO.parse(input_handle, "fasta"):
                prot_id = record.id
                prot_seq = record.seq
                prot = str(prot_seq)

                print("\n>"+prot_id+"\n", file = output_handle)
                #print(prot_seq+"\n", file = output_handle)
                #no se si imprimir tb la secuencia
                for pattern in dic:
                    accession = dic[pattern]
                    if re.search(pattern, prot):
                        with open("prosite.dat","r") as handle:
                            records = Prosite.parse(handle)
                            for record in records:
                                accession_2 = record.accession
                                if (accession_2 == accession):
                                    name = record.name
                                    description = record.description
                                    pattern_2 = record.pattern
                                    print("\tDominio: "+name+" | "+accession, file = output_handle)
                                    print("\tDescripción: "+description, file = output_handle)
                                    print("\tPatrón: "+pattern_2+"\n", file = output_handle)

            #for p in patrones:
                #if re.match(p, donde lo buscas)
    return output
