import math

print("========== Calculator ==========")
Continue = True

while(Continue == True):
	num1 = int(input("Enter number1: "))
	num2 = int(input("Enter number2: "))
	print("\n===== Operators =====")
	print("Addition (+)")
	print("Subtraction (-)")
	print("Multiplication (*)")
	print("Division (/)")
	print("Modulus (%)")
	print("Exponential (**)")
	print("Floor Division (//)")
	print("Square Root (sqrt)")
	print("Percentage (percent %)")
	print("=======================\n")
	opt = input("Enter the operation: ")

	if(opt == "+"):
		num3 = num1+num2
		print("The addition of",num1,"and",num2,"=",num3)
	elif(opt == "-"):
		num3 = num1-num2
		print("The subtraction of",num1,"and",num2,"=",num3)
	elif(opt == "*"):
		num3 = num1*num2
		print("The multiplication of",num1,"and",num2,"=",num3)
	elif(opt == "/"):
		if(num2 == 0):
			print("Cannot divide by Zero")
		else:
			num3 = num1/num2
			print("The division of",num1,"and",num2,"=",num3)
	elif(opt == "%"):
		num3 = num1%num2
		print("The modulus of",num1,"and",num2,"=",num3)
	elif(opt == "**"):
		num3 = num1**num2
		print("The result of",num1,"to the power of",num2,"=",num3)
	elif(opt == "//"):
		if(num2 == 0):
			print("Cannot divide by Zero")
		else:
			num3 = num1//num2
			print("The floor division of",num1,"and",num2,"=",num3)
	elif(opt == "sqrt"):
		if(num1 == 1 and num1 < 0):
			print("Square root cannot be taken for Negative number")
		elif(num2 == 1 and num1 < 0):
			print("Square root cannot be taken for Negative number")
		else:
			num = int(input("Enter the number (1 or 2):"))
			if(num == 1):
				n1 = math.sqrt(num1)
				print("The Square root of",num1,"=",n1)
			elif(num == 2):
				n2 = math.sqrt(num2)
				print("The Square root of",num2,"=",n2)
	elif(opt.lower() == "percentage"):
		if(num2 == 0):
			print("Cannot divide by Zero")
		else:
			percent = (num1/num2)*100
			print("Percentage:",percent,"%")
	else:
		print("Invalid Operation")

	Ctn = input("Do you wish to continue (YES/NO) :")

	if(Ctn.lower() == "yes"):
		Continue = True
	else:
		Continue = False
print("================================")
