# n**3 solution, 75% score

def solution(A):
    if len(A) < 3:
        return 0
    
    for i in range(0, len(A) - 2):
        for j in range(i + 1, len(A) - 1):
            for k in range(j + 1, len(A)):  
                if is_triangular(A, i, j, k):
                    return 1
                    
    return 0
        
def is_triangular(A, P, Q, R):
    if not ((P >= 0) and (Q > P) and (R > Q) and (R < len(A))):
        return False
    if not ((A[P] + A[Q]) > A[R]):
        return False
    if not ((A[Q] + A[R]) > A[P]):
        return False
    if not ((A[R] + A[P]) > A[Q]):
        return False
        
    return True
