from Field import *
from Database import Database
from Model import Model

Model.db = Database('database.sqlite')
Model.connection = Model.db.connect()

class Post(Model):
    title = 'VARCHAR(255)'
    body = 'TEXT'
    created_at = 'TIMESTAMP'
    published = 'INTEGER'

class User(Model):
    first_name = 'VARCHAR(255)'
    last_name = 'VARCHAR(225)'
    age = 'INTEGER'

if __name__ == '__main__':
    post = Post()
