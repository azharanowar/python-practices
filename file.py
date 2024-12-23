test_file = open('index.html', 'r')
print(test_file.read())

html_file_append = open('index.html', 'a')
html_file_append.write("Hello")
html_file_append.close()

