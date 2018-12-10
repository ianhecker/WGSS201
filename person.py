from statistics import Statistics

class Person:

    def __init__(self, statistics_instance):
        self.data = {
            'age': None,
            'sex': None,
            'race': None,
            'LGBT': None,
            'hispanic': None
        }
        self.s = statistics_instance
        #--------------------
        self.init_age()
        self.init_sex(self.data['age'])
        self.init_LGBT()
        self.init_hispanic(self.data['age'], self.data['sex'])
        self.init_race(self.data['age'], self.data['sex'], self.data['hispanic'])


    def init_age(self):
        self.data['age'] = self.s.return_age()

    def init_sex(self, age):
        self.data['sex'] = self.s.return_sex(age)

    def init_LGBT(self):
        self.data['LGBT'] = self.s.return_LGBT()

    def init_hispanic(self, age, sex):
        self.data['hispanic'] = self.s.return_hispanic(age, sex)

    def init_race(self, age, sex, hispanic):
        self.data['race'] = self.s.return_race(age, sex, hispanic)
    #----------------------------------------------------------


    def get_age(self):
        return self.data['age']

    def get_sex(self):
        return self.data['sex']

    def get_LGBT(self):
        return self.data['LGBT']

    def get_hispanic(self):
        return self.data['hispanic']

    def get_race(self):
        return self.data['race']
