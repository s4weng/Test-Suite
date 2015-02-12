#!/usr/bin/env python
import sys, subprocess

if len(sys.argv) != 3:
	print "Incorrect number of arguments"
	
else:
	correct = True
	f = open(sys.argv[2], 'r')

	"""Iterate through each test case"""
	for line in f:
		input = open(line.rstrip()+'.in', 'r').read()
		output = open(line.rstrip()+'.out', 'r').read()
       	        actual = subprocess.check_output('./'+sys.argv[1]+' '+input,shell=True)

		"""Compare actual output to expected output"""
		if (actual != output):
			print "Error in", line + "Actual:" , actual + "Expected:", output.rstrip()
			correct = False
	f.close()

	if correct == True:
		print "All test cases have passed."