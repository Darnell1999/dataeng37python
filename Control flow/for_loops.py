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


# current_number = 1
# max_number = int(input("What number would you like to play up to"))
# while current_number <= max_number:
#     if current_number % 3 != 0 and current_number % 5 != 0:
#         print(current_number)
#     elif current_number % 15 == 0:
#         print("FizzBuzz")
#     elif current_number % 3 == 0:
#         print("Fizz")
#     elif current_number % 5 == 0:
#         print("Buzz")
#     current_number += 1


invalid = True
while invalid:
    games = input("How many games do you want to play?")
    if games.isdigit():
        games = int(games)
        print("Cool let's play")
        invalid1 = True
        while invalid1:
            max_number = input("What number would you like to play up to")
            if max_number.isdigit():
                max_number = int(max_number)
                print("Cool let's play")
                invalid1 = invalid = False
            else:
                print("Please enter a valid answer")
    else:
        print("Please enter a valid answer")
    game_number = 0
    current_number = 1
while game_number < games:
    print(f"This is game number {game_number+1}")
    while current_number <= max_number:
        if current_number % 3 != 0 and current_number % 5 != 0:
            print(current_number)
        elif current_number % 15 == 0:
            print("FizzBuzz")
        elif current_number % 3 == 0:
            print("Fizz")
        elif current_number % 5 == 0:
            print("Buzz")
        current_number += 1
    game_number += 1
    current_number = 0
print("Thanks for playing with me")




