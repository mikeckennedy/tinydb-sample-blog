import os

import tinydb
from tinydb import TinyDB

db_folder = os.path.join(os.path.dirname(__file__))
db_file = os.path.join(db_folder, 'data', 'smallish_blog_db.json')
the_db = TinyDB(db_file)


def insert_post(post):
    table = the_db.table('posts')
    res = table.insert(post)
    print("Inserted post: {} <-- {}".format(res, post))


def all_posts():
    table = the_db.table('posts')
    return table.all()


def all_post_ids():
    return [
        p.eid
        for p in all_posts()
        ]


def add_comment(post_eid, comment_text):
    posts = the_db.table('posts')
    post = posts.get(eid=post_eid)
    print("Adding comment to post: {}".format(post.get('name')))
    post['comments'].append(comment_text)

    posts.update(post, eids=[post.eid])
