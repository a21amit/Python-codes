def LinearSearch(input_list: list, element: int):
    list_len = len(input_list)
    for i in range(list_len):
        if input_list[i] == element:
            return i
    return -1
#reading list
#can be asked from user(optional)
myList = [1, 23, 45, 23, 34, 56, 12, 45, 67, 24]
print("Given list is:", myList)
position = LinearSearch(myList, 12)
print("Element 12 is at position:", position)
