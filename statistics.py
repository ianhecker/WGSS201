'''
Statistics are generated off of the following functional dependencies:

    {Population percentage} -> {Age}
    {Age} -> {Sex}
    #Notice that there are increasing proportions of females as age increases
    #As much as 0.77 of people the age of 100 years or more are female
    #

'''

import csv
import random

class Statistics:


    def __init__(self):
        #Gallup Poll 2017 LGBT Adult Population Estimate for U.S.
        #US Adults who identify as LGBT
        #https://news.gallup.com/poll/234863/estimate-lgbt-population-rises.aspx
        self.GP_US_ADULT_LGBT = 0.045
        self.GP_US_ADULT_MALE_LGBT = 0.039
        self.GP_US_ADULT_FEMALE_LGBT = 0.051
        self.GP_US_ADULT_TRANSGENDER = 0.006

        #US Census
        #Population by age and ethnicity
        #December 1st 2018
        #https://www.census.gov/data/datasets/2017/demo/popest/nation-detail.html#par_textimage_57373479
        with open('US_CENSUS_AGE_STATISTICS.csv', mode='r') as infile:
            reader = csv.reader(infile)
            self.POP_BY_AGE = {int(rows[0]): float(rows[1]) for rows in reader}

        with open('US_CENSUS_SEX_BY_AGE.csv', mode='r') as infile:
            reader = csv.reader(infile)
            self.SEX_BY_AGE = {int(rows[0]): float(rows[1]) for rows in reader}

    #Creates random float and returns an age
    def return_age(self):
        num = random.uniform(0,1)
        #print('-----------' + str(num))
        counter = 0
        previous = 0
        for age in self.POP_BY_AGE.keys():
            if num <= self.POP_BY_AGE[counter] and num > previous:
                return counter
            previous = self.POP_BY_AGE[counter]
            counter += 1

    def return_sex(self, age):
        num = random.uniform(0,1)
        if num <= self.SEX_BY_AGE[age]:
            return 'Male'
        else:
            return 'Female'

    def return_race(self):
        num = random.uniform(0,1)
        counter = 0
        previous = 0
        for age in self.POP_BY_RACE.keys():
            if num <= self.POP_BY_RACE[counter] and num > previous:
                return counter
            previous = self.POP_BY_RACE[counter]
            counter += 1

    def return_sexuality(self):
        num = random.uniform(0,1)
        if num <= self.GP_US_ADULT_LGBT:
            return True
        else:
            return False
