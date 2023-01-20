def fivesums():
    sum = 0

    for i in range(5):
        while True:
            try:
                x = input("Enter int: ")
                y = (int)(x)
                sum += y
                break
            except ValueError:
                print('Invalid input Please enter an int')
    print('your sum is: ', sum)

fivesums()