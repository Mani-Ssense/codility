# https://app.codility.com/demo/results/trainingQPGKVG-NV8/
def solution(A):
    r = 0
    for a in A:
        r ^= a
    
    return r

