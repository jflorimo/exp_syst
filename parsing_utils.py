import re
from var_solution import VarSolution
from parsing import getQueryRegex
from parsing import isVar


def init_varsValue(vars, input):
	for char in input:
		vars[char].setValue(1)

def isResultQueryUndefined(resultQuery):
	for char in resultQuery:
		if char == "^" or char == "|":
			return True
	return False

def setVarsSolution(vars, solutionQuery, resultQuery, boolean):
	if not isResultQueryUndefined(resultQuery):
		for char in resultQuery:
			if isVar(char):
				solution = VarSolution(solutionQuery, resultQuery, char)
				if not boolean:
					vars[char].setSolutionQuery(solution)
				else:
					vars[char].setSolutionQueryAtBegin(solution)

def setVarsData(vars, solution, comparator, result):
	if comparator == "<=>":
		setVarsSolution(vars, solution, result, True)
		setVarsSolution(vars, result, solution, True)
	else:
		setVarsSolution(vars, solution, result, False)

def init_varsQueries(vars, queries):
	for query in queries:
		regex = re.search(getQueryRegex(), query)
# print("Solution: " + regex.group(1) + " cr: " + regex.group(5) + "result: "+ regex.group(6))
		setVarsData(vars, regex.group(1), regex.group(5), regex.group(6))
		