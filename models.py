import datetime

from peewee import *
from flask.ext.login import UserMixin

DATABASE = SqliteDatabase('journal.db')

class Entry(UserMixin, Model):
	title = CharField(max=100)
	date = DateTimeField(default=datetime.datetime.now)
	timespent = BigIntegerField()
	learned = TextField()
	resources = TextField()
	
	class Meta:
		database = DATABASE