 import frontmatter
 from os import listdir
 from os.path import isfile, join
 import re
 
 mypath = '/Users/abhisheknagekar/Code/python/_posts/'
 
 onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
 
 #with open('./_posts/'+onlyfiles[0]) as f:
 #    post = frontmatter.loads(str(f.read()))
 #    print(post['title'])
 #
 
 count = 0
 for filename in onlyfiles:
     with open('./_posts/' + filename) as f:
         post = frontmatter.loads(str(f.read()))
         #if 'permalink' in post.keys():
         #    print('skipping: '+post['title'])
         #    count += 1
         #    continue
         #post_title = filename[11:-3]
         #post_title = re.sub(r'-{2,}', '-', post_title)
         #post['permalink'] = '/en/blog/:categories/'+post_title
         #print('writing to: '+post_title)
         #if 'thumbnail_image_path' in post.keys():
         #    del post['thumbnail_image_path']
         if post['permalink'][-1] is not '/':
             count += 1
             print(post['permalink'])
             post['permalink'] += '/'
             with open('./_posts_output/' + filename, 'w+') as g:
                 g.write(frontmatter.dumps(post))
 
 print('count: '+str(count))
 
 #print(onlyfiles)
