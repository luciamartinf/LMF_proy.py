#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import re

def renom(dic, filename, rename):
	
	"""
		Cambia el accession por el nombre común del organismo con la ayuda
		de un diccionario con el accession y el nombre común de los organismos.
		El resultado se guarda en un fichero diferente. 
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
