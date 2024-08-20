def solution(s1, s2):
    answer = 0
    
    for char in s1:
        for char_2 in s2:
            if char==char_2:
                answer+=1
    return answer
