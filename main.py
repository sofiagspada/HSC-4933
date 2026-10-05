import pandas as pd

# Read dataset to inspect columns and structure
df = pd.read_csv("Maternal Health Risk Data Set (2).csv")
print("Columns:", df.columns.tolist())
print("\nShape:", df.shape)
print("\nHead:\n", df.head())

Code output
Columns: ['Age', 'SystolicBP', 'DiastolicBP', 'BS', 'BodyTemp', 'HeartRate', 'RiskLevel']

Shape: (1014, 7)

Head:
    Age  SystolicBP  DiastolicBP    BS  BodyTemp  HeartRate  RiskLevel
0   25         130           80  15.0      98.0         86  high risk
1   35         140           90  13.0      98.0         70  high risk
2   29          90           70   8.0     100.0         80  high risk
3   30         140           85   7.0      98.0         70  high risk
4   35         120           60   6.1      98.0         76   low risk

Python
# Script to convert CSV to Parquet
parquet_script = """import pandas as pd

# Load dataset
df = pd.read_csv('Maternal Health Risk Data Set (2).csv')

# Ensure duplicate columns are removed (keeps the first occurrence)
df = df.loc[:, ~df.columns.duplicated()]

# Save to Parquet format
df.to_parquet('maternal_health_risk.parquet', index=False)
print("Successfully converted dataset to maternal_health_risk.parquet")
"""

# Script to convert CSV to JSON
json_script = """import pandas as pd

# Load dataset
df = pd.read_csv('Maternal Health Risk Data Set (2).csv')

# Ensure duplicate columns are removed
df = df.loc[:, ~df.columns.duplicated()]

# Save to JSON format
df.to_json('maternal_health_risk.json', orient='records', indent=4)
print("Successfully converted dataset to maternal_health_risk.json")
"""

# Script to convert CSV to XLSX
excel_script = """import pandas as pd

# Load dataset
df = pd.read_csv('Maternal Health Risk Data Set (2).csv')

# Ensure duplicate columns are removed
df = df.loc[:, ~df.columns.duplicated()]

# Save to Excel format
df.to_excel('maternal_health_risk.xlsx', index=False)
print("Successfully converted dataset to maternal_health_risk.xlsx")
"""

with open('convert_to_parquet.py', 'w') as f:
    f.write(parquet_script)

with open('convert_to_json.py', 'w') as f:
    f.write(json_script)

with open('convert_to_excel.py', 'w') as f:
    f.write(excel_script)

# Execute conversion scripts
import subprocess
subprocess.run(['python', 'convert_to_parquet.py'])
subprocess.run(['python', 'convert_to_json.py'])
subprocess.run(['python', 'convert_to_excel.py'])
