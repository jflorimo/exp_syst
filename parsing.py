import string
import re
from var import Var
from error import exit_error


autorizedVars = list(string.ascii_uppercase)
authorizedSpecialChars = "+|^()=<>!? 	\n"
authorizedChars = authorizedSpecialChars +''.join(autorizedVars)

def getQueryRegex():
	return "^(([!]?[A-Z])([+^|]([!]?[A-Z]))*)(=>|<=>)(([!]?[A-Z])([+^|]([!]?[A-Z]))*)$"

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

def checkLine(line, input, output, queries):
	regexQuery = getQueryRegex()
	regexInput = "^([=][]A-Z]{1,})$"
	regexOutput = "^([?][]A-Z]{1,})$"

	if re.search(regexQuery, line):
		queries.append(line)
	elif re.search(regexInput, line):
		input.extend(list(line[1:]))
	elif re.search(regexOutput, line):
		output.extend(list(line[1:]))
	else:
		exit_error("Unauthorized Line in file: "+ line) 

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
		checkLine(parsedLine, input, output, queries)

