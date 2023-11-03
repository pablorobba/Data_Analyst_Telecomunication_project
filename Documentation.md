# VENV

Made the virtual enviorment, you can download the requimerents from the requirements.txt

# ETL

We download the files from the API of official [ENACOM webpage](https://datosabiertos.enacom.gob.ar/dashboards/20000/acceso-a-internet/), saved them in csv format to make the EDA. For that, we utilized the requests library and the GET method. For some files (3 of them), we could not get them from the API, so we chose to use the csv download link instead (we still utilized the requests library for that).
We have to do an adjustment since the data was not load properly with the previous method (loading in a csv), we had to get the original xlsx data navigating in the API, so we have to modified the original code: first the load the API links, then convert them in dictionaries, search the link in one of their keys and load the archive in a csv

# EDA

We started with the csv that analyse the access to dial up and narrow band by province and quarter. We found some outliers in the broadband column, were over the 500 value and that most values are between, if you take only the under 400, under 150 too, so majority of the number of access by quarter and province are under that value.
We dont see any outlier in the dial up graphic that we made 