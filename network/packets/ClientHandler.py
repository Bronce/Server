from Main import *
from network.packets.ByteArray import *

class ClientHandler:
	def __init__(self, session: object, request: object):
		self.session = session
		self.request = request

		self.incomplete = {}

	def parse(self, data: bytes):
		codec = ByteArray(data)
		size = codec.readByte()
		if size == 1:
			length = codec.readUnsignedByte()
		elif size == 2:
			length = codec.readUnsignedShort()
		else:
			length = ((codec.readUnsignedByte() & 0xFF) << 16) | ((codec.readUnsignedByte() & 0xFF) << 8) | (codec.readUnsignedByte() & 0xFF)
		if length != 0:
			data_id = codec.readByte()
			if codec.size() == length:
				if codec.size() >= 2:
					self.findPackage(codec)
				elif codec.size() < length:
					self.putIncomplete(data)
				elif codec.size() > length:
					return
		return

	def findPackage(self, codec: object):
		c_int = codec.readShort()
		Main.get_logger(f"Recv -> ({c_int}) : ({c_int >> 8}, {c_int & 255}) -> {repr(codec.toByteArray())}")
		for packet, c_value in self.session.socket_manage.game_manager.packet_manager.packets_list.items():
			if c_value == c_int:
				packet.handle(self.session, codec)

	def putIncomplete(self, data: bytes):
		self.incomplete[self.session.address] = data