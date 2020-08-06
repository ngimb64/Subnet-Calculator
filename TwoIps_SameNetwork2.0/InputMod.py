def main_input(message):
    while True:
        try:
            user_input = int(input(message))
            if user_input < 000:
                print('Please enter a number between' \
                        ' 000 and 255.')
                continue
            elif user_input > 255:
                print('Please enter a number between' \
                        ' 000 and 255.')
                continue
        except ValueError:
            print('Please enter a number between' \
                    ' 000 and 255.')
            continue
        else:
            return user_input

def alt_input(message):
    while True:
        try:
            user_input = int(input(message))
            if user_input < 000:
                print('Please enter a number between' \
                        ' 000 and 254.')
                continue
            elif user_input > 254:
                print('Please enter a number between' \
                        ' 000 and 254.')
                continue
        except ValueError:
            print('Please enter a number between' \
                    ' 000 and 254.')
            continue
        else:
            return user_input

def sub_input(message):
    while True:
        try:
            user_input = int(input(message))
            if not user_input == 255:
                print('Please enter 255.')
                continue
        except ValueError:
            print('Please enter 255.')
            continue
        else:
            return user_input

def cidr_input(message):
    options = [0, 128, 192, 224, 240, 248, \
                252, 254, 255]
    while True:
        try:
            user_input = int(input(message))
            if user_input in options:
                return user_input
                break
            else:
                print('Please enter one of the' \
                        ' specified values.')
                continue
        except ValueError:
            print('Please enter one of the' \
                    'specified values.')
            continue
        else:
            return user_input