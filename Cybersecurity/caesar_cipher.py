def encrypt(message,shift):
	encrypted = ""
	for char in message:
		if(char == " "):
			encrypted+=" "
		else:
			C = ord(char)+shift
			E = chr(C)
			encrypted += E
	return encrypted

def decrypt(Encrypt,shift):
	decrypted = ""
	for char in Encrypt:
		if(char == " "):
			decrypted += " "
		else:
			D = ord(char)-shift
			M = chr(D)
			decrypted += M
	return decrypted

Continue = True
while Continue:

	message = input("Enter the message: ")
	shift = int(input("Enter the shift value: "))

	print("====== Caesar Cipher ======")
	print("1. Encryption.")
	print("2. Decryption.")
	print("===========================")

	choice = int(input("Enter your choice: "))

	if(choice == 1 or choice == 2):
		encrypted_text = encrypt(message,shift)
		print("Encrypted Message:",encrypted_text)
		print("Decrypted Message:",decrypt(encrypted_text,shift))
	else:
		print("Invalid Choice!")

	opt = input("Do you wish to continue (YES/NO):")

	if(opt.lower() == "yes"):
		Continue = True
	else:
		Continue = False
