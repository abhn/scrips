 from os import listdir
 from os.path import isfile, join
 onlyfiles = [f for f in listdir('./') if isfile(join('./', f))]
 
 for file in onlyfiles:
   print(file)
   if file == 'helper.py':
     continue
   
   with open(file, 'r') as myfile:
     contents = list(myfile.readlines())
 
   indices = [i for i, x in enumerate(contents) if x == "---\n"]
 
   if len(indices) < 2:
     continue
 
   ending = indices[1]
 
   contents.insert(ending, 'featured_image_alt_text: post header image\n')
   contents.insert(ending, 'featured_image_title_text: post header image\n')
 
   with open(file, 'w') as myfile:
     for item in contents:
       myfile.write(item)
