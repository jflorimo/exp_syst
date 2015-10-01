import re

class Query(object):

	def __init__(self, querystr):
		print (querystr)
		self.queryStr = querystr
		self.priority = {}
		self.resolver = self.resolve(self.queryStr)
		print (self.resolver)

	def findSubQuery( self, result ) :
		if re.subn("(\(!?\?)([+^|]!?([A-Z]|\?)){1,}\)", "?", result, count=1)[0] != result:
			return True
		elif re.subn("\((!?([A-Z]|\?)[+^|]){1,}!?\?\)", "?", result, count=1)[0] != result :
			return True
		return False

	def resolve( self, result ):
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
			tmp = {result[pos.start() + 1:pos.end() - 1]: []}
			result = re.subn(regexp, "?", result, count=1)[0]

			while (self.findSubQuery(result)) :
				if re.subn("(\(!?\?)([+^|]!?([A-Z]|\?)){1,}\)", "?", result, count=1)[0] != result :
					pos = re.search("(\(!?\?)([+^|]!?([A-Z]|\?)){1,}\)", result)
					tmp2 = {result[pos.start() + 1:pos.end() - 1]: [tmp]}
					tmp = tmp2
					result = re.subn("(\(!?\?)([+^|]!?([A-Z]|\?)){1,}\)", "?", result, count=1)[0]

				if re.subn("\((!?([A-Z]|\?)[+^|]){1,}!?\?\)", "?", result, count=1)[0] != result :
					pos = re.search("\((!?([A-Z]|\?)[+^|]){1,}!?\?\)", result)
					tmp2 = {result[pos.start() + 1:pos.end() - 1]: [tmp]}
					tmp = tmp2
					result = re.subn("\((!?([A-Z]|\?)[+^|]){1,}!?\?\)", "?", result, count=1)[0]

			resolver[tmp_final].append(tmp)
		return resolver


	def isOperator(self, str):
		operator = ['+', '|', '&', '^', '-']
		if (str in operator):
			return (True)
		return (False)

	def run(self):
		i = 0
		while ( i < self.queryStr.length() ):
			if ( self.queryStr[i] == "(" ):
				i += self.parenthese( self.queryStr, i )

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
				print (left + " " + operator + " " +  right)
				operator = None
				right = None

