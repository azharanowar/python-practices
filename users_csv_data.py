import csv
import os



file_path = 'data_file/users.csv'

# Writing in CSV
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
user_city = input("Enter your city: ")

file_path = 'data_file/users.csv'

if os.path.isfile(file_path):
    with open(file_path, 'a') as file:
        user_data = [user_name, user_age, user_city]
        write_file = csv.writer(file)
        write_file.writerow(user_data)

else:
    with open(file_path, 'w') as file:
        user_data_title = ["Name", "Age", "City"]
        user_data = [user_name, user_age, user_city]
        write_file = csv.writer(file)
        write_file.writerow(user_data_title)
        write_file.writerow(user_data)


with open(file_path, 'r') as file:
    content = csv.reader(file)
    for row in content:
        print(row)