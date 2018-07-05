from flask import Flask
from peewee import *

app = Flask(__name__)

@app.route('/')
def index():
	return 'TEST'
	
if __name__ == '__main__':
	app.run(debug=True)
