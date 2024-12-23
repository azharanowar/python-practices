# Using 'with' statement to open and read a file

# with open('data_file/index.html', 'r') as file:
#     content = file.read()
#     print(content)

# No need to explicitly close the file with this approach


with open('data_file/index.html', 'r') as file:
    for line in file:
        print(line.strip())
