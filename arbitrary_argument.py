# Taking unlimited arguments value for function perameter
def make_pizza(*toppings):
    print("Pizza order completed, here is the toppings: ")
    for topping in toppings:
        print(topping.title())

make_pizza("Mushrooms", "green peppers", "extra cheese")
make_pizza()
make_pizza("Kicu lagbe na")


# # Taking unlimited arguments with key-value for function perameter
# def student_info(**info):
#     student_info = {}
#     print("Here is the details of new student: ")
#     for item in info.items():
#         student_info[item[0]] = item[1]
#         print(item)
#         print(item[0])
#         print(item[1])
#     print(student_info)
# student_info(name="Anowar", id="20243204", age=24, )



# Taking unlimited arguments with key-value for function perameter
def student_info(first_name, last_name, **info):
    student_info = {}
    print("Here is the details of new student: ")
    student_info['first_name'] = first_name
    student_info['last_name'] = last_name
    for item in info.items():
        student_info[item[0]] = item[1]
        print(item[0])
        print(item[1])
    print(student_info)

    
student_info("Azhar", "Anowar", id="20243204", age=24, department="CSE")