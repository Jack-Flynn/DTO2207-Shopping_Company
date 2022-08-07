# Number checker
def int_check(question, low_num, high_num):
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


def island_of_return(question, num1):
    error = "Please enter either North, South or Stewart"
    while True:
        try:
            response = input(question).title()
            if response == islands[0]:
                print("There will be no difference to your base rate")
                return response
            elif response == islands[1]:
                print("The base rate has been multiplied by 1.5")
                num1 = num1 * 1.5
                print(num1)
                return response
            elif response == islands[2]:
                print("The base rate has been multiplied by 2")
                num1 = num1 * 2
                print(num1)
                return response
            else:
                print(error)
        except ValueError:
            print(error)


# Ask for the dimensions
height = int_check("Please enter the required height.", 5, 100)
width = int_check("Please enter the required width.", 5, 100)
depth = int_check("Please enter the required depth.", 5, 100)
volume_1 = volume_math(height, width, depth)

# Working out the base rates
if volume_1 <= 6000:
    print("The base rate is $8.00")
    base_rate = 8.00
elif 6000 < volume_1 <= 100000:
    print("The base rate is $12.00")
    base_rate = 12.00
else:
    print("The base rate is $15.00")
    base_rate = 15.00

# Island of return
islands = ['North', 'South', 'Stewart']
island_of_return("What island are you shipping to?", base_rate)
print(base_rate)
