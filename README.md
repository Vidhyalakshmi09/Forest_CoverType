
## 📌 Project Description

This project predicts the **Forest Cover Type** using machine learning models based on environmental and geographical features such as elevation, slope, hydrology distances, soil type, and hillshade indices.

The final trained model is deployed as an **interactive Streamlit web application** for real-time predictions.

---

## 🌳 Forest Cover Types Predicted

* Spruce / Fir
* Lodgepole Pine
* Aspen
* Douglas-fir
* Ponderosa Pine
* Cottonwood / Willow
* Krummholz

---

## 🧠 Machine Learning Pipeline

### 🔹 Dataset

* **Records:** 145,890
* **Features:** 12 original + 2 engineered
* **Target:** `Cover_Type`

---

### 🔹 Data Preprocessing

* Removed duplicates & handled missing values
* Outlier removal using **IQR method**
* Skewness correction using **log transformation**
* Replaced infinite values
* Cleaned and validated numeric features

---

### 🔹 Feature Engineering

```text
Hydro_Ratio = Vertical_Distance_To_Hydrology / (Horizontal_Distance_To_Hydrology + 1)
Shade_Diff  = Hillshade_3pm - Hillshade_9am
```

---

### 🔹 Class Imbalance Handling

* Applied **SMOTE (Synthetic Minority Oversampling Technique)**

---

### 🔹 Feature Selection

* Low variance filtering
* Feature importance using **Random Forest**
* Selected features with importance > 0.01

---

## 🤖 Models Trained & Evaluation

| Model                  | Test Accuracy |
| ---------------------- | ------------- |
| 🌲 Random Forest       | **99.4%**     |
| 🌳 KNN                 | 99.2%         |
| 🌲 Decision Tree       | 98.7%         |
| 🚀 XGBoost             | 98.5%         |
| 📉 Logistic Regression | 65%           |

✔ **Random Forest** was selected as the final model.

---

### 🔹 Hyperparameter Tuning

* Used **RandomizedSearchCV**
* Optimized Random Forest parameters
* Saved trained model using `pickle`

---

## 💾 Saved Artifacts

| File                     | Description                   |
| ------------------------ | ----------------------------- |
| `forest_cover_model.pkl` | Trained Random Forest model   |
| `cover_type_encoder.pkl` | Label encoder for cover types |

---

## 🚀 Streamlit Web Application

### 🔸 Input Features

* Elevation
* Aspect
* Slope
* Distance to Hydrology
* Distance to Roadways
* Hillshade (9am, Noon, 3pm)
* Distance to Fire Points
* Wilderness Area
* Soil Type
* Hydro Ratio
* Shade Difference

### 🔸 Output

✅ **Predicted Forest Cover Type**

---


## 📂 Project Structure

```text
Forest-Cover-Type-Prediction/
│
├── app.py
├── forest_cover_model.pkl
├── cover_type_encoder.pkl
├── forest_cover.ipynb
├── cover_type.csv
├── requirements.txt
└── README.md
```

---

## 🛠️ Technologies Used

* Python
* NumPy, Pandas
* Scikit-learn
* XGBoost
* Imbalanced-learn (SMOTE)
* Matplotlib & Seaborn
* Streamlit

---

## 📊 Results & Conclusion

* Achieved **99.4% accuracy** on test data
* Successfully handled class imbalance
* Deployed a production-ready ML model
* Built a user-friendly web interface

---

## 📌 Future Enhancements

* Deploy on Streamlit Cloud / AWS
* Add feature importance visualization
* Improve UI/UX
* Add CI/CD pipeline

---


⭐ **If you like this project, don’t forget to star the repository!**

---

