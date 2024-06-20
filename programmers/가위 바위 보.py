def solution(rsp):
    answer = ''
    
    rsp_list=list(rsp)
    
    for i in rsp_list:
        if i=="2":
            answer+=str(0)
        elif i=="0":
            answer+=str(5)
        else:
            answer+=str(2)
    
    return answer
