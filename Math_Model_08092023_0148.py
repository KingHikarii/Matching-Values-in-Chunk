A = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
temp_list = []
list_of_numbers = [1, 1, 1]
matched_list = []
counter = 0

for i in A:

    temp_list = A[counter]
    counter += 1

    for i in range(len(temp_list)):
        if temp_list[i] not in list_of_numbers:
            pass
        else:
            matched_list.append(temp_list[i])

print(matched_list)
print(temp_list)

response = input("Clear? ")
print("You responded with", response)

if response == 'Yes':
    del temp_list[:]

print("This is now your temporary list contents: ", temp_list)
