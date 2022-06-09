# def greeting(name= "Default Output"):
#     return "Hello " + name
#
# print(greeting())
#
#
# result = greeting("Lizzy")
# print(result)
#
# def multiargs(*args):

# def product(*numbers):
#     for number in numbers:
#         total *= number
#     yield number
#
#
# print(product(1, 2, 3))

# def product(*numbers):
#     if len(numbers) == 0:
#         return None
#     result = 1
#     for number in numbers:
#         result *= number
#     return result
#
#
# print(product())

# def kwargs_demo(**kwargs)
#     print(kwargs, type(kwargs))
#
#
# print(kwargs_demo(a="One", b="Two"))

# def calculate_tip(list_of_meals, total_cost, tip_pc):
#     print("You had:")
#     for meal in list_of_meals:
#         print(meal)
#     print(f"Your subtotal is: {total_cost}")
#     print(f"With a {tip_pc:.0%"})

# def calculate_total_cost(**meal_prices):
#     result = 0
#     for meal in meal_prices.values():
#         result += meal
#     return result
#     # return sum(meal_prices.values())
#
#
#
# print(calculate_total_cost(
#     Pizza=8.50,
#     Burger=9.00,
#     Hot_Dog=9.00,
#     chips=3.00
# ))

# Good Functions
# - Name them clearly, lowercase_with_underscores
# - Clear argument names
# - Functions that don't RETURN something return None
# - Keep them small
# - Use comments
# - Consider type hints

def fizzbuzz_line(number: int):
    if number % 15 == 0:
        return "Fizzbuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number


def fizzbuzz_game():
    for i in range(1, 101):
        print(fizzbuzz_line(i))


print(fizzbuzz_game())


