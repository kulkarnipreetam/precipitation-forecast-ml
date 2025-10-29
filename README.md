# 🌦️ Two-Stage Weather Forecast Pipeline  

> A machine learning pipeline for forecasting **precipitation events and intensity** using open meteorological data from the [Open-Meteo API](https://open-meteo.com/).  

---

## 🧠 Project Overview  

This project builds a **two-stage machine learning pipeline** for precipitation forecasting:  

1. **Stage 1 – Classification:** Determines whether precipitation (rain, snow, sleet, etc.) will occur.  
2. **Stage 2 – Regression:** Predicts the **precipitation intensity (mm)** when precipitation is expected.  

The system uses **hourly and daily weather data** from the Open-Meteo API and can be extended to multiple cities. The workflow was prototyped using data from **Greensboro, North Carolina**.
It forms the foundation for a cloud-integrated, continuously updating precipitation forecasting platform.

---

## ⚙️ Notebook Contents (`two_stage_weather_forecast_pipeline.ipynb`)

### **Stage 1: Precipitation Classification (Will it precipitate?)**
- **Objective:** Predict whether any form of precipitation will occur.  
- **Model:** `XGBoostClassifier`  
- **Methods:**  
  - Binary classification (Yes / No)  
  - Feature engineering, normalization, and correlation checks  
  - Metrics: Accuracy, Precision, Recall, F1-score, ROC-AUC  

### **Stage 2: Precipitation Intensity Regression (How much will it precipitate?)**
- **Objective:** Estimate the **precipitation amount (mm)** when Stage 1 predicts precipitation.  
- **Model:** `CatBoostRegressor`  
- **Methods:**  
  - Log-transform of target to reduce skewness  
  - Inverse transformation of predictions for interpretability  
  - Metrics: MAE, RMSE, and R²  

### **Other Highlights**
### **Example Results: Greensboro, North Carolina**

The model was evaluated on hourly weather data for Greensboro, NC.  
The calibration process helped stabilize predictions, especially for smaller precipitation events.

#### Stage 1 – Precipitation Classification Metrics (Test Set)

| Class | Precision | Recall | F1-score | Support |
|-------|-----------|--------|----------|---------|
| 0 (No Precipitation) | 0.97 | 0.96 | 0.96 | 6393 |
| 1 (Precipitation)    | 0.75 | 0.79 | 0.77 | 1009 |

| Metric       | Value |
|--------------|-------|
| **Accuracy** | 0.94  |
| **Macro Avg Precision** | 0.86 |
| **Macro Avg Recall**    | 0.88 |
| **Macro Avg F1-score**  | 0.87 |
| **Weighted Avg Precision** | 0.94 |
| **Weighted Avg Recall**    | 0.94 |
| **Weighted Avg F1-score**  | 0.94 |

#### Stage 2 – Precipitation Amount Regression Metrics

| Metric | Train | Test |
|--------|-------|------|
| **RMSE (mm)** | 0.86 | 1.00 |
| **MAE (mm)**  | 0.56 | 0.64 |
| **R² Score**  | 0.71 | 0.57 |

**Observations:**
- The **classification model** performed reliably with strong discriminative ability (AUC = 0.97).  
- **Calibration** improved regression stability by reducing bias on low-intensity precipitation events.  
- **Precipitation events are relatively rare** in the dataset (occurring in less than ~15% of hourly records).  
  - This imbalance required careful tuning of model thresholds and evaluation metrics beyond raw accuracy.  
  - Metrics like **Precision, Recall, and AUC** provided a more balanced assessment of model performance.  
- Results indicate strong generalization capability for daily and hourly forecasting tasks.

---

## 🧩 Input Features  

The dataset is sourced from the **Open-Meteo API**, which provides rich hourly and daily weather attributes.  
Some variables were **engineered or derived** from the raw features to improve model performance (e.g., temperature differentials, normalized humidity index, radiation ratios, etc.).

| **Category** | **Features** |
|---------------|--------------|
| 🌡️ **Temperature** | `temperature_2m`, `dew_point_2m`, `apparent_temperature`, `wet_bulb_temperature_2m` |
| 💧 **Humidity & Moisture** | `relative_humidity_2m`, `vapour_pressure_deficit`, `soil_moisture_0_to_7cm`, `soil_moisture_7_to_28cm`, `soil_moisture_28_to_100cm`, `soil_moisture_100_to_255cm`, `total_column_integrated_water_vapour` |
| 🌦️ **Precipitation & Snow** | `precipitation`, `rain`, `snowfall`, `snow_depth`, `weather_code` |
| 🌬️ **Wind Metrics** | `wind_speed_10m`, `wind_speed_100m`, `wind_direction_10m`, `wind_direction_100m`, `wind_gusts_10m` |
| ☁️ **Cloud Cover** | `cloud_cover`, `cloud_cover_low`, `cloud_cover_mid`, `cloud_cover_high` |
| 🌞 **Radiation & Sunshine** | `shortwave_radiation`, `direct_radiation`, `diffuse_radiation`, `direct_normal_irradiance`, `global_tilted_irradiance`, `terrestrial_radiation`, `sunshine_duration`, and corresponding `_instant` variables |
| 🌾 **Evaporation & Energy Balance** | `et0_fao_evapotranspiration`, `boundary_layer_height` |
| 🌍 **Pressure** | `pressure_msl`, `surface_pressure` |
| 🌡️ **Soil Temperature (by depth)** | `soil_temperature_0_to_7cm`, `soil_temperature_7_to_28cm`, `soil_temperature_28_to_100cm`, `soil_temperature_100_to_255cm` |
| ☀️ **Day/Night Indicator** | `is_day` |
| 📅 **Temporal Variable** | `date` |

---

## 🚀 Future Work (Work in Progress)

### **1️⃣ Cloud Integration**
- Establish a **Cloud SQL database** to store and update weather data for multiple cities.  
- Use **GitHub Actions** to automate daily data retrieval and ingestion from the Open-Meteo API.

### **2️⃣ Automated Model Retraining**
- Schedule weekly retraining pipelines using GitHub Actions whenever new data is available.  
- Push retrained models to GitHub or cloud storage for versioned deployment.

### **3️⃣ Streamlit Web App**
- Build a **Streamlit dashboard** for hourly precipitation forecasts.  
- Display:  
  - Probability of precipitation (Stage 1)  
  - Predicted intensity in mm (Stage 2)  
  - Historical trend charts and feature importance visualizations.  
- The focus will remain on **precipitation forecasting**, not just rainfall, for city-agnostic accuracy.  

---

## 🧰 Tech Stack  

| **Category** | **Tools / Libraries** |
|---------------|-----------------------|
| 💻 **Language** | Python 🐍 |
| 📊 **Data Source** | Open-Meteo API |
| 🤖 **Modeling** | XGBoost, CatBoost, scikit-learn |
| 📈 **Visualization** | Matplotlib |
| ☁️ **Automation (Future)** | GitHub Actions, Cloud SQL |
| 🌐 **Deployment (Future)** | Streamlit, GitHub Pages / Streamlit Cloud |

---

## 📈 Typical Workflow  

1. Fetch and preprocess weather data from the Open-Meteo API.  
2. Train **Stage 1** (classification): Will it precipitate?  
3. Train **Stage 2** (regression): How much will it precipitate?  
4. Evaluate models using cross-validation and visualizations.  
5. Save and prepare models for automation and deployment.  

---


## Important Notice

The code in this repository is proprietary and protected by copyright law. Unauthorized copying, distribution, or use of this code is strictly prohibited. By accessing this repository, you agree to the following terms:

- **Do Not Copy:** You are not permitted to copy any part of this code for any purpose.
- **Do Not Distribute:** You are not permitted to distribute this code, in whole or in part, to any third party.
- **Do Not Use:** You are not permitted to use this code, in whole or in part, for any purpose without explicit permission from the owner.

If you have any questions or require permission, please contact the repository owner.

Thank you for your cooperation.
