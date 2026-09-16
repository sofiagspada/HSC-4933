
import requests

# TA census API Url always has this shape:
# https://api.census.gov/data/{year}/{dataset}?get={variables}&for={geography}

YEAR = 2020
DATASET = "dec"
URL = f"https://api.census.gov/data/{YEAR}/{DATASET}"
API_KEY = "85fcc6b7c0ad4cf2938d868da6560a69eca034b0"

CENSUS_API_KEY = ""
params = {
    "get": "NAME,DP1_0001C",
    "for": "state:*",
    "key": API_KEY
}

response = requests.get(URL, params=params)

data = response.json()
# the API returns a list of lists. the first row is the column header
print(data)

