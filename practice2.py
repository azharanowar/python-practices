import os
name = input("Enter your name: ")
file_path = ('data_file/user_data.txt')

# If file exits then append or create a new file - To avoid replacing of file everytime with w mode
if os.path.isfile(file_path):
    with open(file_path, 'a') as file:
        file.write(name + '\n')
else:
    with open(file_path, 'w') as file:
        file.write(name + '\n')