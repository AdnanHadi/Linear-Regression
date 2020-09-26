# TODO: Add import statements
import pandas as pd

# Assign the dataframe to this variable.
# TODO: Load the data
bmi_life_data = pd.read_csv('bmi_and_life_expectancy.csv')

# Make and fit the linear regression model
#TODO: Fit the model and Assign it to bmi_life_model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
X=bmi_life_data['Life expectancy']
y=bmi_life_data['BMI']
y_hat = model.fit(X,y)
bmi_life_model = None

# Make a prediction using the model
# TODO: Predict life expectancy for a BMI value of 21.07931
laos_life_exp = None
