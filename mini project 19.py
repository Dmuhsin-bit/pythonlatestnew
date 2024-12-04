def count_file_contents(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = 0
            char_count = 0
            for line in lines:
                words = line.split()
                word_count += len(words)
                char_count += len(line)

            return line_count, word_count, char_count
    except FileNotFoundError:
        print(f"The file at '{file_path}' was not found.")
        return None
file_path = "example.txt"
result = count_file_contents(file_path)
if result:
    line_count, word_count, char_count = result
    print(f"Lines: {line_count}, Words: {word_count}, Characters: {char_count}")
