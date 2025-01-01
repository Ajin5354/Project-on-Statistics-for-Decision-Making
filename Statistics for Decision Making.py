#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
from scipy.stats import ttest_1samp, ttest_ind
from math import factorial  # To calculate binomial coefficient manually

# Helper function for binomial coefficient
def comb(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


# In[21]:


p1=pd.read_csv(r"C:\Users\LENOVO\Downloads\property.csv")


# In[22]:


p1


# In[23]:


# Convert 'Date' column to datetime format for filtering
p1['Date'] = pd.to_datetime(p1['Date'], format='%d/%m/%Y')


# In[24]:


# Task 1: Test if typical property price in Altona is $800,000
altona_prices = p1.loc[p1['Suburb'] == 'Altona', 'Price']
hypothesized_mean = 800000


# In[25]:


# Perform a one-sample t-test
t_stat, p_value = ttest_1samp(altona_prices.dropna(), hypothesized_mean)

print(f"Task 1 - Altona Property Price Test:")
print(f"T-Statistic: {t_stat:.4f}, P-Value: {p_value:.4f}")
if p_value < 0.05:
    print("Conclusion: The typical property price in Altona is significantly different from $800,000.")
else:
    print("Conclusion: No significant evidence that the property price differs from $800,000.")


# In[26]:


# Task 2: Compare prices in summer vs winter months for 2016
# Filter data for 2016
p1_2016 = p1[p1['Date'].dt.year == 2016]


# In[27]:


# Define summer (April-September) and winter (October-March) months
summer_months = [4, 5, 6, 7, 8, 9]
winter_months = [10, 11, 12, 1, 2, 3]


# In[28]:


# Separate prices for summer and winter months
summer_prices = p1_2016[p1_2016['Date'].dt.month.isin(summer_months)]['Price']
winter_prices = p1_2016[p1_2016['Date'].dt.month.isin(winter_months)]['Price']


# In[29]:


# Perform an independent t-test
t_stat_season, p_value_season = ttest_ind(summer_prices.dropna(), winter_prices.dropna(), equal_var=False)

print(f"\nTask 2 - Summer vs Winter Prices (2016):")
print(f"T-Statistic: {t_stat_season:.4f}, P-Value: {p_value_season:.4f}")
if p_value_season < 0.05:
    print("Conclusion: There is a significant difference in property prices between summer and winter months.")
else:
    print("Conclusion: No significant difference in property prices between summer and winter months.")


# In[30]:


# Task 3: Probability of 3 properties out of 10 without car parking in Abbotsford
abbotsford_data = p1[p1['Suburb'] == 'Abbotsford']
p_without_parking = abbotsford_data['Car'].isna().sum() / len(abbotsford_data)
n = 10
k = 3
probability_task3 = comb(n, k) * (p_without_parking ** k) * ((1 - p_without_parking) ** (n - k))

print(f"\nTask 3 - Probability of 3 properties out of 10 without car parking in Abbotsford:")
print(f"Probability: {probability_task3:.3f}")


# In[31]:


# Task 4: Probability of finding a property with 3 rooms in Abbotsford
p_with_3_rooms = abbotsford_data[abbotsford_data['Rooms'] == 3].shape[0] / len(abbotsford_data)
print(f"\nTask 4 - Probability of finding a property with 3 rooms in Abbotsford:")
print(f"Probability: {p_with_3_rooms:.3f}")


# In[32]:


# Task 5: Probability of finding a property with 2 bathrooms in Abbotsford
p_with_2_bathrooms = abbotsford_data[abbotsford_data['Bathroom'] == 2].shape[0] / len(abbotsford_data)
print(f"\nTask 5 - Probability of finding a property with 2 bathrooms in Abbotsford:")
print(f"Probability: {p_with_2_bathrooms:.3f}")


# In[ ]:


### Objective:
Test the assumption that the typical property price in Altona is $800,000 using a one-sample t-test.

#### Hypotheses:
- Null Hypothesis (\(H_0\)): The mean property price in Altona is $800,000.
- Alternative Hypothesis (\(H_1\)): The mean property price in Altona is greater than $800,000.

#### Methodology:
- Significance Level (\(α\)): 5% (0.05).
- Test: One-Sample t-Test.


# In[1]:


import pandas as pd
from scipy.stats import ttest_1samp

# Load the dataset
p1 = pd.read_csv(r"C:\Users\LENOVO\Downloads\property.csv")

# Task 1: Test if typical property price in Altona is $800,000
altona_prices = p1.loc[p1['Suburb'] == 'Altona', 'Price']
hypothesized_mean = 800000

# Perform a one-sample t-test
t_stat, p_value = ttest_1samp(altona_prices.dropna(), hypothesized_mean)

# Results
print(f"T-Statistic: {t_stat:.4f}")
print(f"P-Value: {p_value:.4f}")

if p_value < 0.05:
    print("Conclusion: The typical property price in Altona is significantly different from $800,000.")
else:
    print("Conclusion: No significant evidence that the property price differs from $800,000.")


# Analysis:
# •	The dataset is filtered to extract property prices for the suburb of "Altona."
# •	A one-sample t-test is performed to compare the sample mean against the hypothesized value of $800,000.
# Hypotheses:
# •	Null Hypothesis (Θ0): The mean property price is $800,000.
# •	Alternative Hypothesis (Θ1): The mean property price is not $800,000.
# Results:
# •	T-Statistic: 1.0277
# •	P-Value: 0.3075
# Conclusion: Since the p-value (0.3075) is greater than the significance level (α = 0.05), there is no significant evidence to reject the null hypothesis. This suggests that the typical property price in Altona is not significantly different from $800,000.
# 

# In[2]:


import pandas as pd
from scipy.stats import ttest_ind

# Load the dataset
p1 = pd.read_csv(r"C:\Users\LENOVO\Downloads\property.csv")
p1['Date'] = pd.to_datetime(p1['Date'], format='%d/%m/%Y')

# Task 2: Compare prices in summer vs winter months for 2016
p1_2016 = p1[p1['Date'].dt.year == 2016]

# Define summer (April-September) and winter (October-March) months
summer_months = [4, 5, 6, 7, 8, 9]
winter_months = [10, 11, 12, 1, 2, 3]

# Separate prices for summer and winter months
summer_prices = p1_2016[p1_2016['Date'].dt.month.isin(summer_months)]['Price']
winter_prices = p1_2016[p1_2016['Date'].dt.month.isin(winter_months)]['Price']

# Perform an independent t-test
t_stat_season, p_value_season = ttest_ind(summer_prices.dropna(), winter_prices.dropna(), equal_var=False)

# Results
print(f"T-Statistic: {t_stat_season:.4f}")
print(f"P-Value: {p_value_season:.4f}")

if p_value_season < 0.05:
    print("Conclusion: There is a significant difference in property prices between summer and winter months.")
else:
    print("Conclusion: No significant difference in property prices between summer and winter months.")


# Analysis:
# 
# The dataset is filtered for properties sold in 2016.
# 
# Months are categorized into two groups: summer (April–September) and winter (October–March).
# 
# Property prices for each group are compared using an independent t-test.
# 
# Hypotheses:
# 
# Null Hypothesis (Θ0): There is no difference in the mean property prices between summer and winter.
# 
# Alternative Hypothesis (Θ1): There is a significant difference in the mean property prices between summer and winter.
# 
# Results:
# 
# T-Statistic: -3.9211
# 
# P-Value: 0.0001
# 
# Conclusion:
# Since the p-value (0.0001) is less than the significance level (α = 0.05), the null hypothesis is rejected. This indicates that there is a significant difference in property prices between summer and winter months in 2016.

# In[ ]:




