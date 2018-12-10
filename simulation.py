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
    print("1) Generate Passerby Scenario  (1 person)")
    print("2) Generate Bus Scenario       (10 persons)")
    print("3) Generate Classroom Scenario (50 persons)")
    print("4) Generate Bar Scenario       (200 persons)")
    print("5) Generate Campus Scenario    (14000 persons)")
    print("6) Generate City Scenario      (50000 persons)")
    print("0) End Program")

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
        g = GeneratePersons('Bar', s)
    elif option is 5:
        g = GeneratePersons('Campus', s)
    elif option is 6:
        g = GeneratePersons('City', s)
    else:
        print("--------------------------------------------------------------------------------------------------------------")
        print('Catch \'ya Later!')
        pass


if __name__ == '__main__':
    #keep track of people objects in array
    people_arr = []

    print("--------------------------------------------------------------------------------------------------------------")
    print("  WGSS201 Final Project")
    print("  Passerby Simulator")
    print("  Ian Hecker\n")

    print("  Welcome to the Passerby Simulator! \n  This project is meant to simulate " +
    "what it would be like to walk by \n  a completely random person on the street, in the U.S., " +
    "and be able \n  to instantly know facts about them!\n")

    print("  IMPORTANT:")
    print("  This program takes data from a nationwide census with random sampling. Scenarios will")
    print("  most likely not be representative of ACTUAL real-life situations. This is due to SPECIFIC")
    print("  REGIONS/LOCATIONS of the United States containing stronger/weaker proportions of individuals")
    print("  and their respective traits, such as age, race, ethnicity, sex, LGBT or Intersex status.")
    print("  It IS however representative of the entire population of the United States.")

    print("\n\n  *Clarifying The US Census:*")
    print("  ---------------------------")
    print("  Sexuality:")
    print("  The US Census does not collect data on sexuality or intersex\n  LGBT Statistics are" +
    "  taken from the following sources:")
    print("--------------------------------------------------------------------------------------------------------------")
    print("  + Gallup Poll 2017 U.S. Adult LGBT-Identifying Population Estimate: %s%%" % (s.GP_US_ADULT_LGBT*100))
    print("--------------------------------------------------------------------------------------------------------------")
    print("  Intersex Statistics are taken from the following sources:")
    print("--------------------------------------------------------------------------------------------------------------")
    print("  + Intersex Society of North America Intersex Estimate %s%%" % (s.ISNA_INTERSEX*100))
    print("--------------------------------------------------------------------------------------------------------------")
    print("  Race:")
    print("  The US Census treats persons of Hispanic descent as an ethnicity, and\n" +
    "  therefore has collected data on the premise that any of the following races \n" +
    "  can be of Hispanic ethnicity.")
    print("  The US Census categorizes races in its census data as ancestral descent from these countries:\n")
    print("|------------------------------------------------------------------------------------------------------------|")
    print("|              |        |                         |                | Native Hawaiian or     |                |")
    print("| White        | Black  | Native American/Alaskan | Asian          | Other Pacific Islander | Two/More races |")
    print("|------------------------------------------------------------------------------------------------------------|")
    print("| Europe       | Africa | North America           | Far East       | Hawaii                 |                |")
    print("| Middle East  |        | South America           | Southeast Asia | Guam                   |                |")
    print("| North Africa |        | Central America         | Indian         | Samoa                  |                |")
    print("|              |        |                         |                | Pacific Islands        |                |")
    print("|------------------------------------------------------------------------------------------------------------|")
    print('\n')

    option_chosen = 69
    while(option_chosen is not 0):
        menu()
        option_chosen = get_input()
        run_choice(option_chosen)
