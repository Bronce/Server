# coding: utf-8
import time
import threading
# logging module
from log.logging import *
# game modules
from game.GameManager import *
# database module
from database.Database import *
# socket module
from network.socket.SocketServer import *
# config module
from configuration.Configuration import *

class Main:
	def __init__(self):
		self.end_time = 0
		self.start_time = 0

		self.game_manager = None
		self.socket_thread = None

	def main(self):
		self.start_time = round(time.time() * 1000)
		Main.get_logger("Starting all systems...")
		self.game_manager = GameManager()
		Main.get_logger("Getting configuration.")
		self.game_manager.config = Configuration()
		self.game_manager.config.load()
		Main.get_logger("Connecting to MySQL.")
		self.game_manager.pooling = Database()
		self.game_manager.pooling.connect(
			self.game_manager.config.get_value("database", "db.poolname"),
			self.game_manager.config.get_value("database", "db.poolsize"),
			self.game_manager.config.get_value("database", "db.hostname"),
			self.game_manager.config.get_value("database", "db.user"),
			self.game_manager.config.get_value("database", "db.password"),
			self.game_manager.config.get_value("database", "db.database")
		)
		Main.get_logger("Opening socket system.")
		self.game_manager.socket = SocketServer(self.game_manager, (self.game_manager.config.get_value("socket", "socket.host"), int(self.game_manager.config.get_value("socket", "socket.port"))))
		self.socket_thread = threading.Thread(target=self.game_manager.socket.serve_forever, args=())
		self.socket_thread.start()
		self.end_time = round(time.time() * 1000) - self.start_time
		Main.get_logger(f"Emulator started with {self.end_time}ms.\n")

	@staticmethod
	def get_logger(message: str):
		logging.getLogger(message)

if __name__ == "__main__":
	main = Main()
	main.main()