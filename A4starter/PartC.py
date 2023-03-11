import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import TemperatureHelper
import statistics
import PartB as th

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


def annual_means_combined(cities, years, patterns):
    citiesvalues = []
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

    for city in cities:
        daily_temps = []
        for year in years:
            # Calculate daily temp for each day of that year
            daily_temp = temp_helper.getDailyTemperature(
                city, year, month, day)
            # Plot the annual means for each city
            daily_temps.append(daily_temp)

        plt.plot(years, daily_temps)

        # Set graph title and axis labels
        plt.title(
            f'Temperature for The Date: {MONTH_NAMES[month - 1]}, {day} over Years for {city}')
        plt.xlabel('Year')
        plt.ylabel('Daily Temperature (°C)')
        plt.savefig(
            f'output/partC-daily-temps/DailyTemp-{city}-{month}-{day}.png')
        plt.close()


def single_day_combined(cities, years, month, day, patterns):
    for city in cities:
        x_vals = []  # years
        y_vals = []  # temperatures
        for year in years:
            assert city in temp_helper.data, "requested city is not available"
            assert year in temp_helper.data[city], "requested year is not available"
            y_vals.append(temp_helper.getDailyTemperature(
                city, int(year), month, day))
            x_vals.append(int(year))

        # create graph
        plt.plot(x_vals, y_vals, patterns[cities.index(city)])
        plt.title(
            f"Temperature on {MONTH_NAMES[month - 1]} {day} for {list_to_string(cities, 'and')}")
        plt.xlabel("Year")
        plt.ylabel("Temperature (°C)")
    plt.legend(cities)
    # Save the plot to a file
    plt.savefig(f'output/PartC/single_day_combined_{month}_{day}.png')
    plt.close()


# # cities
# atlanta = data.getYearlyTemperatures("Atlanta", "2000")
# print(test)
