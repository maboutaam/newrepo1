import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.header('Tossing a Coin')

# User input
number_of_trials = st.slider('Number of trials?', 1, 1000, 10)
start_button = st.button('Run')

# Simulation
if start_button:
    # Generate random outcomes
    outcomes = np.random.choice([0, 1], size=number_of_trials)
    
    # Calculate mean
    mean = np.mean(outcomes)
    
    # Plot progress
    fig, ax = plt.subplots()
    ax.plot(outcomes)
    ax.axhline(y=mean, color='r', linestyle='--')
    ax.set_title('Coin Toss Simulation')
    ax.set_xlabel('Trial')
    ax.set_ylabel('Outcome (0 or 1)')
    st.pyplot(fig)
    
    # Show results table
    results = pd.DataFrame({'Outcome': outcomes})
    st.dataframe(results)
    st.write(f'Mean outcome: {mean:.2f}')