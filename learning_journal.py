from flask import Flask, g

from . import models

app = Flask(__name__)

@app.route('/entries')
def load_entries():
	try:
		return models.Entry.get()
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
	app.run(debug=True)
