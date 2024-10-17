import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def main():
    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)# 업데이트

    st.pyplot(fig)

if __name__ == "__main__":
    main()