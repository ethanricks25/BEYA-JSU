import pandas as pd 
import requests
import json

def loadFIPSData():
    data = pd.read_csv("FipsCountyCodes.csv")
    data.set_index("FIPS", inplace = True)
    return data

countyFIPS = loadFIPSData()

def get_CountyfromFIPS(FIPS):
    return countyFIPS.iloc[[FIPS]]["Name"]
  

def hospitalsInCounty(countyName):
    institutions_found= []
    query = "hospitals in {} County".format(countyName)
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key=AIzaSyDIgisINp8Q0Llkw1QVs7guBCgHLDDjg1s".format(query)
    params = {}
    response = requests.get(url, params=params)
    results = json.loads(response.content)
    institutions_found.extend(results['results'])

    col_names = ['name','lat','lng' ]
    hospitalDf = pd.DataFrame(columns=col_names)

    for index, res in enumerate(institutions_found):
        row = []

        for tag in col_names:
            if tag == 'lat' or tag == 'lng':
                row.append(res['geometry']['location'][tag])
            else:
                row.append(res[tag])

        hospitalDf.loc[-1] = row
        hospitalDf.index += 1
        hospitalDf.sort_index()
    return hospitalDf.head(20).copy()

def get_poor_Counties(state):
    stateFIPS = {
        "AL" : "01",
        "AK" : "02",
        "AZ" : "04",
        "AR" : "05",
        "CA" : "06",
        "CO" : "08",
        "CT" : "09",
        "DE" : "10",
        "DC" : "11",
        "FL" : "12",
        "GA" : "13",
        "HI" : "15",
        "ID" : "16",
        "IL" : "17",
        "IN" : "18",
        "IA" : "19",
        "KS" : "20",
        "KY" : "21",
        "LA" : "22",
        "ME" : "23",
        "MD" : "24",
        "MA" : "25",
        "MI" : "26",
        "MN" : "27",
        "MS" : "28",
        "MO" : "29",
        "MT" : "30",
        "NE" : "31",
        "NV" : "32",
        "NH" : "33",
        "NJ" : "34",
        "NM" : "35",
        "NY" : "36",
        "NC" : "37",
        "ND" : "38",
        "OH" : "39",
        "OK" : "40",
        "OR" : "41",
        "PA" : "42",
        "RI" : "44",
        "SC" : "45",
        "SD" : "46",
        "TN" : "47",
        "TX" : "48",
        "UT" : "49",
        "VT" : "50",
        "VA" : "51",
        "WA" : "53",
        "WV" : "54",
        "WI" : "55",
        "WY" : "56",
        "AS" : "60",
        "GU" : "66",
        "MP" : "69",
        "PR" : "72",
        "VI" : "78"
        }
    APIkey = "061e3db32c4cdf59d3e4689ee4daa61166485af9"

    state = stateFIPS[state]
    povertyURL = "https://api.census.gov/data/timeseries/poverty/saipe?get=SAEPOVALL_PT&for=county:*&in=state:{}&time=2018&key={}".format(state, APIkey)
    request = requests.get(povertyURL, {})
    request = request.json()

    poorCounties = pd.DataFrame(request[1:], columns=request[0])
    poorCounties = poorCounties.sort_values(by='SAEPOVALL_PT', ascending=False)
    poorCounties = poorCounties.head(10).copy()
    poorCounties = list(poorCounties['county'])
    for index, county in enumerate(poorCounties):
        poorCounties[index] = str(state)+str(county)
    return poorCounties

def get_all_hospitals(state_abbrev):
    all_hospitals = pd.DataFrame(columns=['name', 'lat', 'lng'])
    top_10_poor_counties = get_poor_Counties(state_abbrev)
    for county in top_10_poor_counties:
        countyName = get_CountyfromFIPS(county)
        data = hospitalsInCounty(countyName)
        if not data.empty:
            all_hospitals= pd.concat([all_hospitals, data], ignore_index=True)
    return all_hospitals

print(get_all_hospitals("AL"))