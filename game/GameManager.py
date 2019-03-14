from network.packets.PacketManager import *
from game.users.PlayerManager import *
from game.sessions.SessionManager import *

class GameManager:
	def __init__(self):
		self.session_manager = SessionManager(self)
		self.player_manager = PlayerManager(self)
		self.packet_manager = PacketManager(self)
		self.packet_manager.load()
		
		self.config = None
		self.socket = None
		self.pooling = None