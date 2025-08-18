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

# with open('tree.txt', 'w') as file:
#     file.write('\t  *\n')
#     file.write('\t ***\n')
#     file.write('\t*****\n')
#     file.write('\t  *\n')
#     file.write('\t  *\n')
# with open('tree.txt', 'r') as file:
#     print(file.read())

# x = 1
# y = 1
# z = 1
# inputs = [x,y,z]
# n = 2

# list_num = [[i,j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n]
# print(list_num)

# n = 5
# arr = map(int, '2 3 6 6 5'.split())
# my_list = list(arr)
# my_list.sort(reverse=True)
# print(my_list)
# runner_score = 0
# high_score = my_list[0]
# for index,num in enumerate(my_list):
#     if num == high_score: continue
#     runner_score = num
#     break
# print(runner_score)

    