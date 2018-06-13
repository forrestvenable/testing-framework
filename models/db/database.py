import psycopg2
from models import element, webpage


connection = None

def connect():
	global connection
	connection = psycopg2.connect("dbname='testing_framework' user='testing_framework' host='localhost' password='password'")

def disconnect():
	global connection
	connection.close()
	connection = None
