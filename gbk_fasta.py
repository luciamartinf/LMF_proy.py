#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-


import sys
from Bio import Seq
from Bio import SeqIO


#input = sys.argv[1]
#os.listdir()

def gbk_to_fasta(input_gbk, output_gbk):

	with open(input_gbk, "r") as input_handle:
		for record in SeqIO.parse(input_handle, "genbank"):
			org = record.id

		with open(output_gbk, 'a') as fasta:
			for feature in record.features:

				if feature.type == 'CDS':
					try:
						locus_tag = feature.qualifiers['locus_tag'][0]
					except:
						locus_tag = "NA"
					try:
						protein = feature.qualifiers['translation'][0]
					except:
						protein = "NA"

					#print(">"+prot_id+"|"+name+"\n"+protein+"\n", file=fasta)
					print(">{}@{}\n{}\n".format(locus_tag,org,protein),
						  file=fasta)

	#print(dic_org)
	return output_gbk

def create_dic_org(input_gbk, dic_org):
	with open(input_gbk, "r") as input_handle:
		for record in SeqIO.parse(input_handle, "genbank"):

			org = record.id
			description = record.description
			division = description.split("PCC") #estas secuencias en concreeto tienen el PCC pero no suele ser asi
			org_name = division[0]
			if not org in dic_org.keys():
				dic_org[org] = org_name

	return dic_org

#gbk_to_fasta(input)
#gbk_to_fasta(sys.argv[1],sys.argv[1]+".2")
#create_dic_org(input)
