def factors(number):
    factors_list = []
    for n in range(1, number+1):
        if number % n == 0:
            factors_list.append(n)
    return factors_list


def multiples(n1, n2):
    if n2 in factors(n1):
        return True
    elif n1 in factors(n2):
        return True
    else:
        return False


print(multiples(36, 72))
