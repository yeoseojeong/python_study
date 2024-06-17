def solution(d, budget):
  
    sort_d=sorted(d)
    cnt=0
    
    for i in range(len(d)):
        if budget<sort_d[i]:
            break   
        budget-=sort_d[i]
        cnt+=1
        
            
    return cnt
    
