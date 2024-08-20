from functools import reduce
def mul(num_list):
    return reduce(lambda x, y: x * y, num_list)
def solution(num_list):

    return int(len(num_list)>=11) * sum(num_list) or mul(num_list)
