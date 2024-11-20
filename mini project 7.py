def removeodd_index_chara(sahal):
    result = ""

    for index, chara in enumerate(sahal):
        if index %2 == 0:
            result += chara

    return result
user_input = input("sahal:")

