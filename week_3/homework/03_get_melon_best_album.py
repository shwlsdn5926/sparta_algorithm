genres = ["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"]
plays = [2000, 500, 600, 150, 800, 2500, 2000]


def get_melon_best_album(genre_array, play_array):
    plays_num_dict = {}
    plays_index_dict = {}
    for i in range(len(genre_array)):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in plays_num_dict:
            plays_num_dict[genre] = play
            plays_index_dict[genre] = [[i, play]]
        else:
            plays_num_dict[genre] += play
            plays_index_dict[genre].append([i, play])
    print(plays_num_dict.items())
    sorted_plays_num_dict = sorted(plays_num_dict.items(), key=lambda item: item[1], reverse=True)
    result = []
    for g, p in sorted_plays_num_dict:
        index_play = plays_index_dict[g]
        sorted_plays_index = sorted(index_play, key=lambda item: item[1], reverse=True)
        for i in range(len(sorted_plays_index)):
            if i > 1:
                break
            result.append(sorted_plays_index[i][0])
    return result


print(get_melon_best_album(genres, plays))
