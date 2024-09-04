st.title("🎈 My new app")
st.write(
    streamlit_code = """
import streamlit as st
import pandas as pd
st.title("VTEC forecasting")

# CHOOSE SLIDING/ TUMBLING WINDOW
# radio button to choose height format
status = st.radio('Select your window type: ',
                  ('sliding', 'tumbling'))

import csv
with open('threeday vtec_Bang.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        print(lines)


df = pd.read_csv('threeday vtec_Bang.csv')
df.to_csv('data1.csv')

        
"""
)
# Save the Streamlit app to a file
with open("app.py", "w") as f:
    f.write(streamlit_code)

