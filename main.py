#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import sys
import os
from Bio import Seq
from Bio import SeqIO
from gbk_fasta import gbk_to_fasta, create_dic_org
from blastp import blast
from muscle import muscle, prep_muscle, muscle_tree
from rename import renom
from myprosite import create_dic_dominios, search_pattern
#from tree import tree

def main():
    carpeta = sys.argv[1] #secuencias_y_...
    querys = sys.argv[2] #PBPs_query.fa

    dic_dominios = create_dic_dominios()

    i=1
    while True :
        secuencias_fasta = "secuencias_{}.fasta".format(i)

        if not os.path.isfile(secuencias_fasta):
            break
        i+=1

    dic_org = {}

    for gbks in os.listdir(carpeta):
        file = os.path.join(carpeta,gbks)
        if os.path.isfile(file) == True:
            try:
                gbk_to_fasta(file, secuencias_fasta)
                create_dic_org(file, dic_org)
            except:
                pass
    #return secuencias.fasta = output_gbk
    #output_gbk = "secuencias_{}.fasta".format(i)

    with open(querys, "r") as query_handle:
        for record in SeqIO.parse(query_handle, "fasta"):
            seq = record.seq
            id = record.id
            query = "{}.fasta".format(id)
            output_blast = "blast_{}.tsv".format(id)
            with open(query, "w") as q:
                print(">{}\n{}\n".format(id,seq), file=q)
            try:
                cov = sys.argv[3]
                ident = sys.argv[4]
                blast(query, secuencias_fasta, output_blast, cov, ident)
            except:
                try:
                    ident = sys.argv[4]
                    blast(query, secuencias_fasta, output_blast, ident)
                except:
                    try:
                        cov = sys.argv[3]
                        blast(query, secuencias_fasta, output_blast, cov)
                    except:
                        blast(query, secuencias_fasta, output_blast)

            input_muscle = "muscle_{}.fa".format(id)
            prep_muscle(output_blast, query, input_muscle)
            rename_muscle = "muscle_{}_rn.fa".format(id)
            renom(dic_org, input_muscle, rename_muscle)

            align = "align_{}.fa".format(id)
            muscle(input_muscle, align)
            rename_align = "align_{}_rn.fa".format(id)
            renom(dic_org, align, rename_align)

            tree = "tree_{}.nw".format(id)
            muscle_tree(align, tree)
            rename_tree = "tree_{}_rn.nw".format(id)
            renom(dic_org, tree, rename_tree)

            dominios = "dominios_{}.txt".format(id)
            search_pattern(dic_dominios, input_muscle, dominios)
            rename_dominios = "dominios_{}_rn.txt".format(id)
            renom(dic_org, dominios, rename_dominios)

    return rename_dominios

if __name__=="__main__":
    main()
