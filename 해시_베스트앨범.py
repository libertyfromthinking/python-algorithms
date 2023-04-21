from collections import defaultdict
from operator import itemgetter


def solution(genres, plays):
    genre_dict = {}
    play_dict = defaultdict(list)
    idx = 0
    answer = []

    for genre, play, idx in zip(genres, plays, range(len(genres))):
        genre_dict[genre] = genre_dict.get(genre, 0) + play
        play_dict[genre].append([-play, idx])

    genre_list = sorted(genre_dict.items(), reverse=True, key=itemgetter(1))

    play_dict = dict(play_dict)
    for i in play_dict:
        play_dict[i].sort(key=itemgetter(0, 1))

    for i in genre_list:
        answer.append(play_dict[i[0]][0][1])
        if len(play_dict[i[0]]) > 1:
            answer.append(play_dict[i[0]][1][1])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 500, 800, 2500]))