"""
Assignment name: CSV Import To Class Object
Program: CountyDemos.py
Author: Colby Boell
Last date modified: 04/11/2022

The purpose of this program is to use code to read a csv file so we can gather and print out information
from it by reading the file. By using  a class and code to get info from the csv file.
"""


# class
class CountyDemos:
    def __init__(self, rank, county, per_capita_income,median_household_income, median_family_income,population, number_of_households):
        self.rank = rank
        self.county = county
        self.per_capita_income = per_capita_income
        self.median_household_income = median_household_income
        self.median_family_income = median_family_income
        self.population = population
        self.number_of_households = number_of_households
