import datetime

import db


def print_welcome():
    print("Run this program (on Python 3) to exercise TinyDb")
    print("Requirements are in requirements.txt, ujson optional")
    print("Data will be stored in ./data/smallish_blog_db.json")
    print("by Michael Kennedy (@mikeckennedy on Github)")
    print()


def main():
    print_welcome()
    add_two_posts()
    show_posts()
    add_comment()


def add_two_posts():
    if db.all_posts():
        print("test data exists, no inserts...")
        return

    db.insert_post({
        'name': 'Getting started with TinyDB',
        'created': str(datetime.datetime(year=2016, month=5, day=1)),
        'comments': []
    })
    db.insert_post({
        'name': 'Smallish embedded databases',
        'created': str(datetime.datetime(year=2016, month=6, day=2)),
        'comments': []
    })


def show_posts():
    print("Your blog contents:")
    for p in db.all_posts():
        print(" * {} [id: {}]".format(p.get('name'), p.eid))
        comments = p.get('comments', [])
        print("      {} comments".format(len(comments)))
        for c in comments:
            print("      -- {}".format(c))


def add_comment():
    res = input("Want to add a comment? (y/n) ")
    if res != 'y':
        print("OK, no comment.")
        return

    ids = db.all_post_ids()
    # noinspection PyBroadException
    try:
        pick = int(input('Choose a post to comment upon: {}'.format(ids)))
        comment = input("Enter your comment on a single line (enter to save):\n\n")
    except:
        print("That wasn't a good choice! (need a valid number)")
        return

    db.add_comment(pick, comment)


if __name__ == '__main__':
    main()
