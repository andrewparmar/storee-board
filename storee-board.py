# !/usr/bin/env python

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
	'''
	Return an html template of list of movies from debug
	'''
	return render_template('movies.html')


if __name__ == '__main__':
    # app.secret_key = 'xvmZcviLG0U8z77LxgKHmgAO'
    app.debug = True
    app.run(host = '0.0.0.0', port=5000)