def read_lines():
    lines = []
    while True:
        line = input("Enter a line (or press Enter to finish): ")
        if line == "":
            break
        lines.append(line)
    return lines

input_lines = read_lines()

print("You entered:")
for line in input_lines:
    print(line)
