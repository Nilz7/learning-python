# names = ["Screws", 'Wheels', 'Metal parts', 'Rubber bits', 'Screwdrivers', 'Wood']
# numbers = [43, 12, 95, 421, 23, 43]
# replenish_list = [(name, number) for name,number in zip(names, numbers) if number < 25]
# print(replenish_list)
# combined_list = [[f"{letter}{num}" for num in range(1,9)] for letter in 'ABCDEfGH']
# for row in combined_list:
#     print(row)

# set = {num for num in range(4)}
# print(set)÷
# tuple = tuple(num for num in range(4))
# print(tuple)

# combined_list = list(zip(names, numbers))
# # print(combined_list)
# print(sorted(combined_list, key = lambda item: item[1]))
# print(sorted(combined_list, key = lambda item: len(item[0])))

# power_list = [num ** 2 for num in range(1,6)]
# filter_list = [num for num in range(1,6) if num < 4]
# print(power_list)
# print(filter_list)

with open('tree.txt', 'w') as file:
    file.write('\t  *\n')
    file.write('\t ***\n')
    file.write('\t*****\n')
    file.write('\t  *\n')
    file.write('\t  *\n')
with open('tree.txt', 'r') as file:
    print(file.read())