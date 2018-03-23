import sys

param_1 = sys.argv[1]
param_2 = sys.argv[2]


def foo(param_1, param_2):
	print "Testing coverage package"
	if param_1 > param_2:
		print "p1 is greater than p2"
		param_2 = param_2 + 1
	elif param_1 == param_2:
		print "p1 and p2 are equal"
	else:
		print "p2 is greater than p1 :)"
		print "Something"


if __name__ == "__main__":
	foo(param_1, param_2)
