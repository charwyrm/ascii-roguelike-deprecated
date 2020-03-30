class Line():
	def __init__(self, length):
		self.length = length
		self.text = []

	def add_char(self, char):
		if char == '\r':
			temp = "".join(self.text)
			self.text = []
			return temp
		elif char == '\x08':
			if len(self.text) > 0:
				self.text.pop()
				return None
		else:
			self.text.append(char)
			return None

	def get_text(self):
		return (self.text)

	def set_text(self, text):
		self.text = text.split()
	
	def set_chars(self, chars):
		self.text = chars
