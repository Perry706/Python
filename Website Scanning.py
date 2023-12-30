import requests
from pyecharts.charts import Line
from bs4 import BeautifulSoup
from flask import Flask
from datetime import timedelta
from flask import request, session

r = requests.get('https://realpython.github.io/fake-jobs/')
page = requests.get('https://realpython.github.io/fake-jobs/')
soup = BeautifulSoup(page.text, 'html.parser')

app = Flask(__name__)
app.secret_key = "secret key"
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=30)

DNT_TRACK = True #False
IGNORE_IPS = set(['127.0.0.1'])

def is_tracking_allowed():
	#print(request.headers)
	if 'DNT' in request.headers and request.headers['DNT'] == 1:
		return False
	if request.remote_addr in IGNORE_IPS:
		return False
	return True

def track_session():
	if 'track_session' in session and session['track_session'] == True:
		return True
	else:
		return False
print(r.url)
print(r.status_code)