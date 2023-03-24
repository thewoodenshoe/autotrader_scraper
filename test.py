from urllib.request import urlopen
import json

url = "https://www.autotrader.com/rest/searchresults/base?startYear=2023&zip=29492&makeCode1=BMW&modelCode1=BMWX7&searchRadius=0&minPrice=80000&maxPrice=95000&sortBy=datelistedDESC"
response = urlopen(url)
data = json.loads(response.read())

if (data['totalResultCount'] > 0):
    # for i in data:
    #    print(json.dumps(i, indent=1))
    # print( data['totalResultCount'])
    x = 0
    for i in data['listings']:
        x += 1
        #   debug
        # print(i['vin'])

        myTuple = i["title"], "Interior color:", i["specifications"]["interiorColor"]["value"], i["vin"]
        text2print = str(myTuple[0])
    text2print = text2print + "hello"
print(text2print)
# print(json.dumps(text2print, indent=1))
