# https://app.codility.com/demo/results/trainingJ2RWYQ-WQJ/
def solution(A):
    r = 0
    i = 1
    for a in A:
        r = r ^ a ^ i
        i += 1
        
    if r == 0:
        return 1
    
    return 0

