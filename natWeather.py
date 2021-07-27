import requests

response = requests.get("https://api.weather.gov/gridpoints/PQR/107,97/forecast/hourly")
data = response.json()
outF = open("output.json", "w")
outF.write(response.text)

flag = 0
mFlag = 0 #this does not need to be reset ever because we only get 1 weeks worth of data
currDate = 0
for i in data['properties']['periods']: #parse the JSON
    strDate = i['startTime'][8] + i['startTime'][9] 
    intDate = int(strDate)
    strHr = i['startTime'][11:13]
    intHr = int(strHr)
    if(intDate == 1 and mFlag == 0):
        currDate = 0
        mFlag = 1

    if(intDate > currDate):
        currDate = intDate
        flag = 0

    if(i['temperature'] >= 80 and flag == 0):
        print("On:", i['startTime'][0:10], "Stop process at:", i['startTime'][11:16])
        flag = 1

    if(intHr == 23 and flag != 1):
        print("On:", i['startTime'][0:10], "temperature will not reach 80 degrees F")
    

input("Press Enter to exit...")