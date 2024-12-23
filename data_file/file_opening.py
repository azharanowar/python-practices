# Opening a file in read mode

file = open('example_1.txt', 'r') # The location will start from main folder not here...

content = file.read()
print(content)


# Closing the file at the end of work...
file.close()