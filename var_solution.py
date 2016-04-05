import re
from query import Query

class VarSolution(object):

	def __init__(self, solution, right, var):
		self.solution = solution
		self.right = right
		self.var = var

	#GETTER && SETTER
	def getSolution(self):
		return ( self.solution )
	def getResult(self):
		return ( self.right )
	def getVar(self):
		return ( self.var )

	def calculValue( self, varMap ):
		undetermined = "!?[A-Z][|^]"
		composite = "!?[A-Z]\+"

		if ( re.search(undetermined, self.right) != None ):
			return ( -1 )

		query = Query( self.solution )
		result = query.run(varMap)
		if ( re.search(composite, self.right) != None and result != 1 ):
			return ( -1 )
		elif (self.right.find( "!" + self.var ) != -1 and result != -1):
			return ( 0 if result == 1 else 1 )
		return (result)

