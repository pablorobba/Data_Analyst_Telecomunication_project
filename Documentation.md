# VENV

Made the virtual enviorment, you can download the requimerents from the requirements.txt

# ETL

We download the files from the API of official [ENACOM webpage](https://datosabiertos.enacom.gob.ar/dashboards/20000/acceso-a-internet/), saved them in csv format to make the EDA. For that, we utilized the requests library and the GET method. For some files (3 of them), we could not get them from the API, so we chose to use the csv download link instead (we still utilized the requests library for that).

***

We discovered that the data was loaded from the main page in csv format had round values and this was not properly aclared in the main page. We had to get the original source xlsx data navigating in the API to discorver which number unit format was every data and check if everything is correct. To the process we made this: first the load the API links, then convert them in dictionaries, search the link in one of their keys and load the archive in a xlsx

# EDA

We started with the csv that analyse the access to dial up and narrow band by province and quarter. We found some outliers in the broadband column, were over the 500 value and that most values are between, if you take only the under 400, under 150 too, so majority of the number of access by quarter and province are under that value.
After that, we realize during this EDA that the values of this datasets were rounded and processed, so we decided to mainly use the source xlsx instead of the frontpage datasets. Some of then are more completed in the source dataset, others were a simple product of the source, others are better shaped in the original datasets. We will leave the csv derived dataframes only if their are needed to analyse something in particular.
A big difference is seen between 4 provinces (mostly 2 of them) and the rest. To discovered that we had to do some trasnformations (which are precised in the Notebook) and made some graphics metrics (bar, scatters). Since the diference is very big with the provinces and that has a direct impact on the localities (towns), we decided to focus our analysis on the provinces (We will develop the KPI's in order to search the way to match the less less favored provinces with the most favored one). The evolution in time, in terms of total conections is great (we did a line graphic to show that).