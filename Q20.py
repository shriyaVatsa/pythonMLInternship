import string

def remove_punctuation(input_string):
    translator = str.maketrans('', '', string.punctuation)
    return input_string.translate(translator)

input_string = "Hello, World! This is an example: Python's capabilities are great."

clean_string = remove_punctuation(input_string)

print("Original string:", input_string)
print("String without punctuation:", clean_string)

