'''
Statistics are generated off of the following functional dependencies:

    {Population percentage} -> {Age}
    {Age} -> {Sex}
    {Age, Sex} -> {Hispanic}
    {Age, Sex, Hispanic} -> {Race}
    {LGBT} -> {GP_US_ADULT_LGBT}

'''
import os
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
        self.CSV_RACE_KEY = ['White', 'Black', 'Native American/Alaskan', 'Asian', 'Native Hawaiian/Other Pacific Islander', 'Two Or More Races']

        #US Census
        #Population by age and ethnicity
        #December 1st 2018
        #https://www.census.gov/data/datasets/2017/demo/popest/nation-detail.html#par_textimage_57373479
        #Proportions of ages
        with open(os.path.join('CSV', 'US_CENSUS_AGE_STATISTICS.csv'), mode='r') as infile:
            reader = csv.reader(infile)
            self.POP_BY_AGE = {int(rows[0]): float(rows[1]) for rows in reader}

        #Proportions of sex by age
        with open(os.path.join('CSV', 'US_CENSUS_SEX_BY_AGE.csv'), mode='r') as infile:
            reader = csv.reader(infile)
            self.SEX_BY_AGE = {int(rows[0]): float(rows[1]) for rows in reader}

        #Proportions of female hispanic persons by age
        with open(os.path.join('CSV', 'US_CENSUS_HISPANIC_BY_AGE.csv'), mode='r') as infile:
            reader = csv.reader(infile)
            self.HISPANIC_BY_AGE = {int(rows[0]): {'F': float(rows[1]), 'M': float(rows[2])} for rows in reader}

        #Proportions of race by age for male hispanic persons
        with open(os.path.join('CSV', 'US_CENSUS_H&M_RACE_BY_AGE.csv'), mode='r') as infile:
            reader = csv.reader(infile)
            self.HM_RACE_BY_AGE = {int(rows[0]): {0: float(rows[1]), 1: float(rows[2]), 2: float(rows[3]), 3: float(rows[4]), 4: float(rows[5]), 5: float(rows[6])} for rows in reader}

        #Proportions of race by age for female hispanic persons
        with open(os.path.join('CSV', 'US_CENSUS_H&F_RACE_BY_AGE.csv'), mode='r') as infile:
            reader = csv.reader(infile)
            self.HF_RACE_BY_AGE = {int(rows[0]): {0: float(rows[1]), 1: float(rows[2]), 2: float(rows[3]), 3: float(rows[4]), 4: float(rows[5]), 5: float(rows[6])} for rows in reader}

        #Proportions of race by age for male non-hispanic persons
        with open(os.path.join('CSV', 'US_CENSUS_NH&M_RACE_BY_AGE.csv'), mode='r') as infile:
            reader = csv.reader(infile)
            self.NHM_RACE_BY_AGE = {int(rows[0]): {0: float(rows[1]), 1: float(rows[2]), 2: float(rows[3]), 3: float(rows[4]), 4: float(rows[5]), 5: float(rows[6])} for rows in reader}

        #Proportions of race by age for female non-hispanic persons
        with open(os.path.join('CSV', 'US_CENSUS_NH&F_RACE_BY_AGE.csv'), mode='r') as infile:
            reader = csv.reader(infile)
            self.NHF_RACE_BY_AGE = {int(rows[0]): {0: float(rows[1]), 1: float(rows[2]), 2: float(rows[3]), 3: float(rows[4]), 4: float(rows[5]), 5: float(rows[6])} for rows in reader}



    #Creates random float between 0 & 1 and returns
    #an age based on age proportions from 0 to 100
    def return_age(self):
        num = random.uniform(0,1)
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

    def return_race(self, age, sex, hispanic):
        num = random.uniform(0,1)
        dict = []
        prev_p = 0
        if hispanic:
            if sex is 'Male':
                dict = self.HM_RACE_BY_AGE
            elif sex is 'Female':
                dict = self.HF_RACE_BY_AGE
        elif not hispanic:
            if sex is 'Male':
                dict = self.NHM_RACE_BY_AGE
            elif sex is 'Female':
                dict = self.NHF_RACE_BY_AGE

        for race in dict[age].keys():
            if num <= (dict[age][race] + prev_p):
                return self.CSV_RACE_KEY[race]
            prev_p += dict[age][race]


    #returns hispanic boolean based on age & sex
    def return_hispanic(self, age, sex):
        num = random.uniform(0,1)
        if sex == 'Male':
            sx_k = 'M'
        else:
            sx_k = 'F'
        if num <= self.HISPANIC_BY_AGE[age][sx_k]:
            return True
        else:
            return False


    def return_LGBT(self):
        num = random.uniform(0,1)
        if num <= self.GP_US_ADULT_LGBT:
            return True
        else:
            return False
