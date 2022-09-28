import streamlit as st
import numpy as np
import json

import pandas as pd

# Set map_data to the geojson.json data
with open("geojson.json") as response:
    map_data = json.load(response)

map_data

# Turn the geojson into a pandas dataframe with a lat and lon column
df = pd.DataFrame(map_data['features'])
df['lat'] = df['geometry'].apply(lambda x: x['coordinates'][1])
df['lon'] = df['geometry'].apply(lambda x: x['coordinates'][0])
df

st.map(df)