class Var(object):

	def __init__(self, name):
		self.name = name
		self.value = 0
		self.solutions = []

	#GETTER && SETTER
	def setValue(self, value):
		self.value = value

	def setSolutionQuery(self, solution):
		self.solutions.append(solution)

	def getValue(self):
		return ( self.value )

	def getName(self):
		return ( self.name )

	# OPERATOR OVERLOADING
	def __add__(self, b):
		tmp = Var(self.name)
		if (self.value == 1 and b.getValue() == 1):
			tmp.setValue(1)
		else:
			tmp.setValue(0)
		return (tmp)

	def __sub__(self, b):
		tmp = Var(self.name)
		tmp.setValue(int(self.value - ingetValue()))
		return (tmp)

	def __eq__(self, b):
		tmp = Var(self.name)
		tmp.setValue(int(self.value == i.getValue()))
		return (tmp)

	def __ne__(self, b):
		tmp = Var(self.name)
		tmp.setValue(int(self.value != i.getValue()))
		return (tmp)

	def __xor__(self, b):
		tmp = Var(self.name)
		if (self.value == 1 ^ b.getValue() == 1):
			tmp.setValue(1)
		else:
			tmp.setValue(0)
		return (tmp)

	def __or__(self, b):
		tmp = Var(self.name)
		if (self.value == 1 or b.getValue() == 1):
			tmp.setValue(1)
		else:
			tmp.setValue(0)
		return (tmp)

	# METHODS
	def toString(self):
		return self.name + ": "  + str(self.value)

	def display(self):
		print(self.name + ": "  + str(self.value))
		print("  solutions:")
		for solution in self.solutions:
			print("    "+ solution.getVar()+": "+solution.getSolution() + " => " + solution.getResult())
