# https://app.codility.com/demo/results/trainingMWVQDP-FQD/
def solution(N):
    b = bin(N)[2:]
    b = b.strip('0')
    arr = b.split('1')
    
    m = 0
    for a in arr:
        if len(a) > m:
            m = len(a)
    return m

