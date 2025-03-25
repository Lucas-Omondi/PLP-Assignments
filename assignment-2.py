#Initialize empty list
my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15)
my_list.extend([50, 60, 70])

#remove the last item in the list
my_list.pop()

#sort the list
my_list.sort()

#print the index of a number
print(f"The index of 30 is {my_list.index(30)}")

