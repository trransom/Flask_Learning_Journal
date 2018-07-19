from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, TextField
from wtforms.validators import DataRequired, Regexp, ValidationError
import datetime

from models import Entry

def title_exists(form, field):
	'''Tests to see if title exists in journal.'''
	if Entry.select().where(Entry.title == field.data).exists():
		raise ValidationError('This title already exists')
		
		
class EntryForm(FlaskForm):
	'''Form to create an entry.'''
	title=StringField(
		'Title',
		validators=[DataRequired(), title_exists]
		)
	date=DateField(
		'Date',
		validators=[DataRequired()]
	)
	timespent=IntegerField(
		'Time Spent (in hours)',
		validators=[DataRequired()]
	)
	learned=TextField(
		'Learned',
		validators=[DataRequired()]
	)
	resources=TextField(
		'Resources Used',
		validators=[DataRequired()]
		)
		
class EditForm(FlaskForm):
	'''Form to edit an entry.'''
	title=StringField(
		)
	date=DateField(
	)
	timespent=IntegerField(
	)
	learned=TextField(
	)
	resources=TextField(
		)
		