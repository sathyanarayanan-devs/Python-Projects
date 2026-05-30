uname = input("Enter your username:")
Has_letter = True
Has_Digit = True
Has_UScore = True
Has_Spaces = False
Strength = 0

if(len(uname)>=5 and len(uname)<15):
	pass
else:
	print("Username should be in a length of 5-15")

if(uname[0].isalpha()):
	pass
else:
	print("Username must start with a letter")

for char in uname:

	if(char.isalnum() or char == "_"):
		continue
	else:
		print("Invalid Username")

	if(char.isupper() and char.islower()):
		continue
	else:
		print("Username must contain 1 uppercase and 1 lowercase letter")

	if(char.isspace()):
		continue
	else:
		print("Username should not contain any spaces")

	if(uname != "__"):
		continue
	else:
		print("Username should not contain '__'")

for i in uname:
	if(i.isalpha() and Has_letter == True):
		Strength+=4
		Has_letter = False


	if(i.isdigit() and Has_Digit == True):
		Strength+=2
		Has_Digit = False
	if(i == "_" and Has_UScore == True):
		Strength+=2
		Has_UScore = False

	if(i.isspace()):
		Has_Space = True

	if(Has_Space == False):
		Strength+=2
	else:
		print("No spaces Allowed")

if(Strength >= 8):
	print("Valid Username!")
	print("Username Strength: High")
elif(Strength >= 5 and Strength < 8):
	print("Valid Username!")
	print("Username Strength: Medium")
elif(Strength >= 2 and Strength < 5):
	print("Valid Username!")
	print("Username Strength: Low")
else:
	print("Invalid Username")
