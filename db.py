from datetime import datetime
from pymongo import MongoClient, DESCENDING


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


def get_all_urls():
    return list(db.links.distinct('url'))


def get_last_status_log(url):
    return db.status_log.find_one({'url': url}, sort=[('date',  DESCENDING)])


def get_chats_for_url(url):

    chat_list = []

    for link in db.links.find({'url': url}):
        chat_list.append(link['chat'])

    return chat_list


def log_status(url, status_code):
    db.status_log.insert_one({'url': url, 'status_code': status_code, 'date': datetime.now()})


def get_log_list(url, limit=20):
    return db.status_log.find({url: url}).sort([('date', DESCENDING)]).limit(limit)
