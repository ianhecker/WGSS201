'''
#   Ian Hecker
#   WGSS201
#   Final Project
#   Passerby-Simulator
'''
from scenarios import GeneratePersons
from statistics import Statistics

simulation_time = 10

s = Statistics()

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
            i = int(input("\nSelection > "))
            return i
        except ValueError:
            print("Entered choice was not an integer")
        except:
            print("Whoops! Unexpected error. Let's try again")


def run_choice(option):
    if option is 1:
        g = GeneratePersons('Passerby', s)
    elif option is 2:
        g = GeneratePersons('Bus', s)
    elif option is 3:
        g = GeneratePersons('Classroom', s)
    elif option is 4:
        g = GeneratePersons('Campus', s)
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

    print("  Clarifying The US Census:")
    print("  Sexuality:")
    print("  The US Census does not collect data on sexuality. LGBT Statistics are \n" +
    "  taken from the following sources:")
    print("------------------------------------------------------------------------------")
    print("  + Gallup Poll 2017 LGBT Identifying-Adult Population Estimate for U.S.: %s%%" % (s.GP_US_ADULT_LGBT*100))
    print()
    print("  Race:")
    print("  The US Census treats persons of Hispanic descent as an ethnicity, and\n " +
    "  therefore has collected data on the premise that any of the following races \n " +
    "  can be of Hispanic ethnicity.")
    print("  The US Census categorizes races in its census data as ancestral descent from these countries:")
    print("|------------------------------------------------------------------------------------------------------------|")
    print("|              |        |                         |                | Native Hawaiian or     |                |")
    print("| White        | Black  | Native American/Alaskan | Asian          | Other Pacific Islander | Two/More races |")
    print("|------------------------------------------------------------------------------------------------------------|")
    print("| Europe       | Africa | North America           | Far East       | Hawaii                 |                |")
    print("| Middle East  |        | South America           | Southeast Asia | Guam                   |                |")
    print("| North Africa |        | Central America         | Indian         | Samoa                  |                |")
    print("|              |        |                         |                | Pacific Islands        |                |")
    print("|------------------------------------------------------------------------------------------------------------|")
    print('\n\n')

    option_chosen = 0
    while(option_chosen is not 5):
        menu()
        option_chosen = get_input()
        run_choice(option_chosen)
