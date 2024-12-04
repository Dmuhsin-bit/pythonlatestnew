def find_and_replace(file_path, target_word, replacement_word):
    try:
        with open(file_path, 'r+') as file:
            content = file.read()
            content = content.replace(target_word, replacement_word)
            file.seek(0)
            file.write(content)
        print(f"Replaced '{target_word}' with '{replacement_word}'.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
find_and_replace("example.txt", "oldword", "newword")
