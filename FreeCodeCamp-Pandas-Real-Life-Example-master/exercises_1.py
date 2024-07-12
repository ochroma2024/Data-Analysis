import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv('data/sales_data.csv',parse_dates=['Date'])

# print(sales.head())
# print(f"{sales.info()}")
print(f"{sales['Customer_Age'].describe()}")

# print(f"{float(sales['Customer_Age'].mean()):.2f}")

# sales['Customer_Age'].plot(kind='kde',figsize=(14,6))
# plt.title('Kernel Density Estimate of Customer Age')
# plt.xlabel('Age')
# plt.ylabel('Density')
# plt.show()

# sales['Customer_Age'].plot(kind='box',vert=False,figsize=(14,6))
# plt.title('Box Plot of Customer Age')
# plt.xlabel('Age')
# plt.show()

