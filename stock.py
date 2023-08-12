import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn import *


def predict_high(com):

    if (com in company and com == "Apple"):
        apple_h_pred = apple_h_reg.predict([[option1, option2, option3]])
        return np.round(apple_h_pred[0], 2)
    if (com in company and com == "Amazon"):
        amazon_h_pred = amazon_h_reg.predict([[option1, option2, option3]])
        return np.round(amazon_h_pred[0], 2)
    if (com in company and com == "Google"):
        google_h_pred = google_h_reg.predict([[option1, option2, option3]])
        return np.round(google_h_pred[0], 2)
    if (com in company and com == "Microsoft"):
        microsoft_h_pred = microsoft_h_reg.predict([[option1, option2, option3]])
        return np.round(microsoft_h_pred[0], 2)
    return 0


def predict_low(com):

    if (com in company and com == "Apple"):
        apple_l_pred = apple_l_reg.predict([[option1, option2, option3]])
        return np.round(apple_l_pred[0], 2)
    if (com in company and com == "Amazon"):
        amazon_l_pred = amazon_l_reg.predict([[option1, option2, option3]])
        return np.round(amazon_l_pred[0], 2)
    if (com in company and com == "Google"):
        google_l_pred = google_l_reg.predict([[option1, option2, option3]])
        return np.round(google_l_pred[0], 2)
    if (com in company and com == "Microsoft"):
        microsoft_l_pred = microsoft_l_reg.predict([[option1, option2, option3]])
        return np.round(microsoft_l_pred[0], 2)
    return 0


def no_of_days(month, year):
    if month == 2:
        if (year % 4 == 0):
            return np.arange(1, 30)
        else:
            return np.arange(1, 29)

    if month in [1,3, 5, 7, 8, 10, 12]:
        return np.arange(1, 32)
    if month in [4, 6, 9, 11]:
        return np.arange(1, 31)
    return []


apple_h_reg = pickle.load(open("apple_h_reg.pkl", "rb"))
apple_l_reg = pickle.load(open("apple_l_reg.pkl", "rb"))
amazon_h_reg = pickle.load(open("amazon_h_reg.pkl", "rb"))
amazon_l_reg = pickle.load(open("amazon_l_reg.pkl", "rb"))
google_h_reg = pickle.load(open("google_h_reg.pkl", "rb"))
google_l_reg = pickle.load(open("google_l_reg.pkl", "rb"))
microsoft_h_reg = pickle.load(open("microsoft_h_reg.pkl", "rb"))
microsoft_l_reg = pickle.load(open("microsoft_l_reg.pkl", "rb"))


st.title("Stock Price Predictor")

company = st.selectbox("Which company's share do you want to predict", options = ["Select Company"] + sorted(["Apple", "Amazon", "Google", "Microsoft"]))
year = np.arange(2010, 2100)
months = np.arange(1, 13)

col1, col2, col3 = st.columns(3)
with col1:
    option1 = st.selectbox("Select Year", ["Select Year"] + list(year))

with col2:
    option2 = st.selectbox("Select Month", ["Select Month"] + list(months))

with col3:
    dates = list(no_of_days(option2, option1))
    option3 = st.selectbox("Select Date", ["Select Date"] + dates)


colb1, colb2 = st.columns(2)
with colb1:
    if st.button("Predict Stock's Highest Price"):
        label_h = "Predicted Highest Price : ₹ " + str(predict_high(company))
        st.write(label_h)
with colb2:
    if st.button("Predict Stock's Lowest Price"):
        label_l = "Predicted Lowest Price : ₹ " + str(predict_low(company))
        st.write(label_l)
