# alphabet = ["A", "B", "C", "D", "E"]
#
# for letter in alphabet:
#     print(letter.lower())

# nest = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
#
# for ssdf in nest:
#     for sjkhkf in ssdf:
#         print(sjkhkf)

# team_home = {
# 'Arsenal': 'The Carpet',
# 'Man City': 'The Emptyhad',
# 'Tottenham': 'Sh*te Hart Lane',
# 'Man Utd': 'Theatre of Nightmares'
# }
#
# for team in team_home.values():
#     print(team)


current_number = 1
while current_number <100:
    if current_number % 3 != 0 and current_number % 5 != 0:
        print(current_number)
    elif current_number % 15 == 0:
        print("FizzBuzz")
    elif current_number % 3 == 0:
        print("Fizz")
    elif current_number % 5 == 0:
        print("Buzz")
    current_number += 1
