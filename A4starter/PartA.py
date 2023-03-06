import FileUtils
import datetime
import matplotlib
import pandas as pd


def convertToCelsius(fahrenheit):
    '''Converts temperature from Fahrenheit to Celsius.'''
    celsius = (fahrenheit - 32.0) * (5/9)
    return celsius


def testDataSet(data):
    '''Tests if the number of lines is (C*YN*365) + (C*YL*366) + 1 Where 
        C is the number of Cities, YN is the number of regular years and YL is the number of leap years'''
    pass


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
    # send to outputFile
    # first make each list into a string
    sendToOutput = []
    for i in range(len(fileDataResult)):
        sendToOutput.append(','.join(map(str, fileDataResult[i])))

    FileUtils.writeListToFile(sendToOutput, outputFileName)
    # print(listToSearch)
    return fileDataResult


cities = ["Atlanta", "Eugene", "Fargo", "Jacksonville"]
startDate = "1997-01-01"
endDate = "2017-01-01"
outputFileName = "test1.csv"
result = consolidateData(cities, startDate, endDate, outputFileName)
# print(result)
