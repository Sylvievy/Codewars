'''
Sum of two lowest positive integers
7kyu
6 d ago
'''
def sum_two_smallest_numbers(numbers):
    x=min(numbers)
    numbers.remove(x)
    y=min(numbers)
    numbers.remove(y)
    return x+y
