'''
Grade book

8kyu
12 m ago
'''
def get_grade(s1, s2, s3):
    score=(s1+s2+s3)/3
    if (90 <= score <= 100):
        grade='A'
    elif (80 <= score < 90):
        grade='B'
    elif (70 <= score < 80):
        grade='C'
    elif (60 <= score < 70):
        grade='D'
    else:
        grade='F'
    return grade
