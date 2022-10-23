char_dict = ["가방", "마라탕", "나비"]
char_index = ["나비", "다람쥐"]


def is_available_to_order(dict, index):
    for word in index:
        if word not in set(dict):
            return False
    return True


result = is_available_to_order(char_dict, char_index)
print(result)
