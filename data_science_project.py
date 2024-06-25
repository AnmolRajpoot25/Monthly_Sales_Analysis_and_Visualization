import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


#Merge the 12 months of sales data into a single CSV file
df= pd.read_csv(r"C:\CODING FOLDER\coding files of python\Pythoncode\jovian\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data\Sales_April_2019.csv")
files= [file for file in os.listdir(r"C:\CODING FOLDER\coding files of python\Pythoncode\jovian\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data")]
p= df.head()
print(p)
all_months_data= pd.DataFrame()
for file in files:
    print(file)
    df =pd.read_csv("C:\CODING FOLDER\coding files of python\Pythoncode\jovian\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data"+"\\" + file)
    all_months_data=pd.concat([all_months_data,df])
    k=all_months_data.head()
    print(k)
all_months_data.to_csv(r"C:\CODING FOLDER\coding files of python\pythoncode\jovian\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data\all_months_data.csv", index=False)
    
all_data=pd.read_csv(r"C:\CODING FOLDER\coding files of python\Pythoncode\jovian\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data\all_months_data.csv")
w=all_data.head()
print(w,all_data)
print(all_data.head())

# clean up the data
#drop rows of NAN
all_data.dropna(how='all'  , inplace=True)

nan_df= all_data[all_data.isna().any(axis=1)]
nan_df.head()
# inplace=true is for the permanent drop of the row 

print(nan_df)

##  find "or"  and delete it 
all_data=all_data[all_data['Order Date'].str[0:2]!='Or']

# Ensure 'Quantity Ordered' and 'Price Each' columns exist

if 'Quantity Ordered' not in all_data.columns or 'Price Each' not in all_data.columns:
    raise KeyError("Missing required columns 'Quantity Ordered' or 'Price Each' in the data.")


## convert the data to the correct type 
all_data['Quantity Ordered']=pd.to_numeric(all_data['Quantity Ordered'],errors='coerce')# make int
all_data['Price Each']=pd.to_numeric(all_data['Price Each'],errors='coerce')#make float
all_data.head()
all_data.dropna(subset=['Quantity Ordered', 'Price Each'], inplace=True)

## augment data with additional columns
##task2 add month column

all_data['Month']=all_data['Order Date'].str[0:2]
all_data['Month']=all_data['Month'].astype('int32')

print(all_data.head())


##what was the best months for sales? how much was earned that month?
# add a sales column
all_data['Sales']=all_data['Quantity Ordered']*all_data['Price Each']
tt=all_data.head()
print(tt)

## add a city columns
#let us use .apply()
def get_city(address):
    return address.split(',')[1]
def get_state(address):
    return address.split(',')[2].split(' ')[1]
    
all_data['City']=all_data['Purchase Address'].apply(lambda x: f"{get_city(x)} ({get_state(x)})")

print(all_data.head())
#what was the best month for sales? how much was earned that month ?
results=all_data.groupby('Month').sum().reindex(range(3, 6), fill_value=0)
print(results)

months=range(3,6)
plt.bar(months,results['Sales'])
plt.xticks(months)
plt.ylabel('sales in USD $')
plt.xlabel('month in number ')
plt.show()
## what city had the highest number of sales
results =all_data.groupby('City').sum()
print(results)
cities=all_data['City'].unique()

plt.bar(cities,results['Sales'])
plt.xticks(cities , rotation='vertical',size=8)
plt.ylabel('sales in USD $')
plt.xlabel('City ')
plt.show()

#task 3 

all_data['Order Date']=pd.to_datetime(all_data['Order Date'])
all_data['Hours']=all_data['Order Date'].dt.hour
all_data['minute']=all_data['Order Date'].dt.minute
all_data['count']=1
print(all_data.head())


hours=[hour for hour,df in all_data.groupby('Hours')]
plt.plot(hours,all_data.groupby(['Hours']).count())
plt.xticks(hours)
plt.xlabel('Hour')
plt.ylabel('numbers of orders ')
plt.grid()
plt.show()

#what products are most often sold together 
df =all_data[all_data['Order ID'].duplicated(keep=False)]
ll=df.head(20)
print(ll)

df['grouped']=df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
df=df[['Order ID','grouped']].drop_duplicates()

print(df.head(100))

from itertools import combinations
from collections import Counter 


count=Counter()
for row  in df['grouped']:
    row_list=row.split(',')
    count.update(Counter(combinations(row_list,2)))
    print(count)
    
for key, value in count.most_common(10):
    print(key,value)
    
    
    ### what Product sold most ?why do you think it sold the most ?
product_group=all_data.groupby('Product')
quantity_Ordered=product_group.sum()['Quantity Ordered'] 
products =[product for product, df in product_group]
plt.bar(products, quantity_Ordered) 
plt.xticks(products,rotation= 'vertical' ,size=8)
plt.show()
prices=all_data.groupby('Product').mean()["Price Each"]
print(prices)

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.bar(products,quantity_Ordered,color='g')
ax2.plot(products, prices,'b-')
ax1.set_xlabel('Product Name')
ax1.set_ylabel('Quantity Ordered',color='b')
ax1.set_xticklabels(products, rotation='vertical', size=9)
plt.show()
