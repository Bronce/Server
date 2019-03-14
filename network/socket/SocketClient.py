import socketserver
from network.packets.ClientHandler import *

class SocketClient(socketserver.BaseRequestHandler):
	def __init__(self, request: object, address: list, socket_manage: object):
		self.request = request
		self.address = address
		self.socket_manage = socket_manage

		self.client_handler = ClientHandler(self, self.request)

		self.disconnected = False

		socketserver.BaseRequestHandler.__init__(
			self, 
			self.request,
			self.address,
			self.socket_manage
		)
		return

	def setup(self):
		self.socket_manage.sockets_list[self.address] = self
		return socketserver.BaseRequestHandler.setup(self)

	def handle(self):
		while True:
			if self.disconnected:
				break
			else:
				data = self.request.recv(1024)
				if len(data) != 0:
					if data == b'<policy-file-request/>\x00':
						self.request.send(b''
							+ '<cross-domain-policy>'
							+ '<allow-access-from domain=\"*\" to-ports=\"*\"/>'
							+ '</cross-domain-policy>'
						)
						self.request.close()
					else:
						self.client_handler.parse(data)
		return

	def finish(self):
		self.disconnected = False
		return socketserver.BaseRequestHandler.finish(self)