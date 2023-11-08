import pandas as pd
import matplotlib.pyplot as plt

#Load the dataset
dataset = pd.read_excel(
    r"C:\Users\Pablo\Documents\Programacion\4 Henry\D) Proyectos Individiduales\2 - Data Analys\Source_Datasets\internet_penetration.xlsx")

last_year = dataset["Año"].max() #took the last year
previous_quarter = dataset["Trimestre"].max() - 1 #took the previous quarter

if previous_quarter == 0:       #if the quarter equals 1, it will subtract 1, so it will be 0. 
    previous_quarter = 4        #Since 1 is the first quarter, we went to the fourth to 
    last_year = last_year - 1   #the previous year(since it's the previous quarter)
last_year = dataset["Año"].max()
previous_quarter = dataset["Trimestre"].max() - 1
last_quarter = dataset["Trimestre"].max()
if previous_quarter == 1:
    previous_quarter = 4
    last_year = last_year - 1

#we make the filters
mask_goal = (dataset ["Año"] == last_year) | (dataset["Trimestre"] == previous_quarter)
df_goal = dataset[mask_goal]
mask_actual = (dataset ["Año"] == last_year) | (dataset["Trimestre"] == last_quarter)
df_actual = dataset[mask_actual] 
       
goal = df_goal["Accesos por cada 100 hab"].sum() * 1.02     #we calculate the 2 % of the access per capita (our goal in our KPI)
actual = df_actual["Accesos por cada 100 hab"].sum()        #the actual value
KPI = ((goal - actual)/actual) * 100                        #the KPI formula

categories = ["Goal", "Actual"]
values = [goal, actual]

#we create the graphic for the KPI
fig, ax = plt.subplots(figsize=(4, 2))
if KPI < 2:
    ax.bar(("Actual"), actual, color=['lightcoral'], width = 0.5)
    ax.axhline(y=goal, color='black', linestyle='--', label='Objetivo')
    ax.set_ylabel('Valor')
    ax.set_title(f'KPI: {KPI} %', color='red')


    plt.show()
else:
    ax.bar(("Actual"), actual, color=['mediumspringgreen'], width = 0.5)
    ax.set_ylabel('Valor')
    ax.set_title(f'KPI: {KPI} %', color='green')


    plt.show()