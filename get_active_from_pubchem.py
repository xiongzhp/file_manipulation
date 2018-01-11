# # pip install pubchempy
from numpy import random
from pubchempy import get_compounds, Compound
# comp = Compound.from_cid(6602565)
# print(comp.isomeric_smiles)
# comps = get_compounds('Aspirin', 'name')
# print(comps[0].xlogp)
# # 1.2

import csv
with open('inhibitor_all.csv', 'r') as inhibitor_all:
	reader = csv.reader(inhibitor_all, delimiter=',', quotechar='"')
	# next(reader, 5)  # skip the headers
	Actives = [compound[2] for compound in reader if compound[3]=="Active"]
inhibitor_all.close()

with open('inhibitor_active.csv', 'w') as inhibitor_active:
	for active in Actives:
		comp = Compound.from_cid(active)
		# print(comp.canonical_smiles)
		writer = csv.writer(inhibitor_active, delimiter=',')
		# writer.writerow(["Active", "mol_id", "smiles"])  # write header
		writer.writerow([1, active, comp.canonical_smiles])
print(len(Actives))
	# break
