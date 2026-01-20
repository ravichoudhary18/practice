# Question:
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

# Hints:
# Consider use yield


def main(end_number):
    for i in range(end_number + 1):
        if i % 7 == 0:
            yield i

for i in main(100):
    print(i)

