import socketserver
from network.socket.SocketClient import *

class SocketServer(socketserver.TCPServer):
	def __init__(self, game_manager: object, address: list):
		self.game_manager = game_manager

		self.sockets_list = {}

		socketserver.TCPServer.__init__(
			self, 
			address,
			SocketClient
		)
		return

	def server_activate(self):
		socketserver.TCPServer.server_activate(self)
		return

	def serve_forever(self, poll_interval=0.5):
		socketserver.TCPServer.serve_forever(self, poll_interval)
		return

	def handle_request(self):
		return socketserver.TCPServer.handle_request(self)

	def verify_request(self, request: object, address: list):
		return socketserver.TCPServer.verify_request(
			self, 
			request, 
			address,
		)

	def process_request(self, request: object, address: list):
		return socketserver.TCPServer.process_request(
			self, 
			request, 
			address,
		)

	def server_close(self):
		return socketserver.TCPServer.server_close(self)

	def finish_request(self, request: object, address: list):
		return socketserver.TCPServer.finish_request(
			self, 
			request, 
			address,
        )

	def close_request(self, request_address):
		return socketserver.TCPServer.close_request(
            self, 
			request_address,
        )

	def shutdown(self):
		return socketserver.TCPServer.shutdown(self)