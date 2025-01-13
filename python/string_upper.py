'''
Is the string uppercase?

8kyu
14 d ago
'''

def is_uppercase(inp):
    return not any(c.islower() for c in inp)
