# Number checker
def int_check(question, low_num, high_num):
    error = "Your specified box is outside of our capabilities, please enter a whole number between {} and {}".format(low_num, high_num)

    valid = False
    while not valid:
        try:
            response = int(input(question))
            if low_num <= response <= high_num:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


def volume_math (num1, num2, num3):
    volume = num1 * num2 * num3
    print("the volume is {}".format(volume))


# Ask for the dimensions
height = int_check("Please enter the required height", 5, 100)
width = int_check("Please enter the required width", 5, 100)
depth = int_check("Please enter the required depth", 5, 100)

volume_math(height, width, depth)

