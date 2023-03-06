import FileUtils
import datetime
import matplotlib
import pandas as pd
import itertools
import calendar

########################### PART A ###############################
#### RESULTS ARE PRESENTED AT Assignment.ipynb ########


def convertToCelsius(fahrenheit):
    '''Converts temperature from Fahrenheit to Celsius.'''
    celsius = (fahrenheit - 32.0) * (5/9)
    return celsius


def isLeap(year):
    '''Checks if an year is a leap year (divisible by 4 ) or (divisible by 400 if ends with 00)
        Returns true if is leap and false if not'''

    res = calendar.isleap(year)
    return res


def testDataSet(data, numOfCities, startDate, endDate):
    '''Tests if the number of lines is (C*YN*365) + (C*YL*366) + 1 Where 
        C is the number of Cities, YN is the number of regular years and YL is the number of leap years'''
    numOfLines = len(data)
    pattern = "%Y-%m-%d"
    startDate = datetime.datetime.strptime(startDate, pattern)
    startYear = startDate.year
    endDate = datetime.datetime.strptime(endDate, pattern)
    endYear = endDate.year
    numOfYears = endYear - startYear
    regularYears = 0
    leapYears = 0
    for i in range(startYear, endYear):

        if (isLeap(i)):
            leapYears += 1
        else:
            regularYears += 1
    # now calculate the number of lines
    checkLines = numOfCities*regularYears*365 + \
        numOfCities*leapYears*366 + 1 - numOfCities
    if (numOfLines == checkLines):
        testResult = True
    else:
        testResult = False
    return testResult


def consolidateData(cities, startDate, endDate, outputFileName):
    '''
    Creates a single file containing the average daily temperatures, in Celsius,
    for each city for each date in the date range. The output should be as shown below:
    City, Date, Temperature
    alphabetically, earliest, temperature
    '''
    # read the files using city_info as base.
    # First, read city_info.csv
    # fileList = FileUtils.readIntoList("city_info.csv")
    # print(fileList)
    lines = FileUtils.readIntoList("sourcedata/city_info.csv")

    cities = [name.lower() for name in cities]
    # print(cities)

    outputList = []
    listToSearch = []
    for i in range(len(lines)):
        lines[i] = lines[i].replace('"', "")
        rows = lines[i].strip().split(",")
        if (rows[1].lower() in cities):
            listToSearch.append(rows)

    fileDataResult = [["CITY", "DATE", "TEMPERATURE"]]
    for i in range(len(listToSearch)):
        city = listToSearch[i][1].strip()
        # print(city)
        file = FileUtils.readIntoList(
            "sourcedata/"+listToSearch[i][2].strip() + ".csv")

        for j in range(len(file)):
            file[j] = file[j].replace('"', "")
            fileRow = file[j].split(",")
            # format_data = "%y-%"
            date = fileRow[1]
            # check if row date is inside the range of dates
            if (date > startDate and date < endDate and date != "NA"):
                # get the temperature average for the row
                try:
                    avgTemp = (int(fileRow[2]) + int(fileRow[3]))/2
                    avgTemp = convertToCelsius(avgTemp)
                except:
                    print("temperature unavailable for city " +
                          city + " in date: " + date)
                    # temperature unavailable
                    return

                else:
                    fileDataResult.append([city, date, avgTemp])
    # sort list
    fileDataResult = sorted(fileDataResult, key=lambda x: (x[0], x[1]))
    fileDataResult = list(fileDataResult for fileDataResult,
                          _ in itertools.groupby(fileDataResult))
    # send to outputFile
    # first make each list into a string
    sendToOutput = ["CITY,DATE,TEMPERATURE"]
    for i in range(len(fileDataResult)):
        sendToOutput.append(','.join(map(str, fileDataResult[i])))

    FileUtils.writeListToFile(sendToOutput, outputFileName)
    # print(listToSearch)
    return fileDataResult

###################################################################

# cities = ["Atlanta", "Eugene", "Fargo", "Jacksonville"]
# startDate = "1998-01-01"
# endDate = "2018-01-01"
# outputFileName = "test1.csv"
# result = consolidateData(cities, startDate, endDate, outputFileName)
# # print(result)

# testResult = testDataSet(result, len(cities), startDate, endDate)
# print(testResult)


########################### PART B ##############################
