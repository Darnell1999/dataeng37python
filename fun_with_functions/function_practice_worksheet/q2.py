def letter_position(letter):

    alphabet = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    return alphabet.index(letter)


def name_index(name):
    index = []
    for char in name:
        ind = str(letter_position(char))
        index.append(ind)
    new_string = "".join(index)
    return new_string


def password(identification):
    total = 0
    index_list = []
    for letter in identification:
        pos = letter_position(letter)
        index_list.append(pos)
        total += pos
    max = int(name_index(identification))
    password = max - total
    return password

print(password("darnell"))