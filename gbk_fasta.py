#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# Author: Lucía Martín Fernández, jun 2020


import sys
from Bio import Seq
from Bio import SeqIO
import os



def gbk_to_fasta(input_gbk, output_gbk):

	"""
		A partir de un fichero tipo genbank crea otro tipo fasta con el locus_tag,
		el organismo y la secuencia de aminoácidos de las proteínas del genbank.
	"""

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

					print(">{}@{}\n{}\n".format(locus_tag, org, protein),
					      file = fasta)


	return output_gbk



def create_dic_org(input_gbk, dic_org):

	"""
		Crea un diccionario con el accession y el nombre común de los organismos
		de los genbank
	"""

	with open(input_gbk, "r") as input_handle:

		for record in SeqIO.parse(input_handle, "genbank"):

			org = record.id
			description = record.description

			division = description.split(" ")
			org_name = str(division[0]) + " " + str(division[1])

			if not org in dic_org.keys():
				dic_org[org] = org_name


	return dic_org


def lee_carpeta(carpeta, secuencias_fasta):
	
	"""
		Lee la carpeta con los genomas bacterianos e intenta 
		ejecutar las funciones gbk_to_fasta y create_dic_org 
		por cada genbank que encuentra. 
	"""

	dic_org = {}

	for gbks in os.listdir(carpeta):

		file = os.path.join(carpeta, gbks)

		if os.path.isfile(file) == True:
			try:
				gbk_to_fasta(file, secuencias_fasta)
				dic_org = create_dic_org(file, dic_org)
			except:
				pass

	return dic_org
