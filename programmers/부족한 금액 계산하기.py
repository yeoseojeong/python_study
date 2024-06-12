def solution(price, money, count):
    total_cost = 0

    for i in range(1, count + 1):
        total_cost += price * i

    answer = total_cost - money

    if answer < 0:
        return 0

    return answer
