def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            print("File content:")
            print(file_content)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")


file_path = input("Enter the path of the text file: ")


read_file(file_path)
