import re
from var_solution import VarSolution
from parsing import getQueryRegex
from parsing import isVar


def init_varsValue(vars, input):
	for char in input:
		vars[char].setValue(1)

def setVarsSolution(vars, solutionQuery, resultQuery):
	for char in resultQuery:
		if isVar(char):
			solution = VarSolution(solutionQuery, resultQuery, char)
			vars[char].setSolutionQuery(solution)

def setVarsData(vars, solution, comparator, result):
	if comparator == "<=>":
		setVarsSolution(vars, solution, result)
		setVarsSolution(vars, result, solution)
	else:
		setVarsSolution(vars, solution, result)

def init_varsQueries(vars, queries):
	for query in queries:
		regex = re.search(getQueryRegex(), query)
# print("Solution: " + regex.group(1) + " cr: " + regex.group(5) + "result: "+ regex.group(6))
		setVarsData(vars, regex.group(1), regex.group(5), regex.group(6))
		