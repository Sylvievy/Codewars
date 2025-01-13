'''
Total amount of points
8kyu
7 d ago
'''
def points(games):
    x=0
    y=0
    p=0
    for i in games:
        x=int(i[0])
        y=int(i[2])
        if x>y:
            p+=3
        elif x==y:
            p+=1
            
        
    return p
