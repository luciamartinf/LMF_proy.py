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
import shutil



def main():
    
    """
        Función principal del proyecto. 
        Coge de primer argumento el nombre de la carpeta donde se encuentra los genbank 
        y de segundo argumento el fichero con las query. #puede que este todo en la misma carpeta
    """
    #[1] secuencias_y_... es una carpeta, igual hago que haya una opción para que no se tenga que introducir necesariamente una carpeta y se pueda introducir simplemente un fichero gb
    #[2] PBPs_query.fa

    name_proy = input("Nombre del proyecto (sin blancos): ")
    os.mkdir(name_proy)
    
    results = "{}/resultados".format(name_proy)
    os.mkdir(results)

    secuencias_fasta = "{}/secuencias.fasta".format(name_proy)

    dic_dominios = create_dic_dominios()
    dic_org = {}
    
    
    carpeta = sys.argv[1]

    for gbks in os.listdir(carpeta): #esto puede ser una función, open_carpeta
        
        file = os.path.join(carpeta,gbks)
        
        if os.path.isfile(file) == True:
            try:
                gbk_to_fasta(file, secuencias_fasta)
                create_dic_org(file, dic_org)
            except:
                pass
            

    querys = sys.argv[2]

    with open(querys, "r") as query_handle:  #esto puede ser una función
        
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

                        
            input_muscle = "{}/muscle_{}.fa".format(folder, id)
            prep_muscle(output_blast, query, input_muscle)
            
            rename_muscle = "{}/muscle_{}_rn.fa".format(folder, id)
            renom(dic_org, input_muscle, rename_muscle)

            
            align = "{}/align_{}.fa".format(folder, id)
            muscle(input_muscle, align)
            
            rename_align = "{}/align_{}_rn.fa".format(folder, id)
            renom(dic_org, align, rename_align)

            
            tree = "{}/tree_{}.nw".format(folder, id)
            muscle_tree(align, tree)
            
            rename_tree = "{}/tree_{}_rn.nw".format(folder, id)
            renom(dic_org, tree, rename_tree)

            
            dominios = "{}/dominios_{}.txt".format(folder, id)
            search_pattern(dic_dominios, input_muscle, dominios)
            
            rename_dominios = "{}/dominios_{}_rn.txt".format(folder, id)
            renom(dic_org, dominios, rename_dominios)

            
            
    return rename_dominios



if __name__=="__main__":
    main()
