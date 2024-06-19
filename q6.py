def write_to_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Successfully wrote to file '{file_path}'.")
    except Exception as e:
        print(f"Error occurred while writing to file '{file_path}': {e}")

content = input("Enter the content to write to the file: ")

file_path = input("Enter the path of the text file to write to: ")

write_to_file(file_path, content)

