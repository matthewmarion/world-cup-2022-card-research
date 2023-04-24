import pandas as pd
import numpy as np
import statsmodels.api as sm

# Placeholder for data. Acquire this data from generate.py
data = [(2, 1), (1, 0), (0, 1), (3, 0), (3, 0), (0, 1), (0, 0), (1, 1), (3, 1), (1, 0), (6, 0), (1, 1), (1, 0), (1, 1), (1, 1), (2, 0), (1, 1), (4, 0), (1, 1), (1, 0), (1, 1), (0, 0), (0, 1), (2, 0), (0, 1), (1, 0), (2, 1), (2, 0), (1, 0), (3, 1), (0, 1), (1, 0), (0, 1), (1, 0), (0, 1), (2, 0), (1, 1), (2, 0), (2, 1), (0, 0), (7, 0), (4, 1), (3, 1), (2, 0), (3, 0), (3, 1), (1, 0), (1, 1), (4, 0), (2, 1), (3, 0), (3, 1), (0, 0), (6, 1), (2, 0), (2, 1), (2, 1), (4, 0), (3, 1), (2, 0), (2, 0), (5, 1), (1, 0), (0, 1), (0, 1), (2, 0), (2, 1), (1, 0), (2, 0), (1, 1), (2, 1), (2, 0), (4, 1), (2, 0), (0, 1), (3, 0), (3, 0), (1, 1), (4, 0), (0, 1), (1, 1), (0, 0), (2, 0), (2, 1), (0, 1), (2, 0), (3, 1), (2, 0), (2, 1), (0, 0), (2, 0), (0, 1), (3, 1), (0, 0)]

# Create pandas dataframe from data
df = pd.DataFrame(data, columns=['Quantity of Cards', 'Outcome'])

# Add intercept column
df['Intercept'] = 1

# Create linear regression model
model = sm.Logit(df['Outcome'], df[['Intercept', 'Quantity of Cards']])

# Fit the model and print results
results = model.fit()
print(results.summary())
