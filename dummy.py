import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "H4DAR2ad4eTvD4ZEpOfbxdM4uVbz-oIsUYFC-aLMSOVH"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields": ["dual_sim", "battery_power", "four_g", "n_cores", "touch_screen", "ram"], "values": [[1,2000,1,2,1,6]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/07f062cc-4693-4602-9857-aaff526f37b1/predictions?version=2023-02-11', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
prediction =response_scoring.json()
prediction = prediction['predictions'][0]['values'][0][0]
print(prediction)
