import csv
from urllib.parse import urljoin

import requests

from helpers import LOCAL_COUNCILS_CODES, BASE_URL, csv_council_results, council_results, election_results, \
    csv_election_results, csv_committee_result, committee_result

contender_results_list = []
election_results_list = []
committee_result_list=[]
for code in LOCAL_COUNCILS_CODES:
    url = urljoin(BASE_URL, str(code))
    print(url)

    res = requests.get(url)
    res = res.json()
    council_name = res['DataCollection']["Name"]
    councils_head_results = res['DataCollection']['CandidateReports']
    settlements = res['DataCollection']['Settlements']
    for head in councils_head_results:
        name = head["Name"]
        percentage = head['VotersPercentage']
        contender_results_list.append(dict(
            council_name=council_name,
            name=name,
            percentage=percentage
        ))
    for settlement in settlements:
        settlement_name = settlement["Name"]
        factions_results = settlement['FactionResults']
        committee_results =settlement['CommitteeResults']
        for factions_result in factions_results:
            letter = factions_result["Letter"]
            name = factions_result["Name"]
            votes_percentage = factions_result["VotesPercentage"]

            election_results_list.append(dict(
                council_name=council_name,
                settlement_name=settlement_name,
                letter=letter,
                name=name,
                votes_percentage=votes_percentage
            ))
        for _committee_result in committee_results:
            letter = _committee_result["Letter"]
            name = _committee_result["Name"]
            votes_percentage = _committee_result["VotesPercentage"]
            committee_result_list.append(dict(
                council_name=council_name,
                settlement_name=settlement_name,
                letter=letter,
                name=name,
                votes_percentage=votes_percentage

            ))

    y = 1
with open(csv_council_results, 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=council_results)
    csv_writer.writeheader()
    csv_writer.writerows(contender_results_list)

with open(csv_election_results, 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=election_results)
    csv_writer.writeheader()
    csv_writer.writerows(election_results_list)

with open(csv_committee_result, 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=committee_result)
    csv_writer.writeheader()
    csv_writer.writerows(committee_result_list)

