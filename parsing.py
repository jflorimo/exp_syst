import string
from error import exit_error
authorizedChars = "+|^()=<>!? " +''.join(list(string.ascii_uppercase))

def checkAuthorizedChar(letter):
	for char in authorizedChars:
		if char == letter:
			return True
	return False;

def parseLine(line, letters):
	parsedLine = ""
	if len(line.strip()) > 0 and line.strip()[0] != '#':
		for letter in line:
			if (letter == '#'):
				break
			if (checkAuthorizedChar(letter)):
				if (letter != ' '):
					parsedLine += letter
			else:
				exit_error("Unauthorized char in input file")	
		print(parsedLine)
