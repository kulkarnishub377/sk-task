# %% [markdown]
# # Shubham Kulkarni

# %% [markdown]
# #### Linkedin profile:- https://www.linkedin.com/in/kulkarni-shubham-sk/

# %% [markdown]
# ## DATA SCIENCE  AND BUSINESS ANALYTICS INTERN @ THE SPARKS FOUNDATION 

# %% [markdown]
# ### #GRIPJUNE23 #TSF  #DATASCIENCE  

# %% [markdown]
# #### DATASET : SAMPLESUPERSTORE.CSV (https://bit.ly/3i4rbWl)

# %% [markdown]
# ## EXPLORATORY DATA ANALYSIS - RETAIL

# %%
%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %% [markdown]
# ##### Importing the Data form Samplesuperstore

# %%
df=pd.read_csv("F:/SampleSuperstore.csv")
df.head()

# %%
df.info()

# %%
df.isnull().sum()

# %%
df.columns

# %%
print("Total number of columns in file")
df.shape

# %%
df.nunique()

# %% [markdown]
# ## Exploratory Data Analysis

# %%
plt.figure(figsize=(8,5))
sns.kdeplot(df['Sales'],color='red',label='Sales',shade=True,bw=25)
sns.kdeplot(df['Profit'],color='Blue',label='Profit',shade=True,bw=25)
plt.xlim([-100,1000])
plt.legend()

# %% [markdown]
# Profit is more than that of sale but there are some areas where profit could be increased.

# %% [markdown]
# ## Analysis using Pairplot of each column

# %% [markdown]
# ### [1] Based on the Catagory

# %%
sns.pairplot(df,hue='Category')

# %% [markdown]
# ### [2] Based on Region

# %%
sns.pairplot(df,hue='Region')

# %% [markdown]
# ### [3] Based on the segment 

# %%
sns.pairplot(df,hue='Segment')

# %%
df.corr()

# %% [markdown]
# ### Heatmap for Correlation

# %%
sns.heatmap(df.corr(),cmap='rocket_r',annot=True)

# %% [markdown]
# _From above Heatmap:_
# 
# - Sales and Profit are Moderately Correlated.
# - Discount and Profit are Negatively Correlated
# - Quantity and Profit are less Moderately Correlated.

# %% [markdown]
# ## Count plot of each column

# %%
fig,axs=plt.subplots(nrows=2,ncols=2,figsize=(10,7));

sns.countplot(df['Category'],ax=axs[0][0])
sns.countplot(df['Segment'],ax=axs[0][1])
sns.countplot(df['Ship Mode'],ax=axs[1][0])
sns.countplot(df['Region'],ax=axs[1][1])
axs[0][0].set_title('Category',fontsize=20)
axs[0][1].set_title('Segment',fontsize=20)
axs[1][0].set_title('Ship Mode',fontsize=20)
axs[1][1].set_title('Region',fontsize=20)


plt.tight_layout()

# %%
plt.figure(figsize=(20,8))
sns.countplot(df['Sub-Category'])
plt.title('Sub-Category',fontsize=20)

# %%
plt.figure(figsize=(18,5))
sns.countplot(df['State'])
plt.xticks(rotation=90)
plt.title('State',fontsize=20)

# %%
plt.figure(figsize=(18,5))
sns.countplot(df['Quantity'])
plt.title('Quantity',fontsize=20)

# %%
plt.figure(figsize=(18,5))
sns.countplot(df['Discount'])
plt.xticks(rotation=90)
plt.title('Discount',fontsize=20)

# %% [markdown]
# ## Distribution of the data using the plot

# %%
fig, axs = plt.subplots(ncols=2, nrows = 2, figsize = (10,10))
sns.distplot(df['Sales'], color = 'red',  ax = axs[0][0])
sns.distplot(df['Profit'], color = 'green',  ax = axs[0][1])
sns.distplot(df['Quantity'], color = 'orange',  ax = axs[1][0])
sns.distplot(df['Discount'], color = 'blue',  ax = axs[1][1])
axs[0][0].set_title('Sales Distribution', fontsize = 20)
axs[0][1].set_title('Profit Distribution', fontsize = 20)
axs[1][0].set_title('Quantity distribution', fontsize = 20)
axs[1][1].set_title('Discount Distribution', fontsize = 20)
plt.show()

# %% [markdown]
# ## Statewise Deal Analysis

# %%
df['Country'].value_counts()

# %%
df1 = df['State'].value_counts()
df1.head(10)

# %%
df1.plot(kind='bar',figsize=(15,5))
plt.ylabel('Frequency / Number of deals')
plt.xlabel('States')

plt.title('State Wise Dealings', fontsize = 20)
plt.show()

# %% [markdown]
# - **Here is top 3 state where deals are Highest.**
#     1. Califonia
#     2. New York
#     3. Texas
# 
# **Wyoming: Lowest Number of deal**

# %%
df['State'].value_counts().mean()

# %% [markdown]
# **Average number of deal per state is 204.**

# %% [markdown]
# ## City Wise analysis of the dealing 

# %%
df2 = df['City'].value_counts()
df2=df2.head(50)

# %%
df2.plot(kind='bar',figsize=(15,5))
plt.ylabel('Frequency / Number of deals')
plt.xlabel('City')

plt.title('City Wise Dealings', fontsize = 20)
plt.show()

# %% [markdown]
# **Here is top 3 city where deals are Highest.**
#     1. New York City
#     2. Los Angeles
#     3. Philadelphia

# %%
df['City'].value_counts().mean()

# %% [markdown]
# **Average number of deal per city is 19.**

# %% [markdown]
# ## Segment wise analysis of Profit, Discount and sell 

# %%
df['Segment'].value_counts()

# %%
df_segment= df.groupby(['Segment'])[['Sales', 'Discount', 'Profit']].mean()
df_segment

# %%
#1. sales 2. Discount 3. Profit
df_segment.plot.pie(subplots=True, 
                    autopct='%1.1f%%',
                    figsize=(18, 20),
                    startangle=90,     # start angle 90° (Africa)
                    shadow=True,
                    labels = df_segment.index)
plt.title('Segment wise analysis of Sale, Discount, profit')

# %% [markdown]
# **Sales:**
#   - Consumer : 32%
#   - Corporate - 33.5%
#   - Home Office : 34.5%

# %% [markdown]
# **Discount :**
#   - Consumer : 15.8%
#   - Corporate : 15.8%
#   - Home Office : 14.7%

# %% [markdown]
# **Profit :**
# 
#   - Consumer : 15.8%
# 
#   - Corporate : 15.8%
# 
#   - Home Office : 14.7%

# %% [markdown]
# ## Statewise analysis of Profit Discount and sell

# %%
df['State'].value_counts().head(10)

# %%
df_state= df.groupby(['State'])[['Sales', 'Discount', 'Profit']].mean()
df_state.head(10)

# %% [markdown]
# **[1] Statewise Profit Analysis**

# %%
df_state1=df_state.sort_values('Profit')

df_state1[['Profit']].plot(kind = 'bar', figsize = (15,4))
plt.title('State wise Profit Analysis', fontsize = 20)
plt.ylabel('Profit per Sate')
plt.xlabel('States')
plt.show()

# %% [markdown]
# **_RESULT_**
# 
# - **Vermont**: Highest Profit
# 
# - **Ohio**: Lowest Profit

# %% [markdown]
# **[2] Statewise Sale Analysis**

# %%
df_state['Sales'].plot(kind='pie',
                        figsize = (20,20),
                        autopct='%1.1f%%',
                        startangle=90,     # start angle 90° (Africa)
                        shadow=True)
plt.title('State wise analysis of Sale',fontsize=20)

# %% [markdown]
# - Highest amount of sales= **Wyoming(11.8%)**
# - Lowest amount of sales= **South Dakota(0.8%)**

# %% [markdown]
# **[3] Statewise Discount Analysis**

# %%
df_state1['Discount'].plot(kind='bar',figsize=(18,5))
plt.title('State wise analysis of Discount', fontsize=20)

# %% [markdown]
# **Illinois at the top**

# %% [markdown]
# ## Citywise Analysis of the Profit

# %%
df_city= df.groupby(['City'])[['Sales', 'Discount', 'Profit']].mean()
df_city = df_city.sort_values('Profit')
df_city.head()

# %%
#1.Low Profit
df_city['Profit'].head(30).plot(kind='bar',figsize=(15,5),color = 'Pink')
plt.title('City wise analysis of Sale, Discount, profit')

# %%
#2. High Profit
df_city['Profit'].tail(30).plot(kind='bar',figsize=(15,5),color = 'Pink')
plt.title('City wise analysis of Sale, Discount, profit')

# %% [markdown]
# 30 CITIES WHICH HAS PROFIT IN POSITIVE
# 
# 30 CITIES WHICH HAS PROFIT IN NEGATIVE
# 
# THE BALANCE IS PRETTY GOOD HERE!

# %% [markdown]
# ## QUANTITY WISE SALES, PROFIT AND DISCOUNT ANALYSIS

# %%
df_quantity = df.groupby(['Quantity'])[['Sales', 'Discount', 'Profit']].mean()
df_quantity.head(10)

# %%
#1. sales 2. Discount 3. Profit
df_quantity.plot.pie(subplots=True, 
                    autopct='%1.1f%%',
                    figsize=(20, 20),
                     pctdistance=0.69,
                    startangle=90,     # start angle 90° (Africa)
                    shadow=True,
                    labels = df_quantity.index)
plt.title('Quantity wise analysis of Sale, Discount, profit')

# %% [markdown]
# 
# 13 Number of Quantity is high for sales and Profit.

# %% [markdown]
# ## CATAGORY WISE SALES DISCOUNT AND PROFIT 

# %%
df_category = df.groupby(['Category'])[['Sales', 'Discount', 'Profit']].mean()
df_category

# %%
df_category.plot.pie(subplots=True, 
                     figsize=(18, 20), 
                     autopct='%1.1f%%', 
                     labels = df_category.index)

# %% [markdown]
# - Maximun sales and Profit obtain in **Technology.**
# - Minimun profit obtain in **Furniture**

# %% [markdown]
# ## Sub-Category wise Sales, Profit and Discount

# %%
df_sub_category = df.groupby(['Sub-Category'])[['Sales', 'Discount', 'Profit']].mean()
df_sub_category.head(10)

# %% [markdown]
# **[1] BASED ON THE SALES**

# %%

plt.figure(figsize = (15,15))
plt.pie(df_sub_category['Sales'], labels = df_sub_category.index, autopct = '%1.1f%%')
plt.title('Sub-Category Wise Sales Analysis', fontsize = 20)
plt.legend()
plt.xticks(rotation = 90)
plt.show()

# %% [markdown]
# 
# Copier then Machine have High sales.

# %% [markdown]
# **[2] BASED ON THE DISCOUNT**

# %%
plt.figure(figsize = (15,15))
plt.pie(df_sub_category['Discount'], labels = df_sub_category.index, autopct = '%1.1f%%')
plt.title('Sub-Category Wise Discount Analysis', fontsize = 20)
plt.legend()
plt.xticks(rotation = 90)
plt.show()

# %% [markdown]
# **Binders , Machines and then tables have high Discount.**

# %% [markdown]
# **[3] BASED ON THE PROFIT**

# %%
df_sub_category.sort_values('Profit')[['Sales','Profit']].plot(kind='bar',
                                                              figsize= (10,5),
                                                              label=['Avg Sales Price($)','Profit($)'])

# %% [markdown]
# **COPIER : HIGHEST PROFIT AS WELL AS SELL**

# %% [markdown]
# ## REGION WISE ANALYSIS

# %%
df_region = df.groupby(['Region'])[['Sales', 'Discount', 'Profit']].mean()
df_region

# %%
df_region.plot.pie(subplots=True, 
                   figsize=(18, 20), 
                   autopct='%1.1f%%',
                   labels = df_region.index)

# %% [markdown]
# **WEST : PROFIT IS HIGH**

# %% [markdown]
# ## SHIP MODE WISE ANALYSIS

# %%
df['Ship Mode'].value_counts()

# %%
df_shipmode = df.groupby(['Ship Mode'])[['Sales', 'Discount', 'Profit']].mean()

# %%

df_shipmode.plot.pie(subplots=True,
                     figsize=(18, 20), 
                     autopct='%1.1f%%', 
                     labels = df_shipmode.index)

# %% [markdown]
# - Profit and Discount is high in First Class
# - Sales is high for Same day ship

# %% [markdown]
# ## RESULT AND CONCLUSION

# %% [markdown]
# - Profit is more than that of sale but there are some areas where profit could be increased.
# 
# - Profit and Discount is high in First Class
# 
# - Sales is high for Same day ship
# 
# - Sub-category: Copier: High Profit & sales
# 
# - Sub-category: Binders , Machines and then tables have high Discount.
# 
# - Category: Maximun sales and Profit obtain in Technology.
# 
# - Category: Minimun profit obtain in Furniture
# 
# - State: Vermont: Highest Profit
# 
# - State: Ohio: Lowest Profit
# 
# - Segment: Home-office: High Profit & sales
# 
# - Here is top 3 city where deals are Highest.
# 
#     1. New York City
# 
#     2. Los Angeles
# 
#     3. Philadelphia
# 
# - Sales and Profit are Moderately Correlated.
# 
# - Quantity and Profit are less Moderately Correlated.
# 
# - Discount and Profit are Negatively Correlated
# 
# - Here is top 3 state where deals are Highest.
# 
#     1. Califonia
# 
#     2. New York
# 
#     3. Texas
# 
# - **Wyoming** : Lowest Number of deal,Highest amount of sales= Wyoming(11.8%)
# 
# - Lowest amount of sales= **South Dakota(0.8%)**
# 

# %% [markdown]
# **THANK YOU!**


