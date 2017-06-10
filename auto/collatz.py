
def collatz(number):
    if number % 2 == 0:
        eve = number // 2
	print(eve)
	return eve 
    else:
        odd = 3 * number + 1
	print(odd)
	return odd

collatz(17)
