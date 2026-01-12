import streamlit as st
import pickle
import numpy as np

# Load model and encoder
model = pickle.load(open(r"C:\Users\ADMIN\Documents\Project\forest_cover_model.pkl", "rb"))
encoder = pickle.load(open(r"C:\Users\ADMIN\Documents\Project\cover_type_encoder.pkl", "rb"))

st.title("Forest Cover Type Prediction")

st.header("Enter Forest Feature Values:")

# Numeric features

Elevation = st.number_input("Elevation (m)", key="elevation")
Aspect = st.number_input("Aspect (degrees)", key="aspect")
Slope = st.number_input("Slope (degrees)", key="slope")
Horizontal_Distance_To_Hydrology = st.number_input("Horizontal Distance to Hydrology (m)", key="hd_hydro")
Vertical_Distance_To_Hydrology = st.number_input("Vertical Distance to Hydrology (m)", key="vd_hydro")
Horizontal_Distance_To_Roadways = st.number_input("Horizontal Distance to Roadways (m)", key="hd_road")
Hillshade_9am = st.number_input("Hillshade at 9am", key="hillshade_9am")
Hillshade_Noon = st.number_input("Hillshade at Noon", key="hillshade_noon")
Hillshade_3pm = st.number_input("Hillshade at 3pm", key="hillshade_3pm")
Horizontal_Distance_To_Fire_Points = st.number_input("Horizontal Distance to Fire Points (m)", key="hd_fire")
Wilderness_Area = st.number_input("Wilderness Area", min_value=1, max_value=4, key="wa")
Soil_Type = st.number_input("Soil Type", min_value=1, max_value=43, key="soil")
Hydro_Ratio= st.number_input("Hydro Ratio", min_value=0, max_value=1, key="Hydro_Ratio")
Shade_Diff = st.number_input("Shade Difference", min_value=0, max_value=1, key="Shade_Diff")

# Predict button
if st.button("Predict"):
    # Combine all inputs into a single array
    input_data = [Elevation, Aspect, Slope, Horizontal_Distance_To_Hydrology,
                  Vertical_Distance_To_Hydrology, Horizontal_Distance_To_Roadways,
                  Hillshade_9am, Hillshade_Noon, Hillshade_3pm, Horizontal_Distance_To_Fire_Points,
                  Wilderness_Area, Soil_Type,Hydro_Ratio,Shade_Diff]

    
    input_array = np.array([input_data])


    
    # Make prediction
    pred = model.predict(input_array)
    st.success(f"Predicted Forest Cover Type: {encoder.inverse_transform(pred)[0]}")


    