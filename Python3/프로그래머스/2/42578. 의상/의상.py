import math

def solution(clothes):
    clothes_dict = {}
    for n, t in clothes:
        if t in clothes_dict:
            clothes_dict[t] += 1
        else:
            clothes_dict[t] = 2
    return math.prod(clothes_dict.values()) - 1