def solution(S):
    l = len(S)
    if (l % 2) == 1:
        return 0
    
    s = []
    for c in S:
        if c == '(':
            s.append(c)
        elif c == ')':
            if len(s) == 0:
                return 0
            s.pop()
        else:
            return 0
    
    return int(len(s) == 0)
    
