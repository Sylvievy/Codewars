'''
Highest and Lowest in a given string of integers

7kyu
14 d ago
'''
def high_and_low(numbers):
    # ...
    n=list(map(int,numbers.split()))

    return f"{max(n)} {min(n)}"

high_and_low('11 4 2 -1 4')
