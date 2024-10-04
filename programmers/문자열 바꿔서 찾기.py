def solution(mystring, pat):
   
    transformed = ''
    
    for i in mystring:
        if i == 'A':
            transformed += 'B'
        elif i == 'B':
            transformed += 'A'
        else:
            transformed += i  
    
 
    if pat in transformed:
        return 1 
    else:
        return 0 
