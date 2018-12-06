from statistics import Statistics

class Person:

    def __init__(self):
        self.data = {
            'age': None,
            'ethnicity': None,
            'first_name': None,
            'last_name': None,
            'sexuality': None,
            'class': None
        }
        self.s = Statistics()
        #--------------------
        self.init_age()

    def init_age(self):
        self.data['age'] = self.s.return_age()

    def init_name(self):
        pass


    def init_ethnicity(self):
        pass

    def init_sexuality(self):
        pass

    def init_gender(self):
        pass

    def init_class(self):
        pass

    def get_age(self):
        return self.data['age']
