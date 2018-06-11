import pyscopg2

class Database:
	connection = None

	def connect():
		connection = psycopg2.connect("dbname='testing_framework' user='testing_framework' host='localhost' password='password'")

	def disconnect():
		connection.close()

	def reconnect():
		disconnect();
		connect();
