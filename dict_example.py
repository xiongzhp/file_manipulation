test_list = []
F1 = open('hERG_test.smiles', 'r')
F2 = open('hERG_ki_canonical.csv', 'r')
O1 = open('hERG_train.csv', 'w')
O2 = open('hERG_test.csv', 'w')
for line in F1:
    line = line.rstrip()
    test_list.append(line)
F1.close()
for line in F2:
    line = line.rstrip()
    line_list = line.split(',')
    smiles = line_list[1]
    pred = line_list[0]
    if smiles in test_list:
    	# print len(smiles)
    	O2.write(pred+','+smiles+'\n')
    else:
		O1.write(pred+','+smiles+'\n')

F2.close()
O1.close()
O2.close()
