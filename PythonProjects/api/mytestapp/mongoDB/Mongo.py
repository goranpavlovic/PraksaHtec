__author__ = 'vladimir'


from mongoengine import *
from pymongo import MongoClient

client = MongoClient()

# db = client.primer
db = client['user-db']

coll = db.dataset

print(coll)


class UserFirst(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


class User(Document):
    name = StringField()

    # meta = {"db_alias": "user-db"}


class Book(Document):
    name = StringField()

    # meta = {"db_alias": "book-db"}


class AuthorBooks(Document):
    author = ReferenceField(User)
    book = ReferenceField(Book)

    # meta = {"db_alias": "users-books-db"}

