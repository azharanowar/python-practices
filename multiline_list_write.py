lines = [
    "Line 1: Introduction\n"
    "Line 2: Main Content\n"
    "Line 31: Conclusion\n"
]

with open('data_file/story_format.txt', 'w') as file:
    file.writelines(lines)