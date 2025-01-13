'''
Reverse words
7kyu
3 d ago

'''
def reverse_words(text):
    a=list(map(str,text.split(' ')))
    b=[]
    for i in a:
        b.append(i[::-1])
    return ' '.join(b)
