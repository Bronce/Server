import mysql.connector
from mysql.connector import pooling
from mysql.connector.connection import MySQLConnection

class Database:
	def __init__(self):
		self.pool = None
		self.cursor = None
		self.connection = None

	def connect(self, pool_name: str, pool_size: int, hostname: str, user: str, password: str, database: str):
		self.pool = mysql.connector.pooling.MySQLConnectionPool(
			pool_name = pool_name,
			pool_size = int(pool_size),
			pool_reset_session = True,
			host = hostname,
			database = database,
			user = user,
			password = password
		)
		self.connection = self.pool.get_connection()
		if self.connection.is_connected():
			self.pool = self
			self.cursor = self.connection.cursor()
			return True
		else:
			return False