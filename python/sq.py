'''
sq every digit
7kyu
9 d ago
'''
def square_digits(num):
    x=str(num)
    y=[int(i) for i in x]
    s=''
    for i in y:
        s+=str(i*i)
    return int(s)
