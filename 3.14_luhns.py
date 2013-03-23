#!/usr/bin/env python2
import random

def is_luhn_valid(n):
	cNum = list(str(n))
	nSum = 0
	if len(cNum)%2 == 0:
		print "even"
		for i in range(len(cNum)):
			if i%2 == 0:
				cNum[i] = str(2 * int(cNum[i]))
				if int(cNum[i]) > 9: cNum[i] = str(int(cNum[i]) - 9)
		for i in range(len(cNum)):
			nSum += int(cNum[i])
		print nSum
		if nSum%10 == 0:
			print True
			return True
		else:
			print False
			return False

	else:
		print "odd"
		for i in range(len(cNum)):
			if i%2 == 1:
				cNum[i] = str(2 * int(cNum[i]))
				if int(cNum[i]) > 9: cNum[i] = str(int(cNum[i]) - 9)
		for i in range(len(cNum)):
			nSum += int(cNum[i])
		print nSum
		if nSum%10 == 0:
			print True
			return True
		else:
			print False
			return False

is_luhn_valid(583265110934587)
