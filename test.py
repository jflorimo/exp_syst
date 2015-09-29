from var import Var

A = Var('A')
B = Var('B')

print (A | B)
print (not A)

A.setValue('1')
print (A | B)
B.setValue('1')
print (A | B)
print (not A)
