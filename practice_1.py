file_path = 'data_file/quotes.txt'
with open(file_path, 'r') as file:
    line_no = 1
    for quote in file:
        print(f"{line_no}. {quote.strip()}")
        line_no += 1
