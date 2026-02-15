#Given an integer n, print:
#"Fizz" if n is divisible by 3
#"Buzz" if n is divisible by 5
#"FizzBuzz" if n is divisible by both 3 and 5
#Otherwise, print n

def fizzBuzz(number):
    if number%3==0 and number%5==0:
        print("FizzBuzz")
    elif number%3==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
    else:
        print(number)
