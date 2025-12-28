# 🌋 Debris Flow Doom Tracker
**Real-time Monitoring & Risk Assessment for Geological Hazards**

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Type](https://img.shields.io/badge/Focus-Geological%20Hazards-red.svg)
![Status](https://img.shields.io/badge/Development-Active-green.svg)

## 📌 Project Overview
Debris flows (massive mudslides) are among the most dangerous geological events. The **Doom Tracker** is a data-driven system designed to monitor rainfall thresholds, soil conditions, and terrain slope to predict and track potential debris flow events.

This project aims to provide an early-warning framework by analyzing historical landslide data and real-time triggers.

## 🚀 Key Features
- **Rainfall Threshold Analysis:** Tracks Cumulative Rainfall Intensity (I-D curves) to predict when soil reaches a breaking point.
- **Geospatial Mapping:** Visualizes high-risk zones based on elevation and slope data.
- **Predictive Modeling:** Uses Machine Learning (Random Forest/XGBoost) to classify "Safe" vs. "Doom" (Hazard) conditions.
- **Real-time Alerts:** System logic for triggering warnings when sensors/data cross safety limits.

## 🛠️ Tech Stack
- **Languages:** Python (Pandas, NumPy, Matplotlib)
- **GIS Tools:** GeoPandas, Rasterio (for mapping terrain)
- **Machine Learning:** Scikit-Learn, XGBoost
- **Data Sources:** NASA Global Landslide Catalog / USGS Rainfall Data

## 📂 Project Structure
```text
├── data/               # Historical landslide & rainfall datasets
├── notebooks/          # Analysis of slope stability & triggers
├── src/                # Prediction algorithms & threshold logic
├── visualizations/     # Risk heatmaps and I-D threshold plots
└── requirements.txt    # Essential libraries
```
## 🤝 Contributing
Geologists and Data Scientists are welcome to contribute. Open an issue to discuss new data sources or algorithmic improvements.

---
*Developed by [Akshat](https://github.com/Akshat8510) to help predict the unpredictable.*
