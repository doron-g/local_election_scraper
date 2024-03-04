import sys

import requests

url = "https://serviceselectionresultsapi.moin.gov.il/api/elections"

res = requests.get(url=url)
res = res.json()
settlements_list = res['DataCollection'][1]['ParticipantMunicipalCouncils']


def get_code_by_name(name_to_find, data_list):
    for item in data_list:
        if item['Name'] == name_to_find:
            print(item['Code'])
            return item['Code']
    print("not found")
    return None


if __name__ == "__main__":
    city_name = sys.argv[1]
    get_code_by_name(city_name, settlements_list)
