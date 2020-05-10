import frontmatter
from os import listdir
from os.path import isfile, join
import re
import sqlite3


mypath = '/home/abhishek/Code/abhn.github.io/_posts/'


onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


date_name_separator = re.compile(r'(\d+-\d+-\d+)-([-.\w]+)')

conn = sqlite3.connect('../websites/db.sqlite3')
c = conn.cursor()


for filename in onlyfiles:
    with open(mypath + filename) as f:
        post = frontmatter.loads(str(f.read()))
        title = post.get('title')
        tags = post.get('tags')
        content = post.content
        so = date_name_separator.search(filename)
        date_created = so.group(1)
        filename = so.group(2)


        c.execute("""
            INSERT INTO nagekar_com_blogpost (title, description, content, created_at, updated_at, filename)
            VALUES (?,?,?,?,?,?)
          """, (title, title, content, date_created, date_created, filename,))

        blog_post_id = c.lastrowid


        # check if the blog post has a tag not aleady created
        if(tags and len(tags)):
            for tag in tags:
                c.execute('SELECT * FROM nagekar_com_tag WHERE name=?', (tag,))
                tag_check = c.fetchone()
                if tag_check == None:
                    c.execute("""
                        INSERT INTO nagekar_com_tag (name) 
                        VALUES(?)""", (tag,))

                    tag_id = c.lastrowid

                else:
                    print(tag_check)
                    tag_id = tag_check[0]

                c.execute("""
                    INSERT INTO nagekar_com_blogpost_tags (blogpost_id, tag_id)
                    VALUES (?,?)
                    """, (blog_post_id, tag_id))


        conn.commit()
