def solution(a, b):
    answer = 0
    
    a_res=int(str(a)+str(b))
    b_res=int(str(b)+str(a))
    
    if a_res>b_res:
        return a_res
    else:
        return b_res
   
