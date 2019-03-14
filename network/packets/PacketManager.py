import glob
import pkgutil
import importlib

class PacketManager:
	def __init__(self, game_manage: object):
		self.game_manage = game_manage

		self.packets_list = {}

	def load(self):
		for dic in glob.glob("./network/messages/incoming/*/"):
			for (module_loader, name, ispkg) in pkgutil.iter_modules([dic]):
				module = dic.replace("/", ".")
				module = module.replace("..", "")
				module = module + name
				module = "" + module + ""
				module = importlib.import_module(module)
				module = getattr(module, name)
				module = module()
				self.packets_list[module] = module.int_c