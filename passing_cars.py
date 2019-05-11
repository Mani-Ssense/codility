def solution(A):
    r = 0
    t = sum(A)
    
    for a in A:
        if a == 0:
            r += t
        else:
            t -= 1
    
    if r > 1000000000:
        return -1 
        
    return r
