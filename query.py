import re
import time
from var import Var

class Query(object):

	def __init__(self, left):
		self.left = left
		self.priority = {}
		self.child = 0
		self.resolver = self.createResolver(self.left)

	def op_add(self, l, r, varMap):
		return (l.op_add(r, varMap))

	def op_or(self, l, r, varMap):
		return (l.op_or(r, varMap))

	def op_xor(self, l, r, varMap):
		return (l.op_xor(r, varMap))


	def opn_add(self, l, r, varMap):
		result = Var(l.getName())

		if ( l.getValue() == 1 and r.getValue() == 0 ):
			result.setValue( 1 )
		elif ( l.getValue() == 0 or r.getValue() == 1 ):
			result.setValue( 0 )
		elif ( l.getValue() == -1 or r.getValue() == -1 ):
			result.setValue( -1 )
		else:
			result.setValue( 0 )
		return (result)

	def opn_or(self, l, r, varMap):
		result = Var(l.getName())
		if ( l.getValue() == 1 or r.getValue() == 0 ):
			result.setValue( 1 )
		elif ( l.getValue() == 0 or r.getValue() == 1 ):
			result.setValue( 0 )
		elif ( l.getValue() == -1 and r.getValue() == -1 ):
			result.setValue( -1 )
		else:
			result.setValue( 0 )
		return (result)

	def opn_xor(self, l, r, varMap):
		result = Var(l.getName())
		if ( l.getValue() == -1 or r.getValue() == -1 ):
			result.setValue( -1 )
		elif ( l.getValue() == 1 ^ r.getValue() == 0 ):
			result.setValue( 1 )
		else:
			result.setValue( 0 )
		return (result)


	def isOperator(self, string):
		operator = ['+', '|', '&', '^']
		if (string in operator):
			return (True)
		return (False)

	def createResolver( self, result ):
		resultold = result
		i = 0
		regexp = "(\((!?([A-Z]|\?)[+^|]){1,}!?([A-Z]|\?)\))"

		while ( result != re.sub(regexp, "?", result)):
			result = re.sub(regexp, "?", result)
		tmp_final = result
		resolver = {result:[]}
		result = resultold

		while ( result != re.subn(regexp, "?", result, count=1)[0] ):
			pos = re.search(regexp, result)
			tmp = result[pos.start() + 1:pos.end() - 1]
			result = re.subn(regexp, "?", result, count=1)[0]
			resolver[tmp_final].append(tmp)

		return resolver

	def run(self, varMap):
		return (self.parse_resolver(varMap, self.resolver).getValue())

	def parse_resolver(self, varMap, resolver):
		tmp = {}
		tmpVarMap = varMap
		elem = None
		self.child = 0

		for (key, value) in resolver.items():
			if (elem == None):
				elem = key
			for (i, query) in enumerate(value):
				tmp[str(self.child)] = self.calcul(query, varMap)
				self.child += 1
		for ( i, var ) in tmp.items():
			elem = str.replace(elem, "?", var.getName(), 1)
			tmpVarMap[var.getName()] = var
		return (self.calcul(elem, tmpVarMap))

	def calcul(self, query, varMap):
		l = Var(str(self.child))
		# print (str(self.child))
		l.setValue(1)
		opposite = 0
		ptr = {
				"+": self.op_add,
				"|": self.op_or,
				"^": self.op_xor,
				"!+": self.opn_add,
				"!|": self.opn_or,
				"!^": self.opn_xor
			}
		op = "+"

		for x in query:
			if ( op == None and self.isOperator(x) == True ):
				op = x
			elif ( self.isOperator(x) == False ):
				if ( x != "!" ):
					if ( opposite == 1 ):
						op = "!" + op
					val = ptr[op](l, varMap[x], varMap).getValue()
					l.setValue(val)
					opposite = 0
					op = None
				else :
					opposite = 1

		return (l)
