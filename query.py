import re
import time
from var import Var

class Query(object):

	def __init__(self, left):
		print (left)
		self.left = left
		self.priority = {}
		self.resolver = self.createResolver(self.left)
		print (self.resolver)

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
			# sub = result
			# while (self.findSubQuery(sub)) :
			# 	pos = re.search(regexp, result)
			# 	tmp = {result[pos.start() + 1:pos.end() - 1]: [tmp]}
			# 	sub = result[pos.start() + 1:pos.end() - 1]
				# result = result[:pos.start()] + "?" + result[pos.end():]

			resolver[tmp_final].append(tmp)
		return resolver

	def isOperator(self, str):
		operator = ['+', '|', '&', '^', '-']
		if (str in operator):
			return (True)
		return (False)

	def run(self, varMap):
		self.parse_resolver(varMap, self.resolver)

	def parse_resolver(self, varMap, resolver):
		for (key, value) in resolver.items():
			for (i, query) in enumerate(value):
				print(self.calcul(query, varMap).getValue())

	def op_add(self, l, r):
		return (l + r)

	def op_or(self, l, r):
		return (l | r)

	def op_xor(self, l, r):
		return (l ^ r)

	def calcul(self, query, varMap):
		l = Var("x")
		l.setValue(1)
		ptr = {
				"+": self.op_add,
				"|": self.op_or,
				"^": self.op_xor
			}
		op = "+"
		r = None
		for x in query:
			if ( op == None and self.isOperator(x) == True ):
				op = x
			elif ( self.isOperator(x) == False ):
				r = x
				l.setValue(ptr[op](l, r))
		return (l)
