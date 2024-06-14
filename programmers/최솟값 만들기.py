def solution(A,B):
    answer = 0
    
    a_res=sorted(A)
    b_res=sorted(B,reverse=True)
    
    
    for i in range(len(A)):
        answer+=(a_res[i]*b_res[i])
    
    return answer
