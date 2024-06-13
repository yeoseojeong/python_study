def solution(x):
    
    total=0
    
    list_x=list(map(int,str(x)))
                
   
    for i in list_x:
        total+=i
    
    if x%total==0:
        return True
    else:
        return False
        
    
