import coverage
import simplest
import os

def run_tests():
	simplest.foo(1, 2)
	simplest.foo(1, 1)
	simplest.foo(2, 1)

command = "sudo coverage html -d /var/www/html"
print "Executing {}".format(command)
os.system(command)