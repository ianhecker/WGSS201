from person import Person
import re

class GeneratePersons:
    def __init__(self, scenario, statistics_instance):
        self.scenario = scenario
        self.population = self.determine_pop(scenario)
        self.people = []
        self.s = statistics_instance
        self.sim_stats = {
            'mean_age': None,
            'median_age': None,
            'oldest': None,
            'youngest': None,
            'st_dev_age': None,
            'male_p': None,
            'female_p': None,
            'intersex_p': None,
            'w_p': None,
            'b_p': None,
            'na_p': None,
            'a_p': None,
            'ni_p': None,
            't_p': None,
            'his_p': None,
            'LGBT_p': None
        }

        self.generate_persons(self.s)
        self.collect_stats(self.people)
        self.print_scenario()

    def determine_pop(self, scenario):
        population = {
            "Passerby": 1,
            "Bus": 10,
            "Classroom": 50,
            "Bar":200,
            "Campus": 14000,
            "City": 50000
        }
        return population[scenario]

    def generate_persons(self, s):
        for i in range(self.population):
            p = Person(s)
            self.people.append(p)

    def collect_stats(self, people):
        #Sort by Age
        self.call_quicksort(people)
        people_amount = len(people)
        tmp = 0
        #Mean
        for p in self.people:
            tmp += p.data['age']
        self.sim_stats['mean_age'] = tmp / people_amount
        #Median
        middle_index = int(people_amount/2)
        self.sim_stats['median_age'] = people[middle_index].data['age']
        #Oldest
        self.sim_stats['oldest'] = people[people_amount-1].data['age']
        #Youngest
        self.sim_stats['youngest'] = people[0].data['age']
        #standard deviation of age
        self.sim_stats['st_dev_age'] = self.std_dev(people, self.sim_stats['mean_age'])

        female_proportion = 0
        intersex_proportion = 0
        his_proportion = 0
        LGBT_proportion = 0
        w_proportion = 0
        b_proportion = 0
        na_proportion = 0
        a_proportion = 0
        ni_proportion = 0
        t_proportion = 0

        for p in people:
            if p.data['sex'] is 'Female':
                female_proportion += 1
            if p.data['intersex'] is True:
                intersex_proportion += 1
            if p.data['hispanic'] is True:
                his_proportion += 1
            if p.data['LGBT'] is True:
                LGBT_proportion += 1
            if p.data['race'] is 'White':
                w_proportion += 1
            elif p.data['race'] is 'Black':
                b_proportion += 1
            elif re.search('American', p.data['race']):
                na_proportion += 1
            elif p.data['race'] is 'Asian':
                a_proportion += 1
            elif re.search('Hawaiian', p.data['race']):
                ni_proportion += 1
            elif re.search('Two', p.data['race']):
                t_proportion += 1

        #Female proportion
        self.sim_stats['female_p'] = (female_proportion / people_amount)
        #Male proportion
        self.sim_stats['male_p'] = (1 - (female_proportion / people_amount))
        #Intersex proportion
        self.sim_stats['intersex_p'] = (intersex_proportion / people_amount)
        #LGBT proportion
        self.sim_stats['LGBT_p'] = (LGBT_proportion / people_amount)
        #Hispanic Proportion
        self.sim_stats['his_p'] = (his_proportion / people_amount)
        #White proportion
        self.sim_stats['w_p'] = (w_proportion / people_amount)
        #Black proportion
        self.sim_stats['b_p'] = (b_proportion / people_amount)
        #Native American/Alaskan proportion
        self.sim_stats['na_p'] = (na_proportion / people_amount)
        #Asian proportion
        self.sim_stats['a_p'] = (a_proportion / people_amount)
        #Native Hawaiian/Other Pacific Islander proportion
        self.sim_stats['ni_p'] = (ni_proportion / people_amount)
        #Two Or More Races proportion
        self.sim_stats['t_p'] = (t_proportion / people_amount)

    def std_dev(self, people_array, mean):
        squared_sum = 0
        n = len(people_array)
        for i in range(n):
            squared_sum += (people_array[i].data['age'] - mean)**2
        return ((squared_sum / n)**0.5)

    def call_quicksort(self, people):
        n = len(people)
        self.quicksort(people, 0, n-1)

    def partition(self, array, low, high):
        i = (low - 1)
        pivot = array[high].data['age']
        for j in range(low, high):
            if array[j].data['age'] <= pivot:
                i = i + 1
                array[i], array[j] = array[j], array[i]

        array[i + 1], array[high] = array[high], array[i + 1]
        return(i + 1)

    def quicksort(self, array, low, high):
        if low < high:
            p = self.partition(array, low, high)
            self.quicksort(array, low, p - 1)
            self.quicksort(array, p + 1, high)


    def print_scenario(self):
        print("\n\nSimulation: " + self.scenario)
        print("Population: " + str(self.population))

        if self.scenario is not 'Campus' and self.scenario is not 'City':
            print('\nSimulated People Raw Data')
            print('\nAge Sex    LGBT   Intersex Hispanic Race')
            print('----------------------------------------')
            for p in self.people:
                a = p.get_age()
                s = p.get_sex()
                l = p.get_LGBT()
                h = p.get_hispanic()
                r = p.get_race()
                i = p.get_intersex()
                print('%-3s %-6s %-6s %-8s %-8s %s' % (a, s, l, i, h, r))

        m =    self.sim_stats['mean_age']
        md =   self.sim_stats['median_age']
        s_d =  self.sim_stats['st_dev_age']
        o =    self.sim_stats['oldest']
        y =    self.sim_stats['youngest']
        ma =   self.sim_stats['male_p']
        fm =   self.sim_stats['female_p']
        hs =   self.sim_stats['his_p']
        lgbt = self.sim_stats['LGBT_p']
        ix =   self.sim_stats['intersex_p']
        w =    self.sim_stats['w_p']
        b =    self.sim_stats['b_p']
        na =   self.sim_stats['na_p']
        a =    self.sim_stats['a_p']
        ni =   self.sim_stats['ni_p']
        t =    self.sim_stats['t_p']

        print('\nSimulation Statistics')
        print('---------------------')
        print('Age:\nMean: %-.5fyrs Median: %syrs Standard_Dev: %-.5fyrs' % (m, md, s_d))
        print('Oldest: %-3s Youngest: %-3s' % (o, y))
        print('\nRace Proportions:\nHispanic Proprotion %-.5f' % hs)
        print('White: %-.5f Black: %-.5f Native American/Alaskan: %-.5f' % (w, b, na))
        print('Asian: %-.5f Native Hawaiian/Other Pacific Islander: %-.5f Two Or More Races: %-.5f' % (a, ni, t))
        print('\nLGBT & Intersex Proportions\nLGBT: %-.5f Intersex %-.5f' % (lgbt, ix))

        print('\n\n')
