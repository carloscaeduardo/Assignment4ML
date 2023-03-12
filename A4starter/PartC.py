import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import TemperatureHelper
import statistics
import PartB as th
import LinearRegressionTools as tools

temp_helper = th.TemperatureHelper("output/partA.csv")
print(temp_helper.data["Atlanta"]["1998"])

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


def annual_means_per_city(cities, years):
    for city in cities:
        x_vals = []  # years
        y_vals = []  # temperatures
        # print(years)
        for year in years:
            appendInY = temp_helper.getYearlyTemperatures(
                city, year)
            appendInY = appendInY.astype(float)
            mean = np.mean(appendInY)
            y_vals.append(mean)
            x_vals.append(int(year))

        # create graph
        plt.plot(x_vals, y_vals, 'bo')
        plt.title(f"Annual Mean Temperatures for {city}")
        plt.xlabel("Year")
        plt.ylabel("Temperature (°C)")
        # Save the plot to a file
        plt.savefig(f'PartC/{city}.png')
        plt.show()


def annualMeansPerCityWithTrendline(cities, years):
    for city in cities:
        x_vals = []  # years
        y_vals = []  # temperatures
        intYears = []
        # print(years)
        for year in years:
            appendInY = temp_helper.getYearlyTemperatures(
                city, year)
            appendInY = appendInY.astype(float)
            mean = np.mean(appendInY)
            y_vals.append(mean)
            x_vals.append(int(year))
            intYears.append(int(year))

        # polyfit finds a polynomial that is the best fit for the data
        # model = plt.polyfit(xVals, yVals, 1)  # 1 is the polynomial degree
        model1 = np.polyfit(intYears, y_vals, 1)
        # polyval evaluates a polynomial at the specified x values and returns
        # the computed y values
        compYVals = np.polyval(model1, intYears)
        rsq = tools.r_squared(np.array(y_vals), np.array(compYVals))
        seSlope = tools.se_over_slope(np.array(intYears), np.array(
            y_vals), np.array(compYVals), np.array(model1))
        # create graph
        plt.plot(x_vals, y_vals, 'bo')
        plt.plot(x_vals, compYVals, 'r', label='Linear Fit')
        plt.title(f"Annual Mean Temperatures for {city} "+'\n R^2 = ' + str(
            rsq) + "\n" + "SE to Slope = " + str(seSlope))
        plt.xlabel("Year")
        plt.ylabel("Temperature (°C)")
        # Save the plot to a file
        plt.savefig(f'PartC/{city}.png')
        plt.show()


def annual_means_combined(cities, years, patterns):
    for city in cities:
        x_vals = []  # years
        y_vals = []  # temperatures
        for year in years:
            appendInY = temp_helper.getYearlyTemperatures(
                city, year)
            appendInY = appendInY.astype(float)
            mean = np.mean(appendInY)
            y_vals.append(mean)
            x_vals.append(int(year))

    # create graph
        plt.plot(x_vals, y_vals, patterns[cities.index(city)])

    plt.title(
        f"Annual Mean Temperatures for {cities}")
    plt.xlabel("Year")
    plt.ylabel("Temperature (°C)")
    plt.legend(cities)
    # Save the plot to a file
    plt.savefig('PartC/combined.png')
    plt.show()


def single_day_per_city(cities, years, month, day):
    '''Creates and save one graph per city, each showing the temperature on the
        specified day for each specified year'''
    for city in cities:
        daily_temps = []
        for year in years:
            # Calculate daily temp for each day of that year
            daily_temp = temp_helper.getDailyTemperature(
                city, year, month, day)
            # Plot the annual means for each city
            daily_temps.append(float(daily_temp))

        plt.plot(years, daily_temps)

        # Set graph title and axis labels
        plt.title(
            f'Temperature for The Date: {MONTH_NAMES[int(month) - 1]}, {day} over Years for {city}')
        plt.xlabel('Year')
        plt.ylabel('Daily Temperature (°C)')
        plt.savefig(
            f'partC-daily-temps/DailyTemp-{city}-{month}-{day}.png')
        plt.show()
        plt.close()


def singleDayPerCityWithTrendline(cities, years, month, day):
    '''Creates and save one graph per city, each showing the temperature on the
        specified day for each specified year with trendlines'''
    for city in cities:
        daily_temps = []
        intYears = []
        for year in years:
            # Calculate daily temp for each day of that year

            daily_temp = temp_helper.getDailyTemperature(
                city, year, month, day)
            # Plot the annual means for each city
            daily_temps.append(float(daily_temp))
            year = int(year)
            intYears.append(year)

        # polyfit finds a polynomial that is the best fit for the data
        # model = plt.polyfit(xVals, yVals, 1)  # 1 is the polynomial degree
        model1 = np.polyfit(intYears, daily_temps, 1)
        # polyval evaluates a polynomial at the specified x values and returns
        # the computed y values
        compYVals = np.polyval(model1, intYears)
        rsq = tools.r_squared(np.array(daily_temps), np.array(compYVals))
        seSlope = tools.se_over_slope(np.array(intYears), np.array(
            daily_temps), np.array(compYVals), np.array(model1))
        plt.plot(years, daily_temps, 'bo', label='Data Points')
        plt.plot(years, compYVals, 'r', label='Linear Fit')
        # Set graph title and axis labels
        plt.title(
            f'Temperature for The Date: {MONTH_NAMES[int(month) - 1]}, {day} over Years for {city}'+'\n R^2 = ' + str(rsq) + "\n" + "SE to Slope = " + str(seSlope))

        plt.xlabel('Year')
        plt.ylabel('Daily Temperature (°C)')
        plt.savefig(
            f'partC-daily-temps/DailyTemp-{city}-{month}-{day}.png')
        plt.show()
        plt.close()


def single_day_combined(cities, years, month, day, patterns):
    for city in cities:
        x_vals = []  # years
        y_vals = []  # temperatures
        for year in years:
            assert city in temp_helper.data, "requested city is not available"
            assert year in temp_helper.data[city], "requested year is not available"
            y_vals.append(round(float(temp_helper.getDailyTemperature(
                city, year, month, day)), 2))
            x_vals.append(year)

        # create graph
        plt.plot(x_vals, y_vals, patterns[cities.index(city)])
        plt.title(
            f"Temperature on {MONTH_NAMES[int(month) - 1]} {day} for {','.join((cities))}")
        plt.xlabel("Year")
        plt.ylabel("Temperature (°C)")
    plt.legend(cities)
    # Save the plot to a file
    plt.savefig(f'PartC/single_day_combined_{month}_{day}.png')
    plt.show()
    plt.close()


# # cities
# atlanta = data.getYearlyTemperatures("Atlanta", "2000")
# print(test)
