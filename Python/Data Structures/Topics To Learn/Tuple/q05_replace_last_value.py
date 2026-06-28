collection_of_groups = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print("Original setup:", collection_of_groups)

updated_groups = []

for single_group in collection_of_groups:
    group_as_list = list(single_group)
    group_as_list[-1] = 100
    group_as_tuple = tuple(group_as_list)
    updated_groups.append(group_as_tuple)

print("Setup after replacing the last numbers with 100:", updated_groups)
