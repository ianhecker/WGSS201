from statistics import Statistics

class Person:

    def __init__(self):
        self.data = {
            'age': None,
            'sex': None,
            'race': None,
            'sexuality': None,
            'class': None
        }
        self.s = Statistics()
        #--------------------
        self.init_age()
        self.init_sex(self.data['age'])
        self.init_sexuality()

    def init_age(self):
        self.data['age'] = self.s.return_age()

    def init_sex(self, age):
        self.data['sex'] = self.s.return_sex(age)

    def init_race(self):
        pass

    def init_sexuality(self):
        sx = self.s.return_sexuality()
        if sx:
            self.data['sexuality'] = 'LGBT'
        else:
            self.data['sexuality'] = 'Non-LGBT'

    def init_class(self):
        pass


    def get_age(self):
        return self.data['age']

    def get_sex(self):
        return self.data['sex']

    def get_sexuality(self):
        return self.data['sexuality']
