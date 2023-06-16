#!/usr/bin/python3

import csv
import re

with open ('100.csv', newline='') as f:
	reader = csv.reader(f, delimiter=",")
	for row in reader:
		print('------ Neue Zeile ------')
		for col in row:
			if re.search('[a-zA-Z0-9]+',col):
				print('Zelle: ' + str(col))