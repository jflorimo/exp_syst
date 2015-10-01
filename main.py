import					sys
from parsing import		parseLine
from parsing_utils import		init_varsValue
from parsing_utils import		init_varsQueries

vars = {}
input = []
output = []
queries = []


def debug():
	print("######Vars:######")
	for var in sorted(vars):
		vars[var].display()
	# print("######Queries:######")
	# for query in queries:
	# 	print(query)
	# print("######Input:######")
	# print(input)
	# print("######OutPut:######")
	# print(output)

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
init_varsValue(vars, input)
init_varsQueries(vars, queries)
debug()



