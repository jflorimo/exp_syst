import re
import time
from var import Var

class Query(object):

	def __init__(self, left):
		self.left = left
		self.priority = {}
		self.child = 0
		self.resolver = self.createResolver(self.left)

	def findSubQuery( self, result ) :
		regexp = "(\((!?([A-Z]|\?)[+^|]){1,}!?([A-Z]|\?)\))"
		pos = re.search(regexp, result)
		if (pos == None):
			return False
		tmp = result[pos.start():pos.end()]
		if tmp.find("?") > 0 :
			return (True)
		return False

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

	def isOperator(self, str):
		operator = ['+', '|', '&', '^', '-']
		if (str in operator):
			return (True)
		return (False)

	def run(self, varMap):
		return (self.parse_resolver(varMap, self.resolver).getValue())

	def parse_resolver(self, varMap, resolver):
		tmp = {}
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
		return (self.calcul(elem, tmp))

	def op_add(self, l, r):
		return (l + r)

	def op_or(self, l, r):
		return (l | r)

	def op_xor(self, l, r):
		return (l ^ r)

	def calcul(self, query, varMap):
		l = Var(str(self.child))
		l.setValue(1)
		ptr = {
				"+": self.op_add,
				"|": self.op_or,
				"^": self.op_xor
			}
		op = "+"
		for x in query:
			if ( op == None and self.isOperator(x) == True ):
				op = x
			elif ( self.isOperator(x) == False ):
				l.setValue(ptr[op](l, varMap[x]).getValue())
				op = None
		return (l)
