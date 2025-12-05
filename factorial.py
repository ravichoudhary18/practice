# the product of a positive integer and all the integers below it; e.g. factorial four ( 4! ) is equal to 24.

def fact(number):
    if number == 0:
        return 1
    
    return  number * fact(number -1)


x=int(input())
print(fact(x))