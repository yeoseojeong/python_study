def solution(n):
    def odd(n):
        answer = 0
        for i in range(n+1):
            if i % 2 == 0:
                answer += (i*i)
        return answer
    
    def even(n):
        answer = 0
        for i in range(n+1):
            if i % 2 == 1:
                answer += i
        return answer

    if n % 2 == 0:
        return odd(n)
    else:
        return even(n)
