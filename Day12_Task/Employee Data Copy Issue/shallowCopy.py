import copy

employees = [[101, "A"], [102, "B"], [103, "C"]]

shallow = copy.copy(employees)

employees[0][1] = "z"

print("Original:", employees)
print("Shallow Copy:", shallow)