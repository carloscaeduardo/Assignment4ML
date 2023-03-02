import FileUtils
import datetime
import matplotlib


def convertToCelsius(fahrenheit):
    '''Converts temperature from Fahrenheit to Celsius.'''
    celsius = (fahrenheit - 32.0) * (5/9)
    return celsius


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

xvals = []
yvas = []
dataList = []
for i in range(len(lines)):
    dataList.append(lines[i].split(","))
# having the list of Countries with the respective file name, we will use it to make an
# list to store the city name, Date and temperature.
completeList = []
for i in range(1, 3):  # len(dataList)):
    # read the file for the city
    filename = dataList[i][2][1:-1]
    cityFile = FileUtils.readIntoList("sourcedata/"+filename + ".csv")
    cityName = dataList[i][1][1:-1]

    # get the Date and Average Temperature for each date
    for j in range(1, 10):  # len(cityFile)):
        cityFileLine = cityFile[j].split(",")
        # try to calculate the avgTemp
        try:

            avgTemp = convertToCelsius(
                (int(cityFileLine[2]) + int(cityFileLine[3]))/2)

        except:
            # this date has no temperature information
            avgTemp = None

        finally:
            date = cityFileLine[1]
            avgTempFormat = "{avgTemp:.2f}"
            outPutLine = cityName+"," + date + \
                "," + avgTempFormat.format(avgTemp=avgTemp)
            completeList.append(outPutLine)
print(completeList[0][1])
FileUtils.writeListToFile(completeList, "testOutput.csv")
