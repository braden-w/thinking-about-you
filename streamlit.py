import streamlit as st
import numpy as np
import json
import pandas as pd

"""
# Thinking about you ♥️
Hi Carrie! This is Braden :)

It's you're birthday, and I wanted to say hi and let you know that I'm thinking about you.  This is a repository of every thought I had of you during this summer :)

While I was at London, I made an app which recorded the time and location whenever I thought of you and pressed a button. The goal was to let you see how much I'm thinking about you. It's a little silly, but I hope you like it (because your architecture friends were roasting me LOL).
"""

st.image("assets/thinking about you.jpg")

"""I exported the database and then converted it into a GeoJSON file (a file which can be visualized on a map) to double check that everything was working. You can also see the file hosted [here](https://github.com/braden-w/thinking-about-you)."""

# Set map_data to the geojson.json data
with open("assets/geojson.json") as response:
    map_data = json.load(response)
map_data

"""Then I converted it into a pandas dataframe so that I could do some data manipulation."""

# Turn the geojson into a pandas dataframe with a lat and lon column
geojson_df = pd.DataFrame(map_data['features'])
geojson_df['lat'] = geojson_df['geometry'].apply(lambda x: x['coordinates'][1])
geojson_df['lon'] = geojson_df['geometry'].apply(lambda x: x['coordinates'][0])
geojson_df

"""Finally, I used the streamlit library to create a map and a slider to visualize the data."""

# Create a map and a slider to visualize the data
st.map(geojson_df)

slider = st.slider("How much do you love me?😍", 0, 100) 

# If the slider is at 100, show a secret message
if slider == 100:
    st.write("I love you too! :)")
# If the slider is at 0, show a secret message
if slider == 0:
    st.write("I'm sorry I'm not good enough for you :(")



"""
## A Problem
An issue I encountered was that the app didn't register the location every time I pressed the button, which may have been because I didn't have internet all the time. I thought I had taken care of that case with Firebase, but it didn't work. So I decided to gather some telemetry from my phone to filll in the gaps.
"""

# Load the "Records.json" file
with open("assets/location_history.json") as response:
    data = json.load(response)
  
# For every record in the data, save the time, lat, and lon in a pandas dataframe
location_history_df = pd.DataFrame(data['locations'])
# Filter down to records where "timestamp" begins with 2022
location_history_df = location_history_df[location_history_df['timestamp'].str.startswith('2022')]
# Rename the "latitudeE7" and "longitudeE7" columns to "lat" and "lon"
location_history_df = location_history_df.rename(columns={"latitudeE7": "lat", "longitudeE7": "lon"})
# Divide the lat and lon columns by 10^7 to get the actual lat and lon
location_history_df['lat'] = location_history_df['lat'].apply(lambda x: x/10**7)
location_history_df['lon'] = location_history_df['lon'].apply(lambda x: x/10**7)
# Filter out duplicate records where lat and lon are the same
location_history_df = location_history_df.drop_duplicates(subset=['lat', 'lon'])
# Truncate the lat and lon columns to 3 decimal places
location_history_df['lat'] = location_history_df['lat'].apply(lambda x: round(x, 3))
location_history_df['lon'] = location_history_df['lon'].apply(lambda x: round(x, 3))
location_history_df

st.map(location_history_df)