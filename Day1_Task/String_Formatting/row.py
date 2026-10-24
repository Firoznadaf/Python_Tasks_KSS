#  Print a table row using formatted strings.

name = "Firoz"
age = 20
marks = 89.5

print(f"{'Name':<10}{'Age':<10}{'Marks':<10}")
print("-" * 30)
print(f"{name:<10}{age:<10}{marks:<10.2f}")