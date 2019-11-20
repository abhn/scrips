import os
days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat']
divs = ['A', 'B']
branches = ['SE', 'TE', 'BE']
def create():
	for k in range(3):
		os.system("mkdir " + branches[k])
		os.system("cd " + branches[k])
		for j in range(2):
			main = branches[k] + "_" + divs[j] + "_main.java"
			file = open(main, 'w+)
			file.close()
			for i in range(6):
				name = branches[k] + "_" + divs[j] + "_" + days[i] + ".java"
				file = open(name, 'w+')
				file.close()
				print name
		os.system("cd ..")		
create()
