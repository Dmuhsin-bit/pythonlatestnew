def check_input_type(illyas):
    if illyas.isdigit():
        return f"'{illyas}' is a integer."
    elif illyas.isalpha():
        return f"'{illyas}' is a string"

illyas = input("illyas is cute:")
result = check_input_type(illyas)
print(result)
