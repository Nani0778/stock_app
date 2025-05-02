import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib  # or pickle
import os

# Page config
st.set_page_config(page_title="📈 Stock Trend Analyzer", layout="centered")

# Logo
st.image("static/logo.png", width=150)

st.title("📊 Stock Trend Analyzer")
st.markdown("Upload your stock CSV file to predict future trend using our AI model.")

# File uploader
file = st.file_uploader("Choose your Stock CSV file", type="csv")

if file:
    df = pd.read_csv(file)
    st.write("### Uploaded Data", df.head())

    # Add your preprocessing steps here
    # Example:
    # features = df[['Open', 'High', 'Low', 'Close', 'Volume']]
    # X = preprocess(features)

    # Simulated prediction for demonstration
    prediction = np.random.choice(["Up", "Down"])
    accuracy = np.random.uniform(70, 95)

    # Display results
    st.markdown(f"### Prediction: 📈 Stock may go **{'🔼' if prediction == 'Up' else '🔻'} {prediction}**")
    st.markdown(f"### Model Accuracy: `{accuracy:.2f}%`")

    # Simulate plot generation (you can replace this with your actual plotting code)
    fig, ax = plt.subplots()
    df['Close'].plot(ax=ax, title='Stock Closing Price')
    st.pyplot(fig)

# Optional: Add live ticker via TradingView (HTML)
st.markdown("---")
st.markdown("### Live Ticker: Apple (AAPL)")
tradingview_html = """
<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>
  {
    "symbol": "NASDAQ:AAPL",
    "width": "100%",
    "height": "100",
    "locale": "en",
    "dateRange": "1D",
    "colorTheme": "light",
    "trendLineColor": "rgba(41, 98, 255, 1)",
    "underLineColor": "rgba(41, 98, 255, 0.3)",
    "isTransparent": false,
    "autosize": true
  }
  </script>
</div>
<!-- TradingView Widget END -->
"""
components.html(tradingview_html, height=120)
