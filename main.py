from urllib.request import urlopen
import json

minPrice=60000
maxPrice=80000
url = f"https://www.autotrader.com/rest/searchresults/base?startYear=2023&zip=29492&makeCode1=BMW&modelCode1=BMWX7&searchRadius=0&minPrice={minPrice}&maxPrice={maxPrice}&numRecords=100&sortBy=datelistedDESC"
response = urlopen(url)
data = json.loads(response.read())

def addTag(i, tagName, overwriteLabel):
    if overwriteLabel != 0:
        label = overwriteLabel
    else:
        label = tagName
    if tagName in i:
        if i[tagName]:
            myValue = f"{label} : {i[tagName]} \n"
        else:
            myValue = f"{label} : no information found \n"
    else:
        myValue = f"{label} : no information found \n"
    return myValue


if (data['totalResultCount'] > 0):
    counter = 0
    for i in data['listings']:
        ProceedWithThisCar = True

        result = addTag(i, "title", 0)
        result = result + addTag(i,"vin", 0)
        result = result + addTag(i['pricingDetail'], "salePrice", 0)
        result = result + addTag(i['pricingDetail'], "msrp", 0)


        # interior color
        if "interiorColor" in i["specifications"]:
            myList = ['silver', 'ivory']
            ProceedWithThisCar = False
            for item in myList:
                if ((i["specifications"]["interiorColor"]["value"].lower().find(item) != -1)):
                    result = result + addTag(i["specifications"]["interiorColor"], "value", "interior color")
                    ProceedWithThisCar = True
        else:
            result = result + "interior color: no information found \n"


        # exterior color
        if "color" in i["specifications"]:
            result = result + addTag(i["specifications"]["color"], "value", "exterior color")
        else:
            result = result + "exterior color: no information found \n"

        # packages
        if "packages" in i:
            if 'Executive Package' in i['packages']:
                result = result + addTag(i, 'packages', 0)
            else:
                ProceedWithThisCar = False
        else:
            result = result + "Packages: no information found \n"

        result = result + "http://www.autotrader.com" + i['website']['href'] + "\n"

        # if we want to continue
        if ProceedWithThisCar:
            counter += 1
            print(result)
    print('Cars found: ', counter)

