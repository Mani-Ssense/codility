def solution(A):
    if len(A) == 0:
        return -1
        
    if len(A) == 1:
        return 0
        
    h = len(A) // 2
    d = {}

    for a in A:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
            
    for i, a in enumerate(A):
        if d[a] > h:
            return i
    return -1

