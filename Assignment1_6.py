No= int(input("Enter a number: "))

def ChkNo(No):
	if (No>0):
		print("Number is positive");
	elif (No<0):
	    print("Number is Negative");
	else:
	    print("Number is Zero");	



if __name__ == '__main__':
   ChkNo(No)