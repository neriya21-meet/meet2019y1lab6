##total = 0
##for number in range(1, 10 + 1):
##    print(number)
##    total = total + number
##print(total)
##

##def add_numbers():
##    total= 0
##    for number in range(1, 10 +10):
##        print(number)
##        total = total + number
##    return (total)
##answer= add_numbers()
##print(answer)

def add_num2(start, end):
	total=0	
	for number in range (start,end+1):
		print(number)
		total+= number
	return (total)
test1 = add_num2(333,777)
print(test1)
