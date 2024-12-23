# Return all lines as a list of object with readlines()

with open('data_file/data_items.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())


print(lines)
print(type(lines))

