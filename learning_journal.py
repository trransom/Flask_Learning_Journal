from flask import (Flask, g, render_template, flash, redirect, url_for, request)

import models
import forms

app = Flask(__name__)
app.secret_key = 'wsdgppweoi38598712e'

@app.before_request
def before_request():
	'''Connect to the database before each request.'''
	g.db = models.DATABASE
	g.db.connect()
	
@app.after_request
def after_request(response):
	'''Close the database connection after each request.'''
	g.db.close()
	return response

@app.route('/entries', methods=('GET', 'POST'))
def list():
	'''Lists all of the journal entries'''
	stream = models.Entry.select().limit(100)
	return render_template('index.html', stream=stream)
	
@app.route('/details/<title>')
def details(title):
	'''Displays the details of the selected entry'''
	post = models.Entry.get(models.Entry.title==title)
	return render_template('detail.html', entry=post)
	
@app.route('/entry', methods=['GET', 'POST'])
def add():
	'''Allows the user to add a journal entry'''
	form = forms.EntryForm()
	if form.validate_on_submit():
		flash('Entry submission successful!', 'success')
		models.Entry.create_entry(
			title=form.title.data,
			date=form.date.data,
			timespent=form.timespent.data,
			learned=form.learned.data,
			resources=form.resources.data
		)
		return redirect(url_for('list'))
	else:
		flash('Failed!')
	print(form.errors)
	return render_template('new.html', form=form)
	
@app.route('/')
def index():
	'''Redirects to list url'''
	return redirect(url_for('list'))
	
@app.route('/edit/<entry_title>', methods=['GET', 'POST'])
def edit(entry_title):
	'''Allows user to edit a journal entry'''
	post = models.Entry.get(models.Entry.title==entry_title)
	form = forms.EditForm(obj=post)
	if form.validate_on_submit():
		flash('Entry update successful!', 'success')
		models.Entry.edit_entry(
			entry_title, 
			form.title.data, 
			form.date.data,
			form.timespent.data, 
			form.learned.data,
			form.resources.data
			)
		return redirect(url_for('list'))
	else:
		flash('Failed!')
	print(form.errors)
	return render_template('edit.html', form=form)
	
@app.route('/delete/<title_del>')
def delete_inst(title_del):
	'''Allows the user to delete a journal entry'''
	models.Entry.delete_entry(title_del)
	flash('Successfully deleted!')
	return redirect(url_for('list'))
	
if __name__ == '__main__':
	models.initialize()
	app.run(debug=True)
