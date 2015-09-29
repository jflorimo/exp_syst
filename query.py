import re

class Query(object):

	def __init__(self, querystr):
		self.queryStr = querystr

	def isOperator(self, str):
		operator = ['+', '|', '&', '^', '-']
		if (str in operator):
			return (True)
		return (False)

	def calcul(self, varMap):
		left = "old Value"
		operator = "+"
		right = None

		for x in self.queryStr:
			if ( operator == None and self.isOperator(x) ):
				operator = x
			elif ( operator != None and self.isOperator(x) ):
				tmpOp = 0 if operator == '+' else -1
				tmpOp2 = 0 if x == '+' else -1
				operator = '-' if tmpOp + tmpOp2 == -1 else '+'
			elif ( right == None ):
				right = x
				print (left + operator + right)
				operator = None
				right = None

