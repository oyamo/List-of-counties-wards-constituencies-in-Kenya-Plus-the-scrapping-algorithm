import re
import json as json
import requests

string = open("counties.txt").read().strip()
const_list = list(eval(string.replace("\n","")))

endpoint = "https://frozen-basin-45055.herokuapp.com/api/wards?"

final_list = {}

for county in const_list:
    url = endpoint + "county="+county.strip().replace(" ","+")
    r = requests.get(url)

    if r.text == "[]":
        print(county,"failed to fetch")
    else:
        print("Sucess",county)
        dictreturned = json.loads(r.text)
        wards = list(dictreturned)
        final_list[county] = {}
        constituencies = list(set([x["constituency"] for x in wards]))
        for i in constituencies:
            final_list[county][i] = []
        for ward in wards:
            final_list[county][ward["constituency"]].append(ward["name"])

json.dump(final_list,open("all-counties-constituencies-ward.json","w"))