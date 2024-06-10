def solution(s):

    s_list = list(map(int, s.split()))
   
    max_value = -10000
    min_value = 10000

    for i in range(len(s_list)):
        if max_value < s_list[i]:
            max_value = s_list[i]

    for i in range(len(s_list)):
        if min_value > s_list[i]:
            min_value = s_list[i]
    
    answer = [str(min_value), str(max_value)]
    
    return ' '.join(answer)
