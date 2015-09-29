class Var(object):

	def __init__(self, name):
		self.name = name
		self.value = 0

	#GETTER && SETTER
	def setValue(self, value):
		self.value = value

	def getValue(self):
		return ( self.value )

	# OPERATOR OVERLOADING
	def __add__(self, b):
		return (int(self.value) + int(b.getValue()))

	def __sub__(self, b):
		return (int(self.value) - int(b.getValue()))

	def __eq__(self, b):
		return (int(self.value) == int(b.getValue()))

	def __ne__(self, b):
		return (int(self.value) != int(b.getValue()))

	def __xor__(self, b):
		return (int(self.value) ^ int(b.getValue()))

	def __or__(self, b):
		return (int(self.value) | int(b.getValue()))

