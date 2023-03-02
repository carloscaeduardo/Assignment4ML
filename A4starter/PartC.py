import matplotlib.pyplot as plt
import TemperatureHelper

MONTH_NAMES = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
]

plt.rcParams["figure.figsize"] = [10, 6]  # bigger than default


def annualMeansPerCity(cities, years):
    '''find the mean for each city and each year'''
    '''save one chart per city'''
    pass


def annualMeansCombined(cities, years, patterns):
    '''find the means for the cities in the timespan, 
    and show each as a separate series'''
    pass


def singleDayPerCity(cities, years, month, day):
    '''create one chart per city'''
    pass


def singleDayCombined(cities, years, month, day, patterns):
    ''' create a single chart with each city as a series'''
    pass
