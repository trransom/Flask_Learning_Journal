from flask import (Flask, g, render_template, flash, redirect, url_for)
#from flask_login import LoginManager

import models

app = Flask(__name__)


@app.route('/entries', methods=('GET', 'POST'))
def list():
	stream = models.Entry.select().limit(100)
	return render_template('index.html', stream=stream)
	
@app.route('/details', methods=('GET', 'POST'))
def details():
	pass
	
@app.route('/')
def index():
	return 'Hey'
	
@app.route('/edit')
def edit():
	return 'EDIT'
	
@app.route('/delete')
def delete():
	return 'DELETE'
	
@app.route('/entry')
def entry():
	form = forms.EntryForm()
	if form.validate_on_submit():
		flash('You logged your entry! Keep up the good work!')
	
if __name__ == '__main__':
	models.initialize()
	try:
		models.Entry.create_entry(
			title='holder',
			date='',
			timespent=30,
			learned='I learned about hidden Markov models',
			resources='Textblob'
		)
	except ValueError:
		pass
	app.run(debug=True)
