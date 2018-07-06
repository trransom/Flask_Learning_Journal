from flask_wtf import Form
import datetime

from models import Entry

class EntryForm(Form):
	title=StringField(
		'Title',
		validators=[DataRequired()]
		)
	date=DateTimeField(
		'Date',
		validators=[DataRequired()]
	)
	timespent=BigIntegerField(
		'Time Spent',
		validators=[DataRequired()]
	)
	learned=TextField(
		'Learned',
		validators=[DataRequired()]
	)
	resources=TextField(
		'Resources Used'
		validators=[DataRequired()]
		)