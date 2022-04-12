"""
Assignment name: CSV Import To Class Object
Program: main.py
Author: Colby Boell
Last date modified: 04/11/2022

The purpose of this program is to use code to read a csv file so we can gather and print out information
from it by reading the file. By using  a class and code to get info from the csv file.
"""
# imports
import csv
from class_defintions.CountyDemos import CountyDemos

with open('Iowa 2010 Census Data Population Income.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # initialize dictionary
    county = {}
    for row in csv_reader:
        # skip first row (data headers)
        if line_count == 0:
            line_count += 1
            continue
        county[str(row[1])] = CountyDemos(rank=row[0], county=row[1], per_capita_income=row[2], median_household_income=row[3], median_family_income=row[4], population=row[5], number_of_households=row[6])

    print("Dallas has a population of: " + str(county['Dallas'].population))
    print("# of households in Dallas is: " + str(county['Dallas'].number_of_households))

    pop_sum = 0
for key in county:
    pop_sum += int(county[key].population.replace(',',''))
print(f'Total population for Iowa: {pop_sum}')
