from error import exit_error

class Var(object):

	def __init__(self, name):
		self.name = name
		self.value = 0
		self.alreadyCalculated = False
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
	def op_add(self, b, varMap):
		tmp = Var(self.name)
		if (self.searchValue(varMap) == 1 and b.searchValue(varMap) == 1):
			tmp.setValue(1)
		else:
			tmp.setValue(0)
		return (tmp)

	def op_xor(self, b, varMap):
		tmp = Var(self.name)
		if (self.searchValue(varMap) == 1 ^ b.searchValue(varMap) == 1):
			tmp.setValue(1)
		else:
			tmp.setValue(0)
		return (tmp)

	def op_or(self, b, varMap):
		tmp = Var(self.name)
		if (self.searchValue(varMap) == 1 or b.searchValue(varMap) == 1):
			tmp.setValue(1)
		else:
			tmp.setValue(0)
		return (tmp)

	# METHODS
	def toString(self):
		return self.name + ": "  + str(self.value)

	def display(self):
		print(self.name + ": "  + str(self.value))
		# print("  solutions:")
		# for solution in self.solutions:
		# 	print("    "+ solution.getVar()+": "+solution.getSolution() + " => " + solution.getResult())

	def searchValue( self, varMap ):
		tmpResult = []
		if ( self.alreadyCalculated == True or self.value == 1 ):
			self.alreadyCalculated = True
			return (self.value)

		for (i, solution) in enumerate(self.solutions):
			tmpResult.append(solution.calculValue(varMap))

		result = -1
		for (i, solution) in enumerate(tmpResult):
			if ( result == -1 ):
				result = solution
			elif ( result != solution and solution != -1 ):
				exit_error("Regles incoherante concernant " + self.name)
			elif ( solution != -1 ) :
				result = solution
		self.alreadyCalculated = True
		self.value = result
		return (result)


