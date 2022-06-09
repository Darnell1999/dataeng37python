def factors(number):
    factors_list = []
    for n in range(1, number+1):
        if number % n == 0:
            factors_list.append(n)
    return factors_list


keep_asking = True
while keep_asking:
    integer = input("What number do you want to check?")
    if integer.isdigit():
        keep_asking = False

        def prime(integer):
            factors(integer)
            if len(factors(integer)) == 2:
                return True
            else:
                return False
    else:
        print("Enter a valid number")


print(prime(int(integer)))
