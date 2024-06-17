def solution(t, p):
    cnt = 0  
    len_p = len(p)  
    num_p = int(p)  
    
   
    for i in range(len(t) - len_p + 1):
        num_t = int(t[i:i+len_p])  
        if num_t <= num_p:  
            cnt += 1  
    
    return cnt  
