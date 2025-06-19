class Command:
    def __init__(self, cmd_list):
        if len(cmd_list) < 3:
            return IndexError("command element count below 3")
        self.start_idx = cmd_list[0] - 1
        self.end_idx = cmd_list[1]
        self.target_idx = cmd_list[2] - 1
    
    def get_target(self, arr):
        if self.start_idx > self.end_idx or self.end_idx - self.start_idx < self.target_idx:
            return IndexError("index range is not valid")
        partial_arr = sorted(arr[self.start_idx:self.end_idx])
        return partial_arr[self.target_idx]

def solution(array, commands):
    return [Command(cmd_list).get_target(array) for cmd_list in commands]