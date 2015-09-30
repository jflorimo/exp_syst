from var import Var
from query import Query

A = Var('A')
B = Var('B')

print (A | B)
A.setValue('1')
print (A | B)
B.setValue('1')
print (A | B)

test = Query("-A+B+C|D")
test.run("pok")
