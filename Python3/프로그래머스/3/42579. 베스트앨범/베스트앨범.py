def solution(genres, plays):
    play_dict = {}
    total_dict = {}
    for idx in range(len(genres)):
        gen = genres[idx]
        cnt = plays[idx]
        
        if gen in play_dict:
            total_dict[gen] += cnt
            play_dict[gen].append((idx, cnt))
        else:
            total_dict[gen] = cnt
            play_dict[gen] = [(idx, cnt)]
    # gen - total_score
    score_list = [(gen, cnt) for gen, cnt in total_dict.items()]
    score_list.sort(key=lambda t: t[1], reverse=True)
    
    answer = []
    for gen, _ in score_list:
        gen_song_list = play_dict[gen]
        gen_song_list.sort(key = lambda t: t[1], reverse=True)
        for idx, (song_idx, _) in enumerate(gen_song_list):
            if idx > 1:
                break
            answer.append(song_idx)
    
    return answer