def solution(numbers, target):
    return dfs(numbers, target, 0)

def dfs(numbers, target, current_idx):
    if current_idx < len(numbers):
        positive_case = dfs(numbers, target, current_idx+1)
        numbers[current_idx] *= -1
        negative_case = dfs(numbers, target, current_idx+1)
        return positive_case + negative_case
    else:
        return 1 if sum(numbers) == target else 0
        