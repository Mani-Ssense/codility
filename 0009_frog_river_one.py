# https://app.codility.com/demo/results/trainingEPBRST-6AD/
def solution(X, A):
    s = set()
    for k, v in enumerate(A):
        s.add(v)
        if len(s) == X:
            return k
            
    return -1

