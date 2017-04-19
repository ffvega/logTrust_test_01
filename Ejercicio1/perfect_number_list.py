from math import sqrt

#
# classify a number into perfecto/defectivo/abundante range 
#
def perfect(num):
	acum = 0
	
	# create a list containing the first n/2 numbers 
	for i in range(1,num/2+1):
	
		# in case of divisor, the number is added
		if num % i == 0:
			acum += i
			
	if acum == num:
		print "PERFECTO  : " + str(num)
	elif acum < num:
		print "DEFECTIVO : " + str(num)
	else:
		print "ABUNDANTE : " + str(num)

#
# call the 'perfect' method with each number in the list
#
def perfect_list(number_list):
	for i in number_list:
		perfect(i)

#
# example
#
number_list = []
for i in range(1,100):
	number_list.append(i)
perfect_list(number_list)


#input("Press Enter to continue...")