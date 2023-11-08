<p align='center'>
<img src ="https://tynmagazine.com/wp-content/uploads/sites/3/2020/01/mundo-conectado.jpg">
<p>

<h1 align='center'>
 <b>PROYECT Nº2</b>
</h1>
 
# <h1 align="center">**`Telecommunications proyect`**</h1>

Telecommunication refers to the transmission of information, such as voice, data, or video, over long distances using various technologies and systems. It involves the exchange of signals or messages between individuals or devices, typically through the use of electronic or digital means, to facilitate communication and the sharing of information across geographical locations.

The internet is a global network of interconnected computers and devices that allows users to access and share information, communicate, and perform various online activities. It facilitates the exchange of data and services across the world through a system of protocols and technologies, including the World Wide Web, email, and online applications.

We are asked, on this work, to do an analysis to the data of [Argentina bringed by the ENACOM](https://datosabiertos.enacom.gob.ar/dashboards/20000/acceso-a-internet/).

On this README we are doing a general overview of what we worked all along but for a more detailed description of what we worked, we recommend to watch the [Documentation](https://github.com/pablorobba/Data_Analyst_Telecomunication_proyect/blob/main/Documentation.md).


## ETL

The ETL was short, since data was mostly processed, but with a big problem: since the data was processed, some of the tables had their numbers rounded and with units that were not clear (You can see this very clear [on this dataset](https://datosabiertos.enacom.gob.ar/dataviews/240976/total-nacional-de-accesos-a-internet-fijo-por-banda-ancha-y-banda-angosta/) were some units are in millions and others in thousands, so the sum of thems, on first sight, dont makes sense) and we realized this on the EDA. To solve this, we accessed the source datasets in the ENACOM's API. There, the units were not rounded and this allowed us to do a more quality analysis. 

[ETL notebook](https://github.com/pablorobba/Data_Analyst_Telecomunication_proyect/blob/main/1%20-%20ETL.ipynb)


## EDA

We started the EDA with the frontpage datasets, but sooner than later we discovered the problem that we described  in the former section. We decided to use mostly the source material, but sometimes we used the processed ones. In general terms, and since the EDA is very long, we can summarise it in: We found that there a are a lot of differences in Argentina between provinces and that has an impact on towns (called localities here) and the outliers come from this difference. We decided that, because of this, we will try to focus our analysis in the dashboard on this topic. The evolution in time seems to be great in most cases and it was increased clearly in 2020 because, of course, the pandemic and the shift to the house working, but the tendecies seems to maintain after the COVID19, which is a great sign.

Besides that, at first sight CABA and Buenos Aires seemed to be the most developed places, but the access per capita is not that great in the second but in the first one. And we had to discard the gaings (profit) dataset since it's not adjusted by inflation and on a country with more than 100 % inflation rate we can't see if profits were made of if it was product of the inflation. For a more in depth analysis you can go the [Documentation](https://github.com/pablorobba/Data_Analyst_Telecomunication_proyect/blob/main/Documentation.md) or the [EDA notebook](https://github.com/pablorobba/Data_Analyst_Telecomunication_proyect/blob/main/2%20-%20EDA.ipynb)


## Analysis 

We made the first KPI following the instructions given (We have to use a scrip to made the graphic on the PowerBI, can be found [here](https://github.com/pablorobba/Data_Analyst_Telecomunication_proyect/blob/main/script_powerbi.py)). It's one which evaluates the performance on the number of access to internet. The goal was to upgrade 2% the access. If we took the 2022 year (the last one on the datasets) and took the 3er quarter compared to the second one (we took the third because we are sure that this has the complete data, the last quarter we dont know) the goal of 2 % was reached but by a slight margin (tiny one, very tiny). We can't say it's success, but it's not a failure either. Something to be showcased it's that this goal was achieved by similar ranges on most of the provinces, the access it's somewhat being garated in equal mounts.

A big problem we see, on the other hand, it's that the internet speed in argentina has good metrics on Buenos Aires and CABA but not so in other provinces. We decided to make a KPI and took as an objetive 50 mbps speed, we look this tendency by year, we decided to look it by province and the goal is reached, as you can imagine, on the capital, with a big margin, but the average it's in 45 mbps (9% away from the goal), and in some provinces (Tierra del Fuego, Santa Cruz, San Juan) the conections are on the 10-20 mbps, very far from the 50 mbps. To do a better performance is suggested to work in the places with less access to a high speed conection, we recommend to upgrade to optic fiber, since all this places coincide to have less access to optic fiber conections and give them access to broadband (the places with less access to broadband are the same to have lower speed and some of them are on the top 10 places with more dial up users).

We want to say, as a conclution, that we have reasons to be optimistic, since the number of dial up users are lowering, on the contrary to broadband users. The conection is getting faster and the proportion of new access to the internet service is somewhere equal all long the country. The main problem to focus is the internet speed, and the solution is by upgrading the technology involved on the service and the conection. A more conected, faster, advanced, but above all, equal country is posible.


<p align='center'>
<img src ="https://as1.ftcdn.net/v2/jpg/04/67/85/46/1000_F_467854633_zTkc7XOGo73RhY4V7HFjBkW2mteE7UqL.jpg">