import os
def check_and_append(file_path, text_to_append):
    try:
        if os.path.exists(file_path):
            with open(file_path, 'a') as file:
                file.write(text_to_append + '\n')
            print(f"Text appended to '{file_path}'.")
        else:
            print(f"File '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = "example.txt"
text_to_append = "This is the text to append."
check_and_append(file_path, text_to_append)
