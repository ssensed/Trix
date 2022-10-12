def give_numbers():
    three_numbers = input("give me three numbers")
    bites = three_numbers.split()
    print(type(bites))

    if len(bites) == 3:
        num1 = int(bites[0])
        num2 = int(bites[1])
        num3 = int(bites[2])
        all_num = num1 + num2 + num3

    if num1 in range(257) and num2 in range(257) and num3 in range(257):
        print("ja, alle tallene er mellom 0 og 256")

    else:
        print("nei, ikke alle tallene er mellom 0 og 256")


give_numbers()
