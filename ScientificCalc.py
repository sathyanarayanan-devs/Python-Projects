import math

def add(a,b):
	c = a+b
	print("Add:",c)

def sub(a,b):
	c = a-b
	print("Subtract:",c)

def mul(a,b):
	c = a*b
	print("Multiply:",c)

def div(a,b):
	c = a/b
	print("Divide:",c)

def mod(a,b):
	c = a%b
	print("Modulus:",c)

def exp(a,b):
	c = a**b
	print("Exponential:",c)

def sqrt(num):
	sr = math.sqrt(num)
	print("Square root:",sr)

def sine(num):
	s = math.sin(num)
	print("Sine(",num,"):",s)


def cosin(num):
	s = math.cos(num)
	print("Cosine(",num,"):",s)


def tane(num):
	s = math.tan(num)
	print("Tangent(",num,"):",s)

Continue = True
a = int(input("Enter the number1:"))
b = int(input("Enter the number2:"))
while Continue:
	print("===== Operations =====")
	print("Addition(+)")
	print("Subtraction(-)")
	print("Multiplication(*)")
	print("Division(?)")
	print("Square Root(Sqrt)")
	print("Sine (sin)")
	print("Cosine (cos)")
	print("Tangent (tan)")
	print("======================")

	opt = input("Enter operator:")

	if(opt == "+"):
		add(a,b)
	elif(opt == "-"):
		sub(a,b)
	elif(opt == "*"):
		mul(a,b)
	elif(opt == "/"):
		div(a,b)
	elif(opt.lower() == "sqrt"):
		num = int(input("Select a value to get Square root (1 or 2):"))
		if(num == 1):
			sqrt(a)
		elif(num == 2):
			sqrt(b)
		else:
			print("Invalid Value")
	elif(opt.lower() == "sin"):
		num = int(input("Select a value to get Sine Value (1 or 2):"))
		if(num == 1):
			sine(a)
		elif(num == 2):
			sine(b)
		else:
			print("Invalid Value")
	elif(opt.lower() == "cos"):
		num = int(input("Select a value to get Cosine Value (1 or 2):"))
		if(num == 1):
			cosine(a)
		elif(num == 2):
			cosine(b)
		else:
			print("Invalid Value")
	elif(opt.lower() == "tan"):
		num = int(input("Select a value to get Tangent Value (1 or 2):"))
		if(num == 1):
			tane(a)
		elif(num == 2):
			tane(b)
		else:
			print("Invalid Value")
	else:
		print("Invalid Operation!")

	choice = input("Do you wish to continue(YES/NO):")
	if(choice.lower() == "yes"):
		Continue = True
	else:
		print("Thank you for using Calculator!!")
		Continue = False
