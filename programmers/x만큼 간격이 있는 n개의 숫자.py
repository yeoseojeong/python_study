def solution(x, n):
    result = [] 
    a = x   
    
    for i in range(n):  
        result.append(x)    
        x += a  
    
    return result
