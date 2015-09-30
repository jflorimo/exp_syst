import sys
from parsing import parseLine
from utils import init_vars

vars = {}
input = []
output = []
queries = []


def debug():
	print("######Vars:######")
	for var in vars:
		print(vars[var].toString())
	print("######Queries:######")
	for query in queries:
		print(query)
	print("######Input:######")
	print(input)
	print("######OutPut:######")
	print(output)

def parse( lines ):
	for tmp in lines:
		parseLine(tmp, vars, input, output, queries)
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
init_vars(vars, input)
debug()


