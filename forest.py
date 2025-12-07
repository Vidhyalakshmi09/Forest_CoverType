import streamlit as st
import pickle
import numpy as np

# Load model and encoder
model = pickle.load(open(r"C:\Users\ADMIN\Desktop\Projects\Heathcare_Project\forest_cover_model.pkl", "rb"))
encoder = pickle.load(open(r"C:\Users\ADMIN\Desktop\Projects\Heathcare_Project\cover_type_encoder.pkl", "rb"))

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

# Categorical/Binary features
Wilderness_Area_1 = st.number_input("Wilderness Area 1", min_value=0, max_value=1, key="wa1")
Wilderness_Area_2 = st.number_input("Wilderness Area 2", min_value=0, max_value=1, key="wa2")
Wilderness_Area_3 = st.number_input("Wilderness Area 3", min_value=0, max_value=1, key="wa3")
Wilderness_Area_4 = st.number_input("Wilderness Area 4", min_value=0, max_value=1, key="wa4")

Soil_Type_inputs = []
for i in range(1, 43):
    Soil_Type_inputs.append(st.number_input(f"Soil Type {i}", min_value=0, max_value=1, key=f"soil{i}"))

# Predict button
if st.button("Predict"):
    # Combine all inputs into a single array
    input_data = [Elevation, Aspect, Slope, Horizontal_Distance_To_Hydrology,
                  Vertical_Distance_To_Hydrology, Horizontal_Distance_To_Roadways,
                  Hillshade_9am, Hillshade_Noon, Hillshade_3pm, Horizontal_Distance_To_Fire_Points,
                  Wilderness_Area_1, Wilderness_Area_2, Wilderness_Area_3, Wilderness_Area_4] + Soil_Type_inputs
    
    input_array = np.array([input_data])
    
    # Make prediction
    pred = model.predict(input_array)
    st.success(f"Predicted Forest Cover Type: {encoder.inverse_transform(pred)[0]}")


    