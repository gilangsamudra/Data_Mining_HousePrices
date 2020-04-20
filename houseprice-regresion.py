# Bismillah
# Import all necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.formula.api import ols

# Load dataset
df = pd.read_csv('D:/Phyton Code/Data_Mining_HousePrices/kc_house_data.csv')

# # Check data quality
# df.info()
# df.head()
# df.tail()
# df.describe()
# df.isnull().any()
# df.dtypes

# Create a figure object
fig = plt.figure(figsize=(12, 6))
sqft = fig.add_subplot(121)
cost = fig.add_subplot(122)

sqft.hist(df.sqft_living, bins=80)
sqft.set_xlabel('Ft^2')
sqft.set_title('Histogram of Housing Prices')

cost.hist(df.price, bins=80)
cost.set_xlabel('Price ($)')
cost.set_title("Histogram of Housing Prices")

# Do a simple single variable regresion calculation
m = ols('price ~ sqft_living', df).fit()
print(m.summary())

# Do a multivariate regresion calculation
mm = ols('price ~ sqft_living + bedrooms + condition + grade', df).fit()
print(mm.summary())

sns.jointplot(x='sqft_living', y='price', data=df, kind='reg', fit_reg=True,
              height=7)
