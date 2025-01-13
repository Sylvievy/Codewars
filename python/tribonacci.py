'''
tribonacci sequence
6kyu
9 h ago
'''
def tribonacci(s, n):
    if n==0:
        return []
    elif n<len(s):
        return s[:n]
    else:
        result=s.copy()
        for i in range(n-3):
            result.append(result[len(result)-1]+result[len(result)-2]+result[len(result)-3])
        return result
