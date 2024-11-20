def check(character):
    if character.isalpha():
        if character.isupper():
            return f"'{character}' is an uppercase alphabe."
        else:
            return f"'{character}' is an lowercase alphabet."
    else:
        return f"'{character}'is not an alphabet."
user_input = input("illyas:")
result = check(user_input)
print(result)
