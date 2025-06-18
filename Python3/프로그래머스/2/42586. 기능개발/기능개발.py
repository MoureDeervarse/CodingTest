def solution(progresses, speeds):
    deploy_indices = []
    used_days = 0
    
    for idx, progress in enumerate(progresses):
        remain_progress = 100 - progress
        
        need_days, remainder = divmod(remain_progress, speeds[idx])
        if remainder > 0:
            need_days += 1
        
        if used_days < need_days:
            # need more days
            used_days = need_days
            deploy_indices.append(1)
        else:
            # deploy with others
            deploy_indices[len(deploy_indices) - 1] += 1
        
    return deploy_indices