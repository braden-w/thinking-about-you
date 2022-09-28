import streamlit as st
import numpy as np
import json
import pandas as pd

"""# Thinking about you
Hi Carrie! This is Braden :)

It's you're birthday, and I wanted to say hi and let you know that I'm thinking about you.

While I was at London, I made an app that lets you see how much I'm thinking about you. It's a little silly, but I hope you like it (because you're architecture friends were roasting me LOL)."""



"""I exported the database and then converted it into a GeoJSON file (a file which can be visualized on a map) to double check that everything was working."""

# Set map_data to the geojson.json data
with open("geojson.json") as response:
    map_data = json.load(response)
map_data

"""Then I converted it into a pandas dataframe so that I could do some data manipulation."""

# Turn the geojson into a pandas dataframe with a lat and lon column
df = pd.DataFrame(map_data['features'])
df['lat'] = df['geometry'].apply(lambda x: x['coordinates'][1])
df['lon'] = df['geometry'].apply(lambda x: x['coordinates'][0])
df

"""Finally, I used the streamlit library to create a map and a slider to visualize the data."""

# Create a map and a slider to visualize the data
st.map(df)
st.slider("How much do you love me?", 0, 100)