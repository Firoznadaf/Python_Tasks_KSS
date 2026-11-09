"""Common Elements Using Sets: Given two lists:
    python
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    Find:
    * Common elements.
    * Elements present only in the first list.
    * All unique elements from both lists."""

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

set1 = set(list1)
set2 = set(list2)

#Common elements
common = set1.intersection(set2)

# Elements only in first list
first = set1.difference(set2)

# All unique elements
unique = set1.union(set2)

print("Common elements:", common)
print("First list:", first)
print("Unique elements:", unique)
