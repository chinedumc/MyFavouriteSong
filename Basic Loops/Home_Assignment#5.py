
'''
A program that prints numbers 1 to 100.
But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz"

'''

num=100
for i in range(0,num):
    if i<=100:
        if (i+1)%3==0 and (i+1)%5==0: # Check if number is divisible by 3 and 5
            print("FizzBuzz")
        elif (i+1)%5==0 and (i+1)%3 != 0: # Check if number is only divisible by 5
            print("Buzz")
        elif (i+1)%3==0 and (i+1)%5!=0: # Check if number is only divisible by 3
            print("Fizz")
        else:
            print(i+1)
            continue
