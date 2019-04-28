def solution(S):
    l = len(S)
    if l == 0:
        return 1
        
    if (l % 2) == 1:
        return 0
    
    set_of_open = {'(', '{', '['}
    set_of_close = {')', '}', ']'}
    
    stck = []
    
    for i in S:
        if i in set_of_open:
            stck.append(i)
        elif i in set_of_close:
            if len(stck) == 0:
                return 0
                
            poped = stck.pop()
            if i == ')' and poped != '(':
                return 0
            if i == '}' and poped != '{':
                return 0
            if i == ']' and poped != '[':
                return 0
        else:
            return 0
    
    return int(len(stck) == 0)
