import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# --- Pre-trained Model Parameters (from previous training or a known model) ---
# In a real application, these would come from a saved model file (e.g., using joblib or pickle)
# For this basic example, we'll hardcode coefficients and intercept derived from the
# synthetic data generation and training in the previous version of this script.
# These values are illustrative and would be learned from real data.

# Coefficients for: size_sqft, num_bedrooms, age_years, location_score
# These are approximate values based on the synthetic data's underlying linear relationship
# and what a trained model might produce.
model_coefficients = np.array([99.98, 9991.60, -500.55, 19998.70])
model_intercept = 10000.0 # An approximate intercept

# Initialize a Linear Regression model and set its parameters
# We are 'simulating' a trained model here by setting its coefficients and intercept directly.
model = LinearRegression()
model.coef_ = model_coefficients
model.intercept_ = model_intercept
# Note: In a real scenario, you'd load a pre-trained model like this:
# from joblib import load
# model = load('house_price_model.joblib')

print("--- House Price Prediction ---")
print("Please enter the details for the house to get a price prediction.")

# --- Get User Input for House Features ---
try:
    size_sqft = float(input("Enter house size in square feet (e.g., 1500): "))
    num_bedrooms = int(input("Enter number of bedrooms (e.g., 3): "))
    age_years = int(input("Enter age of the house in years (e.g., 10): "))
    location_score = int(input("Enter location score (1-10, 10 being best): "))

    # Basic input validation
    if not (800 <= size_sqft <= 5000): # Assuming a reasonable range for size
        print("Warning: Size seems unusual. Please enter a realistic value.")
    if not (1 <= num_bedrooms <= 10):
        print("Warning: Number of bedrooms seems unusual. Please enter a realistic value.")
    if not (0 <= age_years <= 100):
        print("Warning: Age seems unusual. Please enter a realistic value.")
    if not (1 <= location_score <= 10):
        print("Warning: Location score must be between 1 and 10.")

except ValueError:
    print("Invalid input. Please ensure you enter numbers for all fields.")
    exit() # Exit if input is invalid

# --- Prepare User Input for Prediction ---
# Create a Pandas DataFrame from the user's input, matching the feature names
user_input_features = pd.DataFrame([[
    size_sqft,
    num_bedrooms,
    age_years,
    location_score
]], columns=['size_sqft', 'num_bedrooms', 'age_years', 'location_score'])

# --- Make Prediction ---
predicted_price = model.predict(user_input_features)

# --- Display Prediction ---
print("\n--- Prediction Result ---")
print(f"Based on your input, the predicted house price is:  ₹ {predicted_price[0]:,.2f}")
print("\n")
print("Thank you for using the house price predictor!")