number = int(input("Get me a number: "))

# Validate that number is negative, positive or zero
if number < 0:
    print('The number is negative')
elif number == 0:
    print('The number is zero')
else:
    print('The number is positive')

# Validate if a number is odd or even
if number % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')


# Function for validate if number is prime
def isPrime(mun):
    if mun < 1:
        return False
    elif mun == 2:
        return True
    else:
        for i in range(2, mun):
            if mun % i == 0:
                return False
        return True


if isPrime(number) is True:
    print('The number is prime')
else:
    print('The number is not prime')

year = int(input("Get me a year: "))
# Validate if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('Is leap year')
else:
    print('Is not leap year')
