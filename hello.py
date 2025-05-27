def factorial(n):
    if n == 0:
        retrun 1
    else:
    	return n* factorial(n-1)
    	
 number = 5
 result = factorial(number)
 print(f"the facorial of {number} is {result}.")
