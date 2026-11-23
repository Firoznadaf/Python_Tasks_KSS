import copy

employees = [[101, "A"], [102, "B"], [103, "C"]]

deep = copy.deepcopy(employees)

employees[0][1] = "z"

print("Original:", employees)
print("Deep Copy:", deep)