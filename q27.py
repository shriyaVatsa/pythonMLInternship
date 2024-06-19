input_string = "Hello, World!"

prefix = "Hello"
suffix = "World!"

starts_with = input_string.startswith(prefix)

ends_with = input_string.endswith(suffix)

print(f"Does the string '{input_string}' start with '{prefix}'? {starts_with}")
print(f"Does the string '{input_string}' end with '{suffix}'? {ends_with}")
