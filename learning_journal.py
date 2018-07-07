from flask import (Flask, g, render_template, flash, redirect, url_for)
#from flask_login import LoginManager

import models
import forms

app = Flask(__name__)
app.secret_key = 'wsdgppweoi38598712e'

@app.route('/entries', methods=('GET', 'POST'))
def list():
	stream = models.Entry.select().limit(100)
	return render_template('index.html', stream=stream)
	
@app.route('/details', methods=('GET', 'POST'))
def details(entry=None):
	print("\nTitle: ", entry, "\n")
	post = models.Entry.get(models.Entry.title=='Chatbot')
	return render_template('detail.html', entry=post, title=post.title, timespent=post.timespent,
							learned=post.learned, resources=post.resources)
							
@app.route('/entry')
def add():
	form = forms.EntryForm()
	if form.validate_on_submit():
		flash('Entry submission successful!')
		models.Entry.create_entry(
			title=form.title.data,
			date=form.date.data,
			timespent=form.timespent.data,
			learned=form.learned.data,
			resources=form.resources.data
		)
		return redirect(url_for('index'))
	else: 
		print('Not working')
	return render_template('new.html', form=form)
	
@app.route('/')
def index():
	return 'Hey'
	
@app.route('/edit')
def edit(entry=None):
	form = forms.EditForm()
	if form.validate_on_submit():
		flash('Entry update successful!')
		models.Entry.edit_entry(entry, form.title.data, form.date.data,
								form.timespent.data, form.learned.data,
								form.resources.data)
	return render_template('edit.html', form=form)
	
@app.route('/delete')
def delete():
	return 'DELETE'
	
	
if __name__ == '__main__':
	models.initialize()
#	try:
#		models.Entry.create_entry(
#			title='Chatbot',
#			date='2018-01-01',
#			timespent=30,
#			learned='I learned about hidden Markov models',
#			resources='Textblob'
#		)
#	except ValueError:
#		pass
#		
#	try:
#		models.Entry.create_entry(
#			title='Python',
#			timespent=30,
#			learned='I learned about inheritance',
#			resources='Treehouse'
#		)
#	except ValueError:
#		pass
	app.run(debug=True)
