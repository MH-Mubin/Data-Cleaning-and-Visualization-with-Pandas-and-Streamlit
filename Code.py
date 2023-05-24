import pandas as pd 
import matplotlib.pyplot as plt
import streamlit as st


read_file = pd.read_csv (r"C:\Users\DELL\Desktop\Pro\dataset.txt", sep=' ')
read_file.to_csv (r"C:\Users\DELL\Desktop\Pro\dataset.csv", index=None)

data = pd.read_csv(r"C:\Users\DELL\Desktop\Pro\dataset.csv")

count_col = data.shape[0]

data = data[data.Province_State != '0']
count = count_col - data.shape[0]
print(f'Number of rows dropped: {count}')

count_null = (data['Deaths'].isnull().sum()) + (data['Confirmed'].isnull().sum())
print(f'Number of rows with null value: {count_null}')
data['Deaths'] = data['Deaths'].fillna(0)
data['Confirmed'] = data['Confirmed'].fillna(0)

data.to_csv(r"C:\Users\DELL\Desktop\Pro\dataset_new.csv", index=False)

data.dtypes

plt.hist([data['Deaths'], data['Confirmed']],  color=['blue', 'red'], label = ['Deaths', 'Confirmed'], density='True')
plt.legend()
plt.title('Death and Confirmed Histogram')

data.rename(columns={'Province_State': 'Province_State/object', 'Country_Region' : 'Country_Region/object', 'Lat' : 'Lat/float64', 'Long' : 'Long/float64', 'Date' : 'Date/object', 'Confirmed' : 'Confirmed/float64', 'Deaths' : 'Deaths/float64'}, inplace=True)
data.to_csv(r"C:\Users\DELL\Desktop\Pro\dataset_new.csv", index=False)

data_map = pd.read_csv(r"C:\Users\DELL\Desktop\Pro\dataset_new.csv")
data_map.rename(columns={'Lat': 'lat', 'Long' : 'lon' }, inplace=True)
st.map(data_map)
