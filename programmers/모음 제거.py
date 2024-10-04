def solution(my_string):
    aeiou = ['a', 'e', 'i', 'o', 'u']
    answer = ''
    
    for i in my_string:
        if i not in aeiou:  
            answer += i  

    return answer  
