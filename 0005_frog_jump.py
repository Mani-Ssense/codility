# https://app.codility.com/demo/results/trainingFTR6H6-ZG7/
def solution(X, Y, D):
    diff = Y - X
    
    if diff % D == 0:
        return diff // D
    else:
        return (diff // D) + 1

