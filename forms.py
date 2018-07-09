from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, TextField
from wtforms.validators import DataRequired, Regexp, ValidationError
import datetime

from models import Entry

def title_exists(form, field):
	if Entry.select().where(Entry.title == field.data).exists():
		raise ValidationError('This title already exists')
		
		
class EntryForm(FlaskForm):
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
		validators=[
			DataRequired(),
			Regexp(
				r'^[0-9]+$',
				message=('Time spent should only be entered as digits.')
			)
			]
	)
	learned=TextField(
		'Learned',
		validators=[DataRequired()]
	)
	resources=TextField(
		'Resources Used',
		validators=[DataRequired()]
		)