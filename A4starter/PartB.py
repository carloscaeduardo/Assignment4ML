import PartA
import csv
import numpy as np


class TemperatureHelper:
    def __init__(self,  data_file):
        self.data = {}
        lists = []
        with open(data_file) as file:
            next(file)
            for line in file:
                line = line.strip("\n")
                # split the line
                lineSplit = line.split(",")
                # print(lineSplit[0])
                # for the first line in the file
                city, date, temperature = lineSplit
                # print(city, temperature)
                if date == "DATE":
                    continue
                # print(date)
                year, month, day = date.split('-')
                # create dictionaries for each step if they don't exist
                if city not in self.data:
                    self.data[city] = {}
                if year not in self.data[city]:
                    self.data[city][year] = {}
                if month not in self.data[city][year]:
                    self.data[city][year][month] = {}

                # add temperature data to the day of the month of the year in the city
                self.data[city][year][month][day] = temperature
            # print(self.data["Atlanta"]['2011']["01"])

    def getDailyTemperature(self, city, year, month, day):
        '''Returns the temperature for the specified city and date'''
        return self.data[city][year][month][day]

    def getYearlyTemperatures(self, city, year):
        '''Returns a numpy array containin the temperatures for the specified city
            for each day of the specified year
        '''
        result = np.array(self.data[city][year])


# data set goes from 1998 to 2018

# data = TemperatureHelper("test1.csv")
# temp1 = data.getDailyTemperature("Atlanta", '2000', '10', '01')
# print("getDailyTemperature test 1: " + temp1)

# temp2 = data.getDailyTemperature('Fargo', '1998', '05', '21')
# print("getDailyTemperature test 2: " + temp2)

# temp3 = data.getDailyTemperature('Jacksonville', '2017', '12', '29')
# print("getDailyTemperature test 3: " + temp3)
