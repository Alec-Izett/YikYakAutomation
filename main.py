# YikYak message Automation
# Alec Izett 2023

from bs4 import BeautifulSoup
import requests

def getWeather(city):
    city = city.replace(" ", "+")
    page = requests.get(f'https://forecast.weather.gov/MapClick.php?CityName={city}')
    soup = BeautifulSoup(page.content, 'html.parser')
    seven_day = soup.find(id="seven-day-forecast")
    forecast_items = seven_day.find_all(class_="tombstone-container")
    tonight = forecast_items[0]
    short_desc = tonight.find(class_="short-desc").get_text()
    tempLow = tonight.find(class_="temp").get_text()

    tonight = forecast_items[1]
    tempHigh = tonight.find(class_="temp").get_text()

    intTemp = ""
    for c in tempHigh:
        if c.isdigit():
            intTemp = intTemp + c

    page = requests.get(f'https://forecast.weather.gov/MapClick.php?CityName={city}')
    soup = BeautifulSoup(page.content, 'html.parser')
    current_cond = soup.find(id="current_conditions_detail")
    cond_tr = current_cond.find_all('td')

    intHumidity = ""
    for c in str(cond_tr[1]):               # Remove unnecessary text from humidity data
        if c.isdigit():
            intHumidity = intHumidity + c


    print("Weather in "+city+"!")
    print("Today: "+short_desc)
    print(tempHigh)
    print(tempLow)
    print("Humidity: "+intHumidity+"%")
    intTemp = int(intTemp)
    if intTemp <= 32:
        print("Stay warm!!")
    if intTemp >= 72 and intTemp <= 84:
        print("Enjoy the nice temps!!")
    if intTemp > 90:
        print("Stay cool!!")


def isTodayFriday13th():
    page = requests.get("https://istodayfridaythe13th.com/")
    soup = BeautifulSoup(page.content, 'html.parser')
    isFriday = soup.find(id="answer").get_text()
    if isFriday == "NO":
        print("Today is not Friday the 13th")
    else:
        print("Today IS Friday te 13th")


def quoteOfTheDay():
    file2 = open("place.txt", "r+")             # zero indexed (line # storage file)
    quoteLineNumber = (file2.read())
    file1 = open("quotes.txt", "r")             # file with quotes
    quoteList = (file1.readlines())
    if int(quoteLineNumber) >= ((len(quoteList))-1):        # Prevent overflow
        quoteLineNumber = "0"
    else:
        quoteLineNumber = str(int(quoteLineNumber) + 1)
    file2.seek(0)
    file2.write(str(quoteLineNumber))

    file1.close()
    file2.close()

    print("Quote of the Day:")
    print(quoteList[int(quoteLineNumber)])


cityName = "Tulsa"      # this does not work perfectly, only for some cities
getWeather(cityName)
print("")
isTodayFriday13th()
print("")
quoteOfTheDay()
