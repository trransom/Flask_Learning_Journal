from peewee import *
from flask.ext.login import UserMixin

DATABASE = SqliteDatabase('journal.db')

class Entry(UserMixin, Model):
	
	
	class Meta:
		database = DATABASE