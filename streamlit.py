import streamlit as st
import numpy as np
import json
import pandas as pd

"""# Thinking about you
Hi Carrie! This is Braden :)

It's you're birthday, and I wanted to say hi and let you know that I'm thinking about you.

While I was at London, I made an app that recorded the weather every day. I thought it would be fun to see."""

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