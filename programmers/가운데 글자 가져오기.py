def solution(s):
    answer = ''
    
    for i in range(len(s)):
        if (len(s)%2==0):
            answer+=(s[(len(s)//2)-1])
            answer+=(s[len(s)//2])
            break
        else:
            answer+=(s[len(s)//2])
            break
    
    return ''.join(answer)
