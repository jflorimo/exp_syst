import re

class Query(object):

	def __init__(self, querystr):
		self.queryStr = querystr

	def isOperator(self, str):
		operator = ['+', '|', '&', '^']
		print ((str in operator))
		if (str in operator):
			return (True)
		return (False)

	def run(self, varMap):
		left = "old Value"
		operator = "+"
		right = None
		tmp = self.queryStr.split(" ")

		for x in tmp:
			if ( operator == None and self.isOperator(x) ):
				operator = x
			elif ( right == None ):
				right = x
				print (left + operator + right)
				operator = None
				right = None

