import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.write('Trigonmetry Functions')
function = st.radio('Chose a function to plot', ['Sin', 'Cos'])
x = []
y = []
pi = 22/7
if function == 'Sin':
    for i in np.linspace(0, 720):
        x.append(np.sin(i*pi/180))
        y.append(i)
elif function == 'Cos':
    for i in np.linspace(0, 720):
        x.append(np.cos(i*pi/180))
        y.append(i)
fig, ax = plt.subplots()
ax.plot(y,x)
st.pyplot(fig)