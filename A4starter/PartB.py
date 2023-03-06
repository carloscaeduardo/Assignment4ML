import PartA
import csv
import numpy as np


class TemperatureHelper:
    def __init__(self,  data_file):
        self.data = {}
        with open(data_file, 'r') as file:
            for line in file:
                # for the first line in the file
                if (line.split()[1] == "CITY"):
                    pass
                else:
                    city, date, temperature = line.strip().split(",")
                    year, month, day = map(float, date.split('-'))
                    self.data[city][year][month][day] = float(temperature)

    def getDailyTemperature(self, city, year, month, day):
        '''Returns the temperature for the specified city and date'''
        return self.data[city][year][month][day]

    def getYearlyTemperatures(self, city, year):
        '''Returns a numpy array containin the temperatures for the specified city
            for each day of the specified year
        '''
        result = np.array(self.data[city][year])
