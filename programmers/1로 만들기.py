def solution(num_list):
    answer = 0
    n=0
    
    for i in num_list:
        while i>1:
            i=i//2
            answer+=1
            
    return answer
