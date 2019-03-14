import configparser

class Configuration:
	def __init__(self):
		self.config = None

	def load(self):
		self.config = configparser.ConfigParser()
		self.config.read("./configuration/config.config")

	def get_option(self, key: str):
		return self.config.options(key)

	def get_value(self, key: str, value: str):
		return self.config.get(key, value)