def add(a,b):
	checkInputs(a,b)
	return a+b
def substract(a,b):
	checkInputs(a,b)
	return a-b
def multiply(a,b):
	checkInputs(a,b)
	return a*b
def divide(a,b):
	checkInputs(a,b)
	return a/b
def checkInputs(a,b):
	if not instance(a,(int,float)) or not instance(b,(int,float)):
		raise TypeError("Inputs must be either int or float!")
