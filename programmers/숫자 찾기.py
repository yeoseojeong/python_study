def solution(num, k):
    answer = 0
 
    num_str=str(num)
    num_list=list(num_str)
    
    
    for i in range(len(num_list)):
        if int(num_list[i])==k:
            return i+1
        
    return -1
    
  
    
  

