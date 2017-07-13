import json
import os
import sys

import requests


BASE = "https://www.googleapis.com/civicinfo/v2/"

REPRESENTATIVES = BASE + "representatives"


if __name__ == '__main__':
    query_args = {
            "key": os.environ.get("API_KEY"),
            "address": sys.argv[1],
            "includeOffices": "true",
    }

    r = requests.get(REPRESENTATIVES, params=query_args)
    if r.ok:
        # print json.dumps(r.json(), indent=2)
        officials = r.json()["officials"]
        offices = r.json()["offices"]

        for office in offices:
            print "%s:" % office["name"]
            for index in office["officialIndices"]:
                print "%s (%s) [%s]" % (officials[index]["name"], officials[index].get('phones', ['missing'])[0], officials[index].get("party", "Unknown"))
            print "=-" * 40

    else:
        print "error: %s" % r
