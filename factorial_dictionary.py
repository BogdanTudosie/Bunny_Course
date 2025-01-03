# we return either the factorial of the number or None if the number is negative
def factorial(n: int) -> int | None: 
    if n < 0:
        print(f"Number {n} is smaller than zero, exiting")
        return None
    
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i
        
    return result

# setting the return type to dictionary
def dictionary_factorial(elements: int) -> dict:
    result = {} #initialize as empty dictionary
    for i in range(elements):
        result[i] = factorial(i) # here we can use also dict.update({i: factorial(i)}) - update function does the same thing
    return result

if __name__ == "__main__":
    number_of_factorials = int(input("Enter the number of Factorials: "))
    factorials_dict = dictionary_factorial(number_of_factorials)
    
    # we test for all the numbers in the dictionary
    for i in range(len(factorials_dict)):
       print(f"Factorial for element {i} is {factorials_dict[i]}")