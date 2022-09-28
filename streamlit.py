import streamlit as st
import json

with open("geojson.json") as response:
    grid = json.load(response)

import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

