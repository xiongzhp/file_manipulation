# # pip install pubchempy
from numpy import random
from pubchempy import get_compounds, Compound

import csv
with open('inhibitor_all.csv', 'r') as inhibitor_all:
	reader = csv.reader(inhibitor_all, delimiter=',', quotechar='"')
	# next(reader, 5)  # skip the headers
	Inactives = [compound[2] for compound in reader if compound[3]=="Inactive"]
inhibitor_all.close()

with open('inhibitor_inactive.csv', 'w') as inhibitor_inactive:
	for inactive in Inactives:
		comp = Compound.from_cid(inactive)
		# print(comp.canonical_smiles)
		writer = csv.writer(inhibitor_inactive, delimiter=',')
		# writer.writerow(["Active", "mol_id", "smiles"])  # write header
		writer.writerow([0, inactive, comp.canonical_smiles])
	# for x in xrange(12):
	# 	Inactives = random.choice(Inactive, 3880)
