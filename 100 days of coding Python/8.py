#82 functions with inputs
def greet():
    print("hello greet")
    print("hello greet")
    print("hello greet")
greet()

def greet_with_name(name):
    print(f"hello {name}")
    print(f"how are you {name}")
    print(f"isn't it a green weather, {name}")
greet_with_name("Angela")


#85 prime checker
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("print number, i will check if its prime or not: "))  # Check this number
prime_checker(number=n)

#86 Ceaser Cipher part 1 - Encryption

