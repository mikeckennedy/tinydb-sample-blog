import datetime

import db


def main():
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
    res = input("Do you want to add a comment to a post? (y/n) ")
    if res != 'y':
        return

    ids = db.all_post_ids()
    try:
        pick = int(input('Choose a post id to comment upon: {}: '.format(ids)))
        comment = input("Enter your comment on a single line (enter to save):\n\n")
    except:
        print("That wasn't a good choice! (need a valid number)")
        return

    db.add_comment(pick, comment)


if __name__ == '__main__':
    main()
