from person import Person

class GeneratePersons:
    def __init__(self, scenario, statistics_instance):
        self.scenario = scenario
        self.population = self.determine_pop(scenario)
        self.people = []
        self.s = statistics_instance

        self.generate_persons(self.s)
        self.print_scenario()

    def determine_pop(self, scenario):
        population = {
            "Passerby": 1,
            "Bus": 10,
            "Classroom": 50,
            "Campus": 14000
        }
        return population[scenario]


    def generate_persons(self, s):
        for i in range(self.population):
            p = Person(s)
            self.people.append(p)

    def print_scenario(self):
        print('------------------------------------------')
        print("Simulation: " + self.scenario)
        print("Population: " + str(self.population))
        print("People Data:")

        if self.scenario is not 'Campus':
            print('\nAge Sex    LGBT   Hispanic Race')
            for p in self.people:
                a = p.get_age()
                s = p.get_sex()
                sx = p.get_LGBT()
                h = p.get_hispanic()
                r = p.get_race()
                print('%-3s %-6s %-6s %-8s %s' % (a, s, sx, h, r))

        print('\n\n')
