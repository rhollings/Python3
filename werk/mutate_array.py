'''
CodeSignal Question
given arr and int, return new array with such mutations
'''

x = 5
y = [4, 0, 1, -2, 3]
#solution(n, a) = [4, 5, -1, 2, 1]

def solution(n, a):
    curr = 0
    b = []
    
    for i in range(len(a)):
        print(i)
        if a[i] == a[0]:
            curr = a[i] + a[i + 1]
        elif i == last:
            curr = a[i - 1] + a[i]
        else:  
            curr = a[i - 1] + a[i] + a[i + 1]
        b.append(curr)
    return b

#solution(x, y)
