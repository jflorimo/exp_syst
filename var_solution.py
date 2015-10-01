class VarSolution(object):

	def __init__(self, solution, result, var):
		self.solution = solution
		self.result = result
		self.var = var

	#GETTER && SETTER
	def getSolution(self):
		return ( self.solution )
	def getResult(self):
		return ( self.result )
	def getVar(self):
		return ( self.var )

