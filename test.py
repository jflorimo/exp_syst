import re
from query import Query

from var import Var

A = Var('A')
B = Var('B')
C = Var('C')

A.setValue(1)
B.setValue(0)
C.setValue(0)

varMap = {
			"A" : A,
			"B" : B,
			"C" : C
		}

query = "(A+B)|(B+C)"
test = Query(query)
print(query)
tmp = query
for (name, value) in varMap.items():
	tmp = str.replace(tmp, name, str(value.getValue()))
print(tmp)
result = test.run(varMap)
print("result brut = " + str(result))

def interpretResult( right, search, result ):
	undetermined = "!?[A-Z][|^]"
	composite = "!?[A-Z]\+"
	if ( re.search(undetermined, right) != None ):
		return ( -1 )
	elif ( re.search(composite, right) != None and result != 1 ):
		return ( -1 )
	elif (right.find( "!" + search ) != -1 and result != -1):
		return ( 0 if result == 1 else 1 )
	return (result)


right = "!X + Y"
print( "result for X in =>" + right + " : " + str(interpretResult(right, "X", result)) )
