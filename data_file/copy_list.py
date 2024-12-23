def modify_list(input_list):
    input_list.append("new_item")
original_list=["item1", "item2", "item3"]
modify_list(original_list[:])
print(original_list)