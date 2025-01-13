'''
Sum Arrays
8kyu
15 m ago
'''

def sum_array(a):
    sum=0
    if a==[]:
        return 0
    else:
        for i in a:
            sum+=i
    return sum
