from datetime import datetime

class logging:
	@staticmethod
	def getLogger(message: str):
		now = datetime.now()
		print(f"{now.year}/{now.month}/{now.day} {now.hour}:{now.minute}:{now.second} - {message}")