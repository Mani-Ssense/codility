# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
# https://app.codility.com/demo/results/trainingPPNBQJ-YRE/
def solution(A):
    left_sum = 0
    right_sum = 0
    sum_all = sum(A)
    
    m = float('inf')
    
    for P in range(1, len(A)):
        left_sum += A[P-1]
        right_sum = sum_all - left_sum
        diff = abs(left_sum - right_sum)
        if diff < m:
            m = diff
    
    return m

