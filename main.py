# STEP 1: Import the only two tools we need
import pandas as pd
from sklearn.linear_model import LinearRegression

# STEP 2: Create a simple, readable table of gadget data
# 1 = Yes, 0 = No (This is how we tell the computer the product type!)
data = {
    'Is_Laptop':,
    'Is_Smartphone':,
    'RAM_GB':,
    'Storage_GB':,
    'Price_INR':     [65000, 45000, 30000, 18000, 12000, 5000]
}

# Convert this data into a structured table (DataFrame)
df = pd.DataFrame(data)

print("--- Our Simple Gadget Dataset ---")
print(df)
print("\n---------------------------------")

# STEP 3: Separate our inputs (X) from what we want to predict (y)
# Inputs: Is it a laptop? Is it a phone? How much RAM and Storage?
X = df[['Is_Laptop', 'Is_Smartphone', 'RAM_GB', 'Storage_GB']]
# Target: The actual price
y = df['Price_INR']

# STEP 4: Create and train the Machine Learning model
model = LinearRegression()
model.fit(X, y)

print("[Success] The model has learned the pricing patterns!")

# STEP 5: Test the model with a completely new gadget!
# Let's predict the price of a new Smartphone (Is_Laptop=0, Is_Smartphone=1) with 6GB RAM and 128GB Storage
new_gadget = [[0, 1, 6, 128]]

predicted_price = model.predict(new_gadget)

print(f"\nPredicted Price for your custom smartphone: ₹{predicted_price:.2f}")
