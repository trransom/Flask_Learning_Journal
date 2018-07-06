import datetime

from peewee import *

DATABASE = SqliteDatabase('journal.db')

class Entry(Model):
	title = CharField()
	date = DateField()
	timespent = BigIntegerField()
	learned = TextField()
	resources = TextField()
	
	class Meta:
		database = DATABASE
		order_by = ('-date',)
		
	@classmethod
	def create_entry(cls, title, date, timespent, learned, resources):
		try:
			cls.create(
				title=title,
				date=date,
				timespent=timespent,
				learned=learned,
				resources=resources
			)
		except IntegrityError:
			raise ValueError('Entry already exists')
			
	@classmethod
	def return_entries(cls):
		return Entry.select()
		
	@classmethod
	def return_date(cls):
		return cls.date
		
		
def initialize():
	DATABASE.connect()
	DATABASE.create_tables([Entry], safe=True)
	DATABASE.close()