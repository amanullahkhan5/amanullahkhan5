import json
import pandas as pd
import requests

# Load API collection JSON
with open("api_collection.json", "r") as file:
    api_data = json.load(file)

# Load expected output from Excel
df = pd.read_excel("expected_output.xlsx")

# Dictionary to store API verification results
results = []

# Iterate over each API in the JSON collection
for api in api_data["apis"]:
    api_name = api["name"]
    url = api["url"]
    expected_output = api["expected_output"]

    try:
        # Simulating an API request (Uncomment in real scenario)
        # response = requests.get(url)
        # actual_output = response.json()

        # Mock actual response for testing
        actual_output = expected_output  # Replace this with `response.json()` in real use

        # Compare each expected field with actual response
        #amanullah khan
        for _, row in df[df["API Name"] == api_name].iterrows():
            field = row["Field"]
            expected_value = row["Expected Value"]
            actual_value = actual_output.get(field, None)

            result = {
                "API Name": api_name,
                "Field": field,
                "Expected Value": expected_value,
                "Actual Value": actual_value,
                "Match": expected_value == actual_value
            }
            results.append(result)

    except Exception as e:
        print(f"Error verifying {api_name}: {e}")

# Convert results to DataFrame and save as a report
result_df = pd.DataFrame(results)
result_df.to_csv("api_verification_report.csv", index=False)

print("Verification complete! Check 'api_verification_report.csv' for details.")
