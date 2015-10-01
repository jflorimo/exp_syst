import re
from query import Query

from var import Var

A = Var('A')
B = Var('B')
C = Var('C')

A.setValue(1)
B.setValue(1)
C.setValue(0)
# print (A + B)
# A.setValue('1')
# print (A + B)
# B.setValue('1')

varMap = {
			"A" : A,
			"B" : B,
			"C" : C
		}

test = Query("(A+B)|(A+B)")
print( "---------" )
test.run(varMap)

