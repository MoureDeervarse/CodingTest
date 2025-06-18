import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) > 1:
        first_val = heapq.heappop(scoville)
        if first_val >= K:
            return answer
        
        second_val = heapq.heappop(scoville)
        heapq.heappush(scoville, first_val + second_val*2)
        answer += 1
    
    val = heapq.heappop(scoville)
    if val < K:
        return -1
    
    return answer