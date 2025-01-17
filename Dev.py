import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import pyttsx3
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Sample crop yield data similar to what you might find on Kaggle
# Features: Temperature, Humidity, Rainfall
# The following 2D array simulates several data points with crop yield values associated
X = np.array([
    [20, 70, 200],  # Example 1
    [25, 80, 300],  # Example 2
    [30, 60, 250],  # Example 3
    [22, 65, 150],  # Example 4
    [26, 75, 180],  # Example 5
    [28, 85, 220],  # Example 6
])

# Target: Crop Yield values corresponding to above features
y = np.array([3.5, 5.0, 4.5, 3.8, 4.2, 5.1])  # Example yields

# Train a Random Forest Regressor model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Pesticide data for recommendations
pesticide_data = {
    "Wheat": {"Pesticide": "Pesticide A", "Yield Increase (%)": 20, "Potential Profit ($/acre)": 100},
    "Corn":  {"Pesticide": "Insecticide Y", "Yield Increase (%)": 25, "Potential Profit ($/acre)": 150},
    "Rice":  {"Pesticide": "Pesticide D", "Yield Increase (%)": 30, "Potential Profit ($/acre)": 160},
}

def speak(text):
    """Function to convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def predict_yield():
    try:
        # Take input values from the user
        temp = float(entry_temp.get())
        humidity = float(entry_humidity.get())
        rainfall = float(entry_rainfall.get())
        
        # Predict the yield using the ML model
        predicted_yield = model.predict(np.array([[temp, humidity, rainfall]]))

        message = f"The predicted yield for the input conditions is {predicted_yield[0]:.2f} tons per hectare."
        messagebox.showinfo("Predicted Yield", message)
        speak(message)  # Convert prediction to speech
    except ValueError:
        message = "Please enter valid numeric values."
        messagebox.showerror("Input Error", message)
        speak(message)  # Convert error to speech

def get_recommendation():
    crop = crop_entry.get().strip().capitalize()
    try:
        pesticide_info = pesticide_data[crop]

        recommendation = (
            f"Recommended: {pesticide_info['Pesticide']}\n"
            f"Expected Yield Increase: {pesticide_info['Yield Increase (%)']}%\n"
            f"Potential Profit: ${pesticide_info['Potential Profit ($/acre)']}/acre"
        )
        recommendation_label.config(text=recommendation)
        speak(recommendation)  # Convert recommendation to speech
        plot_statistics(pesticide_info)
    except KeyError:
        message = "No suitable pesticide found for the given crop."
        recommendation_label.config(text=message)
        speak(message)  # Convert error to speech

def plot_statistics(pesticide_info):
    # Data for plotting
    labels = ['Yield Increase (%)', 'Potential Profit ($/acre)']
    values = [pesticide_info['Yield Increase (%)'], pesticide_info['Potential Profit ($/acre)']]
    
    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color=['green', 'blue'])
    plt.ylabel('Value')
    plt.title('Pesticide Effectiveness and Profit Potential')
    plt.ylim(0, max(values) + 50)  # Adjust y-axis limit to improve visualization
    plt.show()

# GUI setup
root = tk.Tk()
root.title("Agricultural Super Application")
root.geometry("600x600")

header = tk.Label(root, text="Agricultural Super Application", font=("Arial", 18))
header.pack(pady=10)

# Crop Yield Prediction UI
tk.Label(root, text="Crop Yield Prediction", font=("Arial", 14)).pack(pady=10)
tk.Label(root, text="Temperature (°C):").pack()
entry_temp = tk.Entry(root)
entry_temp.pack()
tk.Label(root, text="Humidity (%):").pack()
entry_humidity = tk.Entry(root)
entry_humidity.pack()
tk.Label(root, text="Rainfall (mm):").pack()
entry_rainfall = tk.Entry(root)
entry_rainfall.pack()
tk.Button(root, text="Predict Yield", command=predict_yield).pack(pady=10)

# Pesticide Recommendation UI
tk.Label(root, text="Pesticide Recommendation System", font=("Arial", 14)).pack(pady=10)
tk.Label(root, text="Enter Crop Type (Wheat, Corn, Rice):").pack()
crop_entry = tk.Entry(root)
crop_entry.pack()
tk.Button(root, text="Get Pesticide Recommendation", command=get_recommendation).pack(pady=10)
recommendation_label = tk.Label(root, text="", font=("Arial", 12))
recommendation_label.pack(pady=10)

root.mainloop()
