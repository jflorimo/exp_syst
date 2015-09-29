import string
from var import Var
from error import exit_error


autorizedVars = list(string.ascii_uppercase)
authorizedSpecialChars = "+|^()=<>!? 	"
authorizedChars = authorizedSpecialChars +''.join(autorizedVars)

def isVar(letter):
	for var in autorizedVars:
		if var == letter:
			return True
	return False

def checkAuthorizedChar(letter):
	for char in authorizedChars:
		if char == letter:
			return True
	return False;

def fillVar(vars, letter):
	if isVar(letter):
		if not letter in vars:
			vars[letter] = Var(letter)

def parseLine(line, vars, input, output, queries):
	parsedLine = ""
	if len(line.strip()) > 0 and line.strip()[0] != '#':
		for letter in line:
			if (letter == '#'):
				break
			if (checkAuthorizedChar(letter)):
				if not letter.isspace():
					parsedLine += letter
					fillVar(vars, letter)
			else:
				exit_error("Unauthorized char in input file")
		# processLine(parsedLine, input, output, queries)

