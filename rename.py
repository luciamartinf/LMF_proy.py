#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import re

def renom(dic, filename, rename):
	
	"""
		Cambia el accession por el nombre común del organismo
		  	Input = diccionario con el accession y el nombre común de los organismos,
			fichero que queremos renombrar, nombre del fichero renombrado.
	"""

	file = open(filename, "r")
	filetext = file.read()
	file.close()
	
	with open(rename, "w") as f:
		for org in dic:
			if re.search(org, filetext):
				filetext = filetext.replace(org, dic[org])
				filetext = filetext.replace("@"," | ")
		print(filetext, file = f)
		
	return rename
