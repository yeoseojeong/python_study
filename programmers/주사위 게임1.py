def solution(a, b):
    answer = 0
    
    if (a%2==1) and (b%2==1):
        answer=(a*a)+(b*b)
    elif ((a%2==1)and(b%2==0)) or ((a%2==0)and(b%2==1)):
        answer=2*(a+b)
    elif (a%2==0) and (b%2==0):
        if a>b:
            answer=a-b
        else:
            answer=b-a
    return answer
