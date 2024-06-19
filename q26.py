# Specify the file paths
source_file_path = 'myfile.txt'
destination_file_path = 'finalfile.txt'

with open(source_file_path, 'r') as source_file:
    with open(destination_file_path, 'w') as destination_file:

        contents = source_file.read()

        destination_file.write(contents)

