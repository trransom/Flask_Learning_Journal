import datetime

from peewee import *

DATABASE = SqliteDatabase('journal.db')

class Entry(Model):
	title = CharField()
	date = DateField()
	timespent = IntegerField()
	learned = TextField()
	resources = TextField()
	
	class Meta:
		database = DATABASE
		order_by = ('-date',)
		
	@classmethod
	def create_entry(cls, title, date, timespent, learned, resources):
		try:
			with DATABASE.transaction():
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
	def edit_entry(cls, prev_title, title, date, timespent, learned, resources):
		d = cls.get(cls.title == prev_title)
		d.delete_instance()
		cls.create_entry(title, date, timespent, learned, resources)
		
	@classmethod
	def delete_entry(cls, title):
		delete = cls.get(cls.title == title)
		delete.delete_instance()
			
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