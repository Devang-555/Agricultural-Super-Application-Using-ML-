# 🌾 Agricultural Super Application Using Machine Learning

A Python-based mini project that demonstrates how **Machine Learning**, **GUI development**, and **text-to-speech** can be combined to build a simple agricultural decision-support system.

This application:
- Predicts crop yield based on environmental factors
- Recommends suitable pesticides for selected crops
- Visualizes yield and profit statistics
- Provides voice feedback using text-to-speech

---

## 🚀 Features

### 1️⃣ Crop Yield Prediction
- Uses a **Random Forest Regressor**
- Input parameters:
  - Temperature (°C)
  - Humidity (%)
  - Rainfall (mm)
- Outputs predicted yield in **tons per hectare**
- Prediction is also spoken aloud using text-to-speech

### 2️⃣ Pesticide Recommendation System
- Supports crops:
  - Wheat
  - Corn
  - Rice
- Displays:
  - Recommended pesticide
  - Expected yield increase (%)
  - Potential profit per acre
- Includes **bar chart visualization** using Matplotlib
- Voice feedback for recommendations

### 3️⃣ Graphical User Interface (GUI)
- Built using **Tkinter**
- Simple, beginner-friendly layout
- Interactive input fields and buttons

---

## 🧠 Machine Learning Model

- Algorithm: **RandomForestRegressor**
- Library: `scikit-learn`
- Trained on a **sample dataset** (simulated data similar to public agricultural datasets)
- Features used:
  - Temperature
  - Humidity
  - Rainfall

> ⚠️ Note: This project uses sample data for educational purposes, not real-world agricultural predictions.

---

## 🛠️ Technologies & Libraries Used

- Python 3.12
- Tkinter (GUI)
- NumPy
- Scikit-learn
- Matplotlib
- pyttsx3 (Text-to-Speech)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Devang-555/Agricultural-Super-Application-Using-ML-.git
cd Agricultural-Super-Application-Using-ML-




2️⃣ Install required libraries
pip install numpy matplotlib scikit-learn pyttsx3

3️⃣ Run the application
python Dev.py


The application can be run using:

Python IDLE (Python 3.12 recommended)

Jupyter Notebook (with required libraries installed)

🖥️ How to Use

Enter temperature, humidity, and rainfall values

Click Predict Yield

Enter a crop name (Wheat / Corn / Rice)

Click Get Pesticide Recommendation

View results, hear voice output, and see graphs

📊 Sample Input
Temperature	Humidity	Rainfall
25°C	80%	300 mm
📌 Project Status

✅ Functional

✅ Beginner-friendly

🔄 Can be extended with real datasets, APIs, or databases

🔮 Future Improvements

Use real Kaggle or government agricultural datasets

Add soil parameters (pH, nitrogen, potassium)

Add more crops and pesticides

Convert to a web application (Flask / Django)

Improve UI design

👤 Author

Devang
Student | Machine Learning Enthusiast
