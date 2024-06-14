def solution(food):
    answer = ''
    plus=''
    
    for i in range(1,len(food)):
        if food[i]%2==0:
            for pl in range(food[i]//2):
                answer+=str(i)
        else:
            food[i]-=1
            for mi in range(food[i]//2):
                answer+=str(i)
    
    answer+=str(0)
    
    plus = ''.join(reversed(answer[:-1]))  
    
    answer+=plus
    
    return answer
