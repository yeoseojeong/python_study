def solution(num_list):
    answer = 0
    plus=0
    mul=1
    
    for i in range(len(num_list)):
        plus+=num_list[i]
        mul*=num_list[i]
        
       
    if plus*plus<mul:
        answer=0
    else:
        answer=1
    return answer
