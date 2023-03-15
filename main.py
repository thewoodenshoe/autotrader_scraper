from urllib.request import urlopen
import json

url = "https://www.autotrader.com/rest/searchresults/base?startYear=2023&zip=29492&makeCode1=BMW&modelCode1=BMWX7&searchRadius=0&minPrice=80000&maxPrice=89000&sortBy=datelistedDESC"
response = urlopen(url)
data = json.loads(response.read())

if (data['totalResultCount'] > 0):
    # for i in data:
    #    print(json.dumps(i, indent=1))
    print( data['totalResultCount'])
    x = 0
    for i in data['listings']:
        x += 1
        #   debug
        # print(i['vin'])
        if i['vin'] == '5UX23EM04P9N98461':
            print(json.dumps(i, indent=1))

        myprintln = i["title"], "Interior color:", i["specifications"]["interiorColor"]["value"], i["vin"]
        if "packages" in i:
            myprintln = myprintln, i['packages']
        if i['pricingDetail']['salePrice'] == 0:
            if "msrp" in i['pricingDetail']:
                currency_string = "${:,.2f}".format(i['pricingDetail']['msrp'])
                myprintln = myprintln, currency_string
        else:
            currency_string = "${:,.2f}".format(i['pricingDetail']['salePrice'])
            myprintln = myprintln, currency_string
        if "color" in i["specifications"]:
            myprintln = myprintln, "exterior color: ", i["specifications"]["color"]["value"]

        myprintln = myprintln, i['website']['href']

        # Now we're gonna filter
        if (i["specifications"]["interiorColor"]["value"] not in ('Coffee','Cognac','Black','Coffee Sensafin','Coffee W/Sensafin Upholstery','Cognac Sensafin')):
            if "packages" in i and 'Executive Package' in i['packages']:
                # sold
                if i["vin"] not  in ('5UX23EM06P9R78708'):
                   print(json.dumps(myprintln, indent=1))
                   #print(i["vin"])
                   #print(json.dumps(i, indent=1))
    # print('amount fetched', x)
