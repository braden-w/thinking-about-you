import streamlit as st
import numpy as np
import json
import pandas as pd

"""# Thinking about you ♥️
Hi Carrie! This is Braden :)

It's you're birthday, and I wanted to say hi and let you know that I'm thinking about you.  This is a repository of every thought I had of you during this summer :)

While I was at London, I made an app which recorded the time and location whenever I thought of you and pressed a button. The goal was to let you see how much I'm thinking about you. It's a little silly, but I hope you like it (because your architecture friends were roasting me LOL).
"""

st.image("thinking about you.jpg")

"""I exported the database and then converted it into a GeoJSON file (a file which can be visualized on a map) to double check that everything was working. You can also see the file hosted [here](https://github.com/braden-w/thinking-about-you)."""

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

slider = st.slider("How much do you love me?😍", 0, 100) 

# If the slider is at 100, show a secret message
if slider == 100:
    st.write("I love you too! :)")
# If the slider is at 0, show a secret message
if slider == 0:
    st.write("I'm sorry I'm not good enough for you :(")



"""## A Problem
An issue I encountered was that the app didn't regester the location every time I pressed the button, which may have been because I didn't have internet all the time. Firebase was supposed to take care of i, but it didn't work.
"""

# Load the "Records.json" file
with open("Records.json") as response:
    data = json.load(response)
  
# For every record in the data, save the time, lat, and lon in a pandas dataframe
df = pd.DataFrame(data['locations'])
df