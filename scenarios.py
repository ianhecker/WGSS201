from person import Person

class GeneratePersons:
    def __init__(self, scenario):
        self.scenario = scenario
        self.population = self.determine_pop(scenario)
        self.people = []

        self.generate_persons()
        self.print_scenario()

    def determine_pop(self, scenario):
        population = {
            "Passerby": 1,
            "Bus": 10,
            "Classroom": 50,
            "Campus": 14000
        }
        return population[scenario]


    def generate_persons(self):
        for i in range(self.population):
            p = Person()
            self.people.append(p)

    def print_scenario(self):
        print('------------------------------------------')
        print("Simulation: " + self.scenario)
        print("Population: " + str(self.population))
        print("People Data:")
        if self.scenario is not 'Campus':
            for p in self.people:
                a = str(p.get_age())
                s = str(p.get_sex())
                sx = str(p.get_sexuality())
                print("Age: %s Sex: %s Sexuality: %s" %
                (a, s, sx))
        print('\n\n')
