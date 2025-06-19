import heapq
class Job:
    def __init__(self, job_idx, req_time, need_time):
        self.job_idx = job_idx
        self.req_time = req_time
        self.need_time = need_time
        self.start_at = 0
    
    def __lt__(self, other):
        if self.need_time != other.need_time:
            return self.need_time < other.need_time
        elif self.req_time != other.req_time:
            return self.req_time < other.req_time
        else:
            return self.job_idx < other.job_idx
    def start(self, time_now):
        self.start_at = time_now
    def is_done(self, time_now) -> bool:
        return time_now - self.start_at >= self.need_time
    def get_working_time(self, end_time) -> int:
        return end_time - self.req_time
    def get_remain_time(self, time_now) -> int:
        # return self.need_time - (time_now - self.start_at)
        remain = self.start_at + self.need_time - time_now
        return remain if remain > 0 else 0
    
def solution(jobs):
    jobs = [Job(idx, job[0], job[1]) for idx, job in enumerate(jobs)]
    jobs.sort(key=lambda j: j.req_time)
    
    used_times: List[int] = []
    job_queue: List[Job] = []
    cur_job: Job = None

    check_job_idx = 0
    time_now = 0
    while len(jobs) > len(used_times):
        # 이 시점에 받을 수 있는 job이 있으면 받기 
        while len(jobs) > check_job_idx and jobs[check_job_idx].req_time <= time_now:
            heapq.heappush(job_queue, jobs[check_job_idx])
            check_job_idx += 1
        
        # 진행중인 job 처리됐는지 체크
        if cur_job != None:
            if cur_job.is_done(time_now):
                used_times.append(cur_job.get_working_time(time_now))
                cur_job = None
            else:
                # 현재 작업의 끝나는 시점으로 이동
                time_now += cur_job.get_remain_time(time_now)
                continue;
            
        if len(job_queue) > 0:
            # 가동할 수 있는 작업 시작
            cur_job = heapq.heappop(job_queue)
            cur_job.start(time_now)
            time_now += cur_job.need_time
        elif len(jobs) > check_job_idx:
            # 다음 작업을 받을 수 있는 시점으로 이동
            time_now = jobs[check_job_idx].req_time
        else:
            pass
            
    return sum(used_times) // len(used_times)