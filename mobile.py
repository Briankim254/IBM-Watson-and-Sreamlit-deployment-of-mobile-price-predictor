import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import requests


@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(dualsim, batterypower, fourg, cores, touchscreen,ram):   
 
    # Pre-processing user input    
    if dualsim == "true":
        dual_sim = 1
    else:
        dual_sim = 0
 
    if fourg == "true":
        four_g = 1
    else:
        four_g = 0
 
    if touchscreen == "touch":
        touch_screen = 1
    else:
        touch_screen = 0  
 
    battery_power = batterypower

    n_cores = cores

    ram = ram
 
    # Making predictions 
    # NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
    # NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
    API_KEY = "H4DAR2ad4eTvD4ZEpOfbxdM4uVbz-oIsUYFC-aLMSOVH"
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
    API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]

    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"fields": ["dual_sim", "battery_power", "four_g", "n_cores", "touch_screen", "ram"], "values": [[dual_sim,battery_power,four_g,n_cores,touch_screen,ram]]}]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/07f062cc-4693-4602-9857-aaff526f37b1/predictions?version=2023-02-11', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    prediction =response_scoring.json()
    prediction = prediction['predictions'][0]['values'][0][0]
    
        
    if prediction == 0:
        pred = 'low priced'
    elif prediction == 1:
        pred = 'low-mid price'
    elif prediction == 2:
        pred = 'mid-high price'
    elif prediction == 3:
        pred = 'high priced'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    #side bar menu
    
    selected = option_menu(
        menu_title = None,#required
        options =["Home","Code","Predictor"],#required
        icons =["house","code","stars"],#optinal
        menu_icon = "cast",#optinal
        default_index = 2,#optinal
        orientation = "horizontal"     
        )
        
    if selected == "Predictor":
            st.title("""Mobile Phone Price Predictor:iphone: :dollar:""")   
            dualsim = st.selectbox('dual sim',("true","false"))
            batterypower = st.number_input('battery power',min_value=500,max_value=2000,step=100) 
            cores = st.number_input("number of cores",min_value=1,max_value=8,step=1) 
            ram = st.number_input("Total ram",min_value=100,max_value=4000,step=100)
            fourg = st.selectbox('4G enabled',("true","false"))
            touchscreen = st.selectbox('touch enabled',("touch","non-touch"))
            result =""
            
            # when 'Predict' is clicked, make the prediction and store it 
            if st.button("Predict"): 
                result = prediction(dualsim, batterypower, fourg, cores, touchscreen,ram) 
                st.success('Your phone is {}'.format(result))

    if selected == "Code":
        pass

    if selected == "Home":
        pass
        
     
if __name__=='__main__': 
    main()
