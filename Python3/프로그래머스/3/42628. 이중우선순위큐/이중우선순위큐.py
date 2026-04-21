import sys

def solution(operations):
    queue = DoublePriorityQueue()
    for cmd in operations:
        if cmd.startswith('I'):
            queue.insert(int(cmd.split()[1]))
        elif cmd == "D 1":
            queue.pop(True)
        elif cmd == "D -1":
            queue.pop(False)
        else:
            raise Exception(f"Not implemented case for {cmd}")
    
    return [queue.get_max(), queue.get_min()]

class DoublePriorityQueue:
    def __init__(self):
        self.init()
        
    def init(self):
        self.max_value = -sys.maxsize - 1
        self.min_value = sys.maxsize
        self.value_dict = dict()
        
    def insert(self, value):
        if self.max_value < value:
            self.max_value = value
        if self.min_value > value:
            self.min_value = value
        if value in self.value_dict:
            self.value_dict[value] += 1
        else:
            self.value_dict[value] = 1
    
    def pop(self, is_max):
        if len(self.value_dict) == 0:
            return
        
        key = self.max_value if is_max else self.min_value
        
        if self.value_dict[key] > 1:
            self.value_dict[key] -= 1
        else:
            # to init for empty dict
            if len(self.value_dict) == 1:
                self.init()
                return
            
            # remove target value and set next min/max
            del self.value_dict[key]
            next_value = sorted(self.value_dict.keys(), reverse=is_max)[0]
            if is_max:
                self.max_value = next_value
            else:
                self.min_value = next_value
            
    def get_max(self):
        return 0 if len(self.value_dict) == 0 else self.max_value
    
    def get_min(self):
        return 0 if len(self.value_dict) == 0 else self.min_value
    
        