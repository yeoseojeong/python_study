def solution(myString):
    answer = ''
    
    for char in myString:
        if char.isupper():
            answer+=char.lower()
        else:
            answer+=char
    return answer
