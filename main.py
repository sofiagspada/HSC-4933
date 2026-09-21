import requests

# Ask the user for the state FIPS code(s)
state_fips = input("Enter the State FIPS code(s) that you would like data for: ")

# Ask the user for the variable names
variables = input("Enter the variable names that you would like data for: ")

# Build the Census API URL
url = f"https://api.census.gov/data/2023/acs/acs1?get=NAME,{variables}&for=state:{state_fips}"

# Request the data
response = requests.get(url)

# Convert the response to JSON
data = response.json()

# Print the number of rows
print(f"\nFound {len(data) - 1} Rows of Data.")

# Print each row of data
for row in data:
    print(row)