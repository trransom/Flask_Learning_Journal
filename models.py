import datetime

from flask.ext.brcypt import generate_password_hash
from flask.ext.login import UserMixin
from peewee import *

DATABASE = SqliteDatabase('journal.db')

class Entry(Model):
	title = CharField(max=100)
	date = DateTimeField(default=datetime.datetime.now)
	timespent = BigIntegerField()
	learned = TextField()
	resources = TextField()
	
	class Meta:
		database = DATABASE
		order_by = ('-date',)
		
def initialize():
	DATABASE.connect()
	DATABASE.create_tables([Entry], safe=True)
	DATABASE.close()