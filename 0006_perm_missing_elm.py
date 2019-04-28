# https://app.codility.com/demo/results/training9CUG3D-D89/
def solution(A):
    r = 0
    i = 1
    
    for a in A:
        r = r ^ a ^ i
        i +=1 
    
    return r ^ i

