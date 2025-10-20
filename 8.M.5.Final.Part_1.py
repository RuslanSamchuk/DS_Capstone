''''
Create visualizations using Matplotib, Seaborn and Folium
Estimated time needed: 40 minutes

In this assignment, you will have the opportunity to demonstrate the skills you have acquired in creating visualizations using Matplotlib, Seaborn, Folium.

After each task you will be required to save your plots as an image or screenshot using the filenames specified. You will be uploading these images during your final project submission so they can be evaluated by your peers.

Table of Contents
Objectives
Setup
Installing Required Libraries
Importing Required Libraries
Scenario
Data Description
Importing data
Creating Visualizations for Data Analysis
Objectives
After completing this lab you will be able to:

Create informative and visually appealing plots with Matplotlib and Seaborn.
Apply visualization to communicate insights from the data.
Analyze data through using visualizations.
Customize visualizations
Setup
For this lab, we will be using the following libraries:

pandas for managing the data.
numpy for mathematical operations.
matplotlib for plotting.
seaborn for plotting.
Folium for plotting.
'''
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import folium

pd.set_option('display.max_columns', None)  # show all columns
pd.set_option('display.width', 400)         # adjust width to your console size
pd.set_option('display.max_colwidth', None)  # Show full content of each column
pd.set_option('display.max_rows', None)

''''
Scenario
In this assignment you will be tasked with creating plots which answer questions for analysing "historical_automobile_sales" data to understand the historical trends in automobile sales during recession periods.
recession period 1 - year 1980
recession period 2 - year 1981 to 1982
recession period 3 - year 1991
recession period 4 - year 2000 to 2001
recession period 5 - year end 2007 to mid 2009
recession period 6 - year 2020 -Feb to April (Covid-19 Impact)

Data Description
The dataset used for this visualization assignment contains historical_automobile_sales data representing automobile sales and related variables during recession and non-recession period.

The dataset includes the following variables:
1. Date: The date of the observation.
2. Recession: A binary variable indicating recession perion; 1 means it was recession, 0 means it was normal.
3. Automobile_Sales: The number of vehicles sold during the period.
4. GDP: The per capita GDP value in USD.
5. Unemployment_Rate: The monthly unemployment rate.
6. Consumer_Confidence: A synthetic index representing consumer confidence, which can impact consumer spending and automobile purchases.
7. Seasonality_Weight: The weight representing the seasonality effect on automobile sales during the period.
8. Price: The average vehicle price during the period.
9. Advertising_Expenditure: The advertising expenditure of the company.
10.Vehicle_Type: The type of vehicles sold; Supperminicar, Smallfamiliycar, Mediumfamilycar, Executivecar, Sports.
11.Competition: The measure of competition in the market, such as the number of competitors or market share of major manufacturers.
12.Month: Month of the observation extracted from Date..
13.Year: Year of the observation extracted from Date.
By examining various factors mentioned above from the dataset, you aim to gain insights into how recessions impacted automobile sales for your company.

Importing Data
'''
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"
df = pd.read_csv(URL)
print('Data read into a pandas dataframe!')
print(df.head())
print(df.describe())
print(df.columns)
''''
Creating Visualizations for Data Analysis
TASK 1.1: Develop a Line chart using the functionality of pandas to show how automobile sales fluctuate from year to year
Include the following on the plot
ticks on x- axis with all the years, to identify the years of recession
annotation for at least two years of recession
Title as Automobile Sales during Recession
'''
df2 = df.groupby('Year')['Automobile_Sales'].mean()
plt.figure(figsize=(10, 6))
df2.plot(x=df2.index, y=df2.values, kind='line')
years = list(range(1980,2024))
plt.xticks(rotation=90, fontsize=8,  ticks=years, labels=years)
plt.xlabel('Year')
plt.ylabel('The number of vehicles sold during the period')
plt.title('How automobile sales fluctuate from year to year')
plt.text(1982.3, 650, '1981-82 Recession')
plt.text(1991.3, 650, '1990-91 Recession')
plt.legend()
plt.grid(alpha=0.3)
#plt.show()
plt.close()
''''
TASK 1.2: Plot different lines for categories of vehicle type and analyse the trend to answer the question Is there a noticeable difference in 
sales trends between different vehicle types during recession periods?
'''
Vehicle_Types = df[df['Recession'] == 1]
#Vehicle_Types = df
# Calculate the average automobile sales by year and vehicle type during the recession
Vehicle_Types2 = Vehicle_Types.groupby(['Year','Vehicle_Type'], as_index=False)['Automobile_Sales'].mean()
#Calculate the normalized sales by dividing by the average sales for each vehicle type
Vehicle_Types2['Normalized_Sales'] = Vehicle_Types2.groupby('Vehicle_Type')['Automobile_Sales'].transform(lambda x: x / x.mean())
# Set the 'Year' as the index
Vehicle_Types2.set_index('Year', inplace=True)

# Create the plot for each vehicle type
plt.figure(figsize=(12, 8))
for vehicle_type in Vehicle_Types2['Vehicle_Type'].unique():
    data = Vehicle_Types2[Vehicle_Types2['Vehicle_Type'] == vehicle_type]
    #plt.plot(data.index, data['Normalized_Sales'], label=vehicle_type, marker='o')
    plt.plot(data.index, data['Normalized_Sales'],marker='o', linewidth=2, label=vehicle_type)

# Highlight recession years
recession_years = Vehicle_Types['Year'].unique()
for year in recession_years:
    plt.axvline(x=year, color='gray', linestyle='--', alpha=0.5)

# Add labels, legend, and title
plt.legend(title="Vehicle Type", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.ylabel("Normalized Sales")
plt.xlabel("Year")
plt.title("Normalized Automobile Sales by Vehicle Type During Recession")
plt.grid(alpha=0.3)
plt.tight_layout()
#plt.show()
plt.close()
''''
Inference: Sports cars and supermini cars demonstrate resilience or growth during recession periods.Medium family cars and, to a lesser extent, small family cars show more sensitivity to economic changes, with less consistent trends.
The upward trend in sports vehicles sales indicates the stability of the luxury market, even during economic downturns.
'''
''''
TASK 1.3: Use the functionality of Seaborn Library to create a visualization to compare the sales trend per vehicle type for a recession period with a non-recession period.
'''
new_df = df.groupby('Recession')['Automobile_Sales'].mean().reset_index()

# Create the bar chart using seaborn
plt.figure(figsize=(10, 6))
sns.barplot(x='Recession', y='Automobile_Sales', hue='Recession',  data=new_df, palette='Set2')
plt.xlabel('Economic Condition')
plt.ylabel('Average Automobile Sales')
plt.title('Average Automobile Sales during Recession and Non-Recession')
plt.xticks(ticks=[0, 1], labels=['Non-Recession', 'Recession'])
#plt.show()
plt.close()
''''
Now you want to compare the sales of different vehicle types during a recession and a non-recession period
We recommend that you use the functionality of Seaborn Library to create this visualization
'''
grouped_df = df.groupby(['Recession','Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
#print(grouped_df.head())
# Create the grouped bar chart using seaborn
plt.figure(figsize=(12, 7))
sns.barplot(x='Recession', y='Automobile_Sales', hue='Vehicle_Type', data=grouped_df, palette='tab10')
plt.xticks(ticks=[0, 1], labels=['Non-Recession', 'Recession'])
plt.xlabel('Economic Condition')
plt.ylabel('Average Automobile Sales')
plt.title('Vehicle-Wise Sales during Recession and Non-Recession Period')
plt.legend(title='Vehicle Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
#plt.show()
plt.close()
#Inference: all types of cars sales are drop during recession, the most are sport and executive
''''
TASK 1.4: Use sub plotting to compare the variations in GDP during recession and non-recession period by developing 
line plots for each period.
Now, you want to find more insights from the data to understand the reason.
Plot a two line charts using subplotting to answer:-
How did the GDP vary over time during recession and non-recession periods?
Make use of add_subplot() from Matplotlib for this comparision.
'''
#grouped_df = df.groupby(['Recession','Vehicle_Type'])['Automobile_Sales'].mean().reset_index()


df_rec = df.groupby(['Recession','Year'])['GDP'].mean().reset_index()
# Split datasets
rec_data = df_rec[df_rec['Recession'] == 1]
non_rec_data = df_rec[df_rec['Recession'] == 0]

fig = plt.figure(figsize=(8, 4))
# Add the first subplot (top-left)
axs1 = fig.add_subplot(1, 2, 1)
# Plotting in first axes - the left one
#data1 = df_rec[df_rec['Recession'] == 0]
sns.lineplot(x='Year', y='GDP', data=non_rec_data, color='seagreen')
plt.title('Non-Recession')
plt.xlabel('Year')
plt.ylabel('GDP')
# Add the second subplot (top-right)
axs2 = fig.add_subplot(1, 2, 2)
# Plotting in second axes - the right one
sns.lineplot(x='Year', y='GDP', data=rec_data, color='firebrick')
plt.title('Recession')
plt.xlabel('Year')
plt.ylabel('GDP')
# Adding a Title for the Overall Figure
plt.suptitle('GDP Variation During Recession vs Non-Recession', fontsize=14)
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Show the figure
#plt.show()
plt.close()

rec_data = df[df['Recession'] == 1]
non_rec_data = df[df['Recession'] == 0]

# Figure
fig = plt.figure(figsize=(12, 6))

# Create different axes for subploting
ax1 = fig.add_subplot(1, 2, 1)  # add subplot 1 (1 row, 2 columns, first plot)
ax2 = fig.add_subplot(1, 2, 2)  # add subplot 2 (1 row, 2 columns, second plot).

# Left plot — Non-recession
sns.lineplot(x='Year', y='GDP', data=non_rec_data, ax=ax1, color='seagreen')
ax1.set_title('GDP Variation During Non-Recession Period')
ax1.set_xlabel('Year')
ax1.set_ylabel('GDP')
ax1.grid(True)

# Right plot — Recession
sns.lineplot(x='Year', y='GDP', data=rec_data, ax=ax2, color='firebrick')
ax2.set_title('GDP Variation During Recession Period')
ax2.set_xlabel('Year')
ax2.set_ylabel('GDP')
ax2.grid(True)

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.95])
fig.suptitle('Comparison of GDP During Recession and Non-Recession Periods', fontsize=14)

#plt.show()
plt.close()
#Inference
#From this plot, it is evident that during recession, the GDP of the country was in a low range, might have afected the overall sales of the company
''''
TASK 1.5: Develop a Bubble plot for displaying the impact of seasonality on Automobile Sales.
How has seasonality impacted the sales, in which months the sales were high or low? Check it for non-recession years 
to understand the trend
Develop a Bubble plot for displaying Automobile Sales for every month and use Seasonality Weight for representing 
the size of each bubble
Title this plot as 'Seasonality impact on Automobile Sales'
'''
non_rec_data = df[df['Recession'] == 0]
size = non_rec_data['Seasonality_Weight']

sns.scatterplot(
    data=non_rec_data,
    x='Month',
    y='Automobile_Sales',
    size=size,
    hue='Seasonality_Weight',
    sizes=(50, 500),
    #palette='viridis',
    #alpha=0.7,
    #edgecolor='gray',
    legend=False
)

plt.xlabel('Month')
plt.ylabel('Automobile Sales')
plt.title('Seasonality impact on Automobile Sales')
#plt.tight_layout(rect=[0, 0, 1, 0.95])
#plt.show()
plt.close()
''''
TASK 1.6: Use the functionality of Matplotlib to develop a scatter plot to identify the correlation between average 
vehicle price relate to the sales volume during recessions.
From the data, develop a scatter plot to identify if there a correlation between consumer confidence and automobile 
sales during recession period?
Title this plot as 'Consumer Confidence and Automobile Sales during Recessions'
'''
rec_data = df[df['Recession'] == 1]
plt.scatter(rec_data['Consumer_Confidence'], rec_data['Automobile_Sales'], color='seagreen')
plt.xlabel('Consumer_Confidence')
plt.ylabel('Automobile Sales')
plt.title('Consumer Confidence and Automobile Sales during Recessions')
#plt.show()
plt.close()
#How does the average vehicle price relate to the sales volume during recessions?
#Plot another scatter plot and title it as 'Relationship between Average Vehicle Price and Sales during Recessions'
plt.scatter(rec_data['Price'], rec_data['Automobile_Sales'], color='seagreen')
plt.xlabel('Price')
plt.ylabel('Automobile Sales')
plt.title('Relationship between Average Vehicle Price and Sales during Recessions')
#plt.show()
plt.close()
''''
TASK 1.7: Create a pie chart to display the portion of advertising expenditure of XYZAutomotives during recession and non-recession periods.
How did the advertising expenditure of XYZAutomotives change during recession and non-recession periods?
'''
# Filter the data
Rdata = df[df['Recession'] == 1]
NRdata = df[df['Recession'] == 0]

# Calculate the total advertising expenditure for both periods
RAtotal = Rdata['Advertising_Expenditure'].sum()
NRAtotal = NRdata['Advertising_Expenditure'].sum()

# Create a pie chart for the advertising expenditure
plt.figure(figsize=(8, 6))

labels = ['Recession', 'Non-Recession']
sizes = [RAtotal, NRAtotal]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

plt.title('Portion of advertising expenditure of XYZAutomotives during recession and non-recession periods')
#plt.show()
plt.close()
#Inference
#It seems XYZAutomotives has been spending much more on the advertisements during non-recession periods as compared to during recession times. Fair enough!
''''
TASK 1.8: Develop a pie chart to display the total Advertisement expenditure for each vehicle type during recession period.
Can we observe the share of each vehicle type in total expenditure during recessions?
'''
# Filter the data
Rdata = df[df['Recession'] == 1]

df3 = Rdata.groupby('Vehicle_Type')['Advertising_Expenditure'].sum()

# Create a pie chart for the advertising expenditure
plt.figure(figsize=(8, 6))

labels = df3.index
sizes = df3.values
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

plt.title('Share of Each Vehicle Type in Total Expenditure during Recessions')
#plt.show()
plt.close()
#Inference
#During recession the advertisements were mostly focued on low price range vehicle. A wise decision!
''''
TASK 1.9: Develop a lineplot to analyse the effect of the unemployment rate on vehicle type and sales during the Recession Period.
Analyze the effect of the unemployment rate on vehicle type and sales during the Recession Period
You can create a lineplot and title the plot as 'Effect of Unemployment Rate on Vehicle Type and Sales'
'''
df_rec = df[df['Recession']==1]
#print(df_rec.head())
#df_rec = df_rec.sort_values(by=['Vehicle_Type', 'Unemployment_Rate'])
plt.xlim(df_rec['unemployment_rate'].min(), df_rec['unemployment_rate'].max())
sns.lineplot(data=df_rec, x='unemployment_rate', y='Automobile_Sales',
             hue='Vehicle_Type', style='Vehicle_Type', markers=True, err_style=None)
plt.ylim(0,850)
plt.legend(loc=(0.05,.3))
#plt.legend(title='Vehicle Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xlabel('Unemployment Rate (%)')
plt.ylabel('Automobile Sales')
plt.title('Effect of Unemployment Rate on Vehicle Type and Sales')
#plt.show()
plt.close()
''''
OPTIONAL : TASK 1.10 Create a map on the hightest sales region/offices of the company during recession period
'''
import requests, webbrowser

# URL to download
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/us-states.json"

# Filename to save as
filename = "us-states.json"

# Download the file
response = requests.get(url)
if response.status_code == 200:
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"✅ File downloaded successfully: {filename}")
else:
    print(f"❌ Failed to download file. Status code: {response.status_code}")

# Filter the data for the recession period and specific cities
recession_data = df[df['Recession'] == 1]

print(recession_data['City'].unique())
    # Calculate the total sales by city
sales_by_city = recession_data.groupby('City')['Automobile_Sales'].sum().reset_index()

    # Create a base map centered on the United States
map_auto = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

    # Create a choropleth layer using Folium
choropleth = folium.Choropleth(
    geo_data= 'us-states.json',  # GeoJSON file with state boundaries
    data=sales_by_city,
    columns=['City', 'Automobile_Sales'],
    key_on='feature.properties.name',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Automobile Sales during Recession'
).add_to(map_auto)


    # Add tooltips to the choropleth layer
choropleth.geojson.add_child(
    folium.features.GeoJsonTooltip(['name'], labels=True)
)

    # Display the map
map_path = "auto_sales_map.html"
map_auto.save(map_path)
webbrowser.open(map_path)
