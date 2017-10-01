### creating the function for validatiting a gtin8 number
def valid (gtin):	
		gtin2=int(gtin[1])+int(gtin[3])+int(gtin[5])+int(gtin[7])+(int(gtin[4])+int(gtin[6])+int(gtin[2])+int(gtin[0]))*3
		# above it changes each number in the input to an interger then doing the gtin8 algorithm multiplying by 3 then 1 then 3 etc.
		#adds all of the numbers together
		if gtin2%10!=0: 
			print ("GTIN8 is invalid")
		else:
			print ("valid GTIN-8")
		#if the length if the gtin != 7 and is not a digit it will print error and ask the question again
###creating the function for creating a gtin8 number
def gtin7 (gtin):
				gtin1=int(gtin[1])+int(gtin[3])+int(gtin[5])+(int(gtin[0])+int(gtin[2])+int(gtin[4])+int(gtin[6]))*3
				# above it changes each number in the input to an interger then doing the gtin8 algorithm multiplying by 3 then 1 then 3 etc.
				#adds all of the numbers together
				rem=gtin1%10
				
				#to find the check digit we need the remainder of the sum3 and 10
				#rem=divmod(43,10)[1]
				#div=divmod(43,10)[0]
				
				# The remainder might be 0 if the number sum3 is a multiple of 10
				# Generate the Check Digit appropriately
				if rem==0:
					checkdigit=0
				else:
					checkdigit=10-rem
					#to find checkdigit we take the remainder form 10
				GTIN8=str(gtin)+str(checkdigit)
				#puts the gtin7 that the user entered and the checkdigit and combing it all into one number-The GTIN8
				print('Your GTIN-8 ' + GTIN8)
			#if the length if the gtin != 7 and is not a digit it will print error and ask the question again
				
while 1:
	gtin=input("Do you want to make a gtin type gtin7 or if you want to validate one type valid")
	#ask the user which one they want to do validate or create
	if len(gtin)==8 and gtin.isdigit:
		valid(gtin)
	elif len(gtin)==7 and gtin.isdigit:
		gtin7(gtin)
	else:
		if raw_input("Error incorrect do you want to carry on?(Type Y is yes)")!="Y":
			quit()
		#if they dont enter anything or something else it ask do you want to carry on
		#if the user input != to Y then the code closes
