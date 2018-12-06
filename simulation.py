'''
#   Ian Hecker
#   WGSS201
#   Final Project
#   Passerby-Simulator
#   Purpose: This code is meant to simulate walking by a stranger on the street, and
#   being able to know facts about them. Statistics have been taken from:
#   www.census.gov/quickfacts
#
'''
from scenarios import GeneratePersons

simulation_time = 10

def menu():
    print("Enter a number below, and press enter to execute that option:")
    print("1) Generate Passerby Scenario (1 person)")
    print("2) Generate Bus Scenario (10 persons)")
    print("3) Generate Classroom Scenario (50 persons)")
    print("4) Generate Campus Scenario (14000 persons)")
    print("5) End Program")

def get_input():
    while(True):
        try:
            i = int(input("\n  Type choice here > "))
            return i
        except ValueError:
            print("Entered choice was not an integer")
        except:
            print("Whoops! Unexpected error. Let's try again")


def run_choice(option):
    if option is 1:
        g = GeneratePersons('Passerby')
    elif option is 2:
        g = GeneratePersons('Bus')
    elif option is 3:
        g = GeneratePersons('Classroom')
    elif option is 4:
        g = GeneratePersons('Campus')
    else:
        print('------------------------------------------')
        print('Catch \'ya Later!')
        pass


if __name__ == '__main__':
    #keep track of people objects in array
    people_arr = []

    print('------------------------------------------')
    print("WGSS201 Final Project")
    print("Passerby Simulator")
    print("Ian Hecker\n")

    print("Welcome to the Passerby Simulator! \nThis project is meant to simulate " +
    "what it would be like to walk by \na completely random person on the street, in the U.S., " +
    "and be able \nto instantly know facts about them!\n")

    option_chosen = 0
    while(option_chosen is not 5):
        menu()
        option_chosen = get_input()
        run_choice(option_chosen)
