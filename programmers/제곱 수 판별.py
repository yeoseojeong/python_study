def solution(n):
    answer = 2  # 기본값을 2로 설정
    
    for i in range(n + 1):  # 0부터 n까지 반복
        if (i**2) == n:
            answer = 1
            break  # 완전제곱수를 찾았으므로 반복문 종료
    
    return answer
