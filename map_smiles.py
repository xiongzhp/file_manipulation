from numpy import random

import csv
sid_smiles = dict()
# random_smiles = dict()
with open('inhibitor_all.smiles', 'r') as smiles:
	reader = csv.reader(smiles, delimiter=' ', quotechar='"')
	for line in reader:
		sid_smiles[line[1]] = line[0]
smiles.close()

with open('inhibitor_all.csv', 'r') as inhibitor_all:
	reader = csv.reader(inhibitor_all, delimiter=',', quotechar='"')
	# next(reader, 5)  # skip the headers
	Actives = [compound[1] for compound in reader if compound[3]=="Active"]	
inhibitor_all.close()

with open('inhibitor_all.csv', 'r') as inhibitor_all:
	reader = csv.reader(inhibitor_all, delimiter=',', quotechar='"')
	# next(reader, 5)  # skip the headers
	Inactives = [compound[1] for compound in reader if compound[3]=="Inactive"]
inhibitor_all.close()

with open('hERG.csv', 'w') as hERG:
	writer = csv.writer(hERG, delimiter=',')
	for active in Actives:
		writer.writerow([1,1,1,1,1,1,1,1,1,1,1,1, active, sid_smiles[active]])

	for x in xrange(12):
		Inactives = random.choice(Inactives, 3880)
		for inactive in Inactives:
			random_smiles = [None] * 14
			random_smiles[12] = inactive
			random_smiles[13] = sid_smiles[inactive]
			random_smiles[x] = 0	
			writer.writerow(random_smiles)
	# break
