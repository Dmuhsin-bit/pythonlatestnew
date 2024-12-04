def copy_file_contents(source_file, destination_file):
    try:
        with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
            dest.write(src.read())
        print(f"Contents copied from '{source_file}' to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"File not found: '{source_file}'")
    except Exception as e:
        print(f"An error occurred: {e}")

source_file = "source.txt"
destination_file = "destination.txt"
copy_file_contents(source_file, destination_file)
