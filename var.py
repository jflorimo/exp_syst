class Var(object):

	def __init__(self, name):
		self.name = name
		self.value = 0
		self.solutions = []
		self.results = []

	#GETTER && SETTER
	def setValue(self, value):
		self.value = value

	def setSolutionQuery(self, solution):
		self.solutions.append(solution)

	def setResultQuery(self, result):
		self.results.append(result)

	def getValue(self):
		return ( self.value )

	# OPERATOR OVERLOADING
	def __add__(self, b):
		return (int(self.value) and int(b.getValue()))

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

	# METHODS
	def toString(self):
		return self.name + ": "  + str(self.value)

	def display(self):
		print(self.name + ": "  + str(self.value))
		print("  solutions:")
		for solution in self.solutions:
			print("    "+solution)
		print("  results:")
		for result in self.results:
			print("    "+result)