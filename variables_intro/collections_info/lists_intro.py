shopping_list = ["bread", "bananas", "biscuits", "oat milk"]

shopping_list.append("cereal")
print(shopping_list)
shopping_list.append("chocolate")

print(len(shopping_list))

shopping_list.remove("biscuits")
print(shopping_list)

print(shopping_list.pop())
print(shopping_list)

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list)
print(nested_list[1])
print(nested_list[1][-1])  # Should not be nested

# Tuples are IMMUTABLE
# Similar to lists otherwise
# DICTIONARY NAME [ KEY ]
