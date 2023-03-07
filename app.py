import streamlit as st
import pandas as pd

st.title("The main dataset")
data = pd.read_csv('/Users/amogharya/Documents/projects/IOT2_LAB/Lab_exp_5/automobile1.csv')
st.dataframe(data)

import matplotlib.pyplot as plt

fig = plt
fig.scatter(data['engine-size'],data['price'])
plt.xlabel('Engine Size')
plt.ylabel('price')
plt.show

st.plotly_chart(plt)
