import re
from query import Query

from var import Var

A = Var('A')
B = Var('B')
C = Var('C')

A.setValue(1)
B.setValue(1)
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
print(str(test.run(varMap)))

