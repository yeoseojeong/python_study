def solution(num_list):
    answer = []
    res=sorted(num_list)
    
    for i in range(5):
        answer.append(res[i])
    return answer
