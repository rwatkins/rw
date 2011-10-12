from flask import render_template
from datetime import datetime
from rw import app

@app.route('/')
def home():
    return render_template('home.html', decades=getAgeInDecades()) 

#@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

def getAgeInDecades():
    date0 = datetime(1988, 5, 26, 23, 20)
    today = datetime.now()
    delta = today - date0
    num_decades = (delta.days / (365.2425)) / 10
    return num_decades
