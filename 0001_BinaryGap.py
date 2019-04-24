#https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
#https://app.codility.com/demo/results/trainingW7PUFK-KZ5/
def solution(N):
    b = bin(N)
    b = b[2:]
    
    max_gap = 0
    current_gap = 0
    seen_one = False
    
    for c in b:
        if c == '1' and not seen_one:
            seen_one = True
            continue
        
        if seen_one and c == '0':
            current_gap += 1
            continue
        
        if seen_one and c == '1':
            if current_gap > max_gap:
                max_gap = current_gap
            current_gap = 0
            
    return max_gap
