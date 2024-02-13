import pandas as pd 
import requests
import json

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
demographic_to_code = {
    "white" : "DP1_0086P",
    "black" : "DP1_0087P",
    "native" : "DP1_0088P",
    "asian" : "DP1_0089P",
    "pacific_islander" : "DP1_0090P"
    }

class finding_hospitals:
    def __init__(self, race, state) -> None:
        self.countyFIPS = self.loadFIPSData()
        self.hospitals = self.get_all_hospitals(race, state)

    def loadFIPSData(self):
        data = pd.read_csv("FipsCountyCodes.csv")
        data.set_index("FIPS", inplace = True)
        return data

    

    def get_CountyfromFIPS(self, FIPS):
        return self.countyFIPS.loc[[FIPS]]["Name"]
    

    def hospitalsInCounty(self, countyName):
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

    def get_county(self, demographic_code, state):

        APIkey = "31e3fca039ce2563eac1600da2f1e7a7d813902b"

        state = stateFIPS[state]

        demographicsURL = "https://api.census.gov/data/2020/dec/dp?get={}&for=county:*&in=state:{}&key={}".format(demographic_code, state, APIkey)
        request = requests.get(demographicsURL, {})
        request = request.json()

        print(request)
        print(state)
        print("This is the counties URL" + demographicsURL)

        counties = { record[2] : float(record[0]) for record in list(request)[1:]}
        print(counties)
        

        return max(counties, key=lambda k: counties[k])

    def get_all_hospitals(self, race, state_abbrev):
        all_hospitals = pd.DataFrame(columns=['name', 'lat', 'lng'])
        county = self.get_county(demographic_to_code[race],state_abbrev)
        print(county)
        countyName = self.get_CountyfromFIPS(int(stateFIPS[state_abbrev] + county))
        print(countyName)
        data = self.hospitalsInCounty(countyName)
        if not data.empty:
            all_hospitals= pd.concat([all_hospitals, data])
        return all_hospitals
    
    def get_hospitals(self):
        return self.hospitals
    # print(get_county( demographic_to_code["black"], "MS"))
    # print(get_CountyfromFIPS(int(stateFIPS['MS'] + "003")))
    #print(get_all_hospitals("black", "MS"))