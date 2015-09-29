import sys
from parsing import parseLine

letters = {}

def parse( lines ):
	for tmp in lines:
		parseLine(tmp, letters)
		# Go parse here

def read( filename ):
	result = []

	try:
		fd = open(filename, 'r')
	except Exception:
		print("[ERROR] Can't open specified file")
		exit(-2)

	for tmp in fd :
		result.append(tmp)

	parse(result)

if ( len(sys.argv) < 2 ) :
	print("Usage : ./" + sys.argv[0] + " [Input file]")
	exit( -1 )

print(sys.argv[1])
read(sys.argv[1])
