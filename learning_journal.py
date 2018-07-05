from flask import (Flask, g)

import models

app = Flask(__name__)


@app.route('/entries')
def load_entries():
	try:
		return models.Entry.return_entries()
	except models.DoesNotExist:
		return None
	
@app.route('/edit')
def edit():
	return 'EDIT'
	
@app.route('/delete')
def delete():
	return 'DELETE'
	
@app.route('/entry')
def entry():
	return 'ENTRY'
	
if __name__ == '__main__':
	models.initialize()
	try:
		models.Entry.create_entry(
			title='Senior Project',
			date='',
			timespent=30,
			learned='I learned about hidden Markov models',
			resources='Textblob'
		)
	except ValueError:
		pass
	app.run(debug=True)
