import numpy as np


class TemperatureHelper(object):
    # Initialize with data from a consolidated dataset file created in PartA.
    def __init__(self, filename):
        self.rawdata = {}
        # finish building the rawdata in dictionary format

    # Get the daily temperatures for the given year and city.
    def getYearlyTemperatures(self, city, year):
        temperatures = []

        # your code here

        return np.array(temperatures)

    # Get the daily temperature for the given city and date (day, month, year).
    def getDailyTemperature(self, city, day, month, year):
        assert city in self.rawdata, "requested city is not available"
        assert year in self.rawdata[city], "requested year is not available"
        assert month in self.rawdata[city][year], "requested month is not available"
        assert day in self.rawdata[city][year][month], "requested day is not available"
        return self.rawdata[city][year][month][day]
