from pymongo import MongoClient


client = MongoClient('db', 27017)

db = client.httpgram


def add_url(chat, url):
    db.links.insert_one({'chat': chat, 'url': url})


def remove_url(chat, url):
    db.links.delete_one({'chat': chat, 'url': url})


def get_url_list(chat):

    links = []

    for result in db.links.find({'chat': chat}, {'_id': False, 'url': True}):
        links.append(result['url'])

    return links
