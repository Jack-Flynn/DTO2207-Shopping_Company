# High low checker
def high_low_check(question, low_num, high_num):
    error = "Your specified box is outside of our capabilities, please enter a whole number between {} and {}.".format(low_num, high_num)

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


# Finding the volume
def volume_math (num1, num2, num3):
    volume = num1 * num2 * num3
    print("The volume on this box is {}.".format(volume))
    return volume


# Island of return math
def island_of_return(question, num1):
    error = "Please enter either North, South or Stewart"
    while True:
        try:
            response = input(question).title().strip()
            if response == islands[0]:
                print("There will be no difference to your base rate")
                return num1
            elif response == islands[1]:
                print("The base rate has been multiplied by 1.5")
                num1 = num1 * 1.5
                return num1
            elif response == islands[2]:
                print("The base rate has been multiplied by 2")
                num1 = num1 * 2
                return num1
            else:
                print(error)
        except ValueError:
            print(error)


# Number checker
def int_check(question):
    error = "Please enter a number (8 digits or more) without any spaces"
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if response < 10000000:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


def blank_check(question):
    valid = False
    while not valid:
        response = input(question).title().strip()
        if response != "":
            return response
        else:
            print("Your answer cannot be blank, please try again.")


# Ask for the dimensions
height = high_low_check("Please enter the required height.", 5, 100)
width = high_low_check("Please enter the required width.", 5, 100)
depth = high_low_check("Please enter the required depth.", 5, 100)
volume_1 = volume_math(height, width, depth)

# Working out the base rates
if volume_1 <= 6000:
    print("The base rate is $8.00")
    total_cost = 8.00
elif 6000 < volume_1 <= 100000:
    print("The base rate is $12.00")
    total_cost = 12.00
else:
    print("The base rate is $15.00")
    total_cost = 15.00

# Island of return
islands = ['North', 'South', 'Stewart']

# Customer details
first_name = blank_check("What is your first name?")
last_name = blank_check("What is your last name?")
address = blank_check("What is your address?")
phone_number = int_check("What is your phone number?")
details = [first_name, last_name, address, phone_number]
print("Thank you {} {} who lives at {} with the phone number {}, the cost for this is {}"
      .format(details[0], details[1], details[2], details[3], island_of_return("What island are you shipping to?", total_cost)))
