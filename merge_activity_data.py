import tarfile
import os
with open('all_activities.txt', 'w') as fout:
	for filename in os.listdir('All_Datasets'):
		filename = 'All_Datasets/'+filename
		print filename
		try:
			tar = tarfile.open(filename)
			files = tar.getmembers()
			f = tar.extractfile(files[1])
			fout.write(f.read())
			f.close()
		except Exception as e:
			print e
			pass			
fout.close()

