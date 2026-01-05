def main(number:int)-> dict:
    return {i: i*i for i in range(1, number+1)}

result = main(12)
print(result)