# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
# https://app.codility.com/demo/results/training929UJV-7J3/
def solution(A, K):
    l = len(A)
    arr = [0] * l
    
    for i in range(0, l):
        if i + K < l:
            arr[i + K] = A[i]
        else:
            idx = (i + K) % l
            arr[idx] = A[i] 
    return arr
 
