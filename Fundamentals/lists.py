age = 19
my_list = ["zesan", age, True]

print(len(my_list))

for i in range(len(my_list)):
    print(my_list[i])

my_list[0] = "Nolin"

my_list.insert(2, False)

for i in range(len(my_list)):
    print(my_list[i])