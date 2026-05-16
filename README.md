🚖 Uber/Ola Ride Analytics

📌 Project Overview

The Uber/Ola Ride Analytics Dashboard is an end-to-end data analytics and business intelligence project developed to analyze ride-booking patterns, revenue trends, customer demand, and operational performance.

This project uses real-world Uber trip data combined with generated business metrics to simulate a professional ride-booking analytics system similar to platforms like Uber and Ola.

The project demonstrates practical skills in:

Data Cleaning

Exploratory Data Analysis (EDA)

SQL Analytics

Data Visualization

Business Intelligence

Dashboard Development

KPI Reporting

🎯 Project Objectives

The main objectives of this project are:

Analyze ride booking trends

Identify peak booking hours

Understand ride demand patterns

Analyze revenue generation

Compare vehicle category performance

Track ride completion and cancellation rates

Visualize geographic ride hotspots

Build an interactive Tableau dashboard

Generate business insights for decision-making
 
 🛠️ Technologies Used

Technology	Purpose

Python	Data cleaning and preprocessing

Pandas	Data manipulation

NumPy	Numerical operations

SQL (MySQL)	Business analytics queries

Tableau	Interactive dashboard visualization

Google Colab	Python development environment

GitHub	Project hosting and portfolio

📂 Project Structure

Uber_Ola_Analytics/

│

├── data/

│   └── cleaned_uber_data.csv

│

├── notebooks/

│   └── Uber_Ola_Analytics.ipynb

│

├── sql/

│   └── queries.sql

│

├── dashboard/

│   └── uber_dashboard.twbx

│

├── images/

    └── dashboard_screenshots.png

📊 Dataset Information

The dataset used in this project is based on Uber pickup ride data.

Original dataset columns included:

Date/Time

Latitude

Longitude

Base

Additional business-related columns were generated using Python to create a realistic analytics environment.

Generated columns include:

Trip Distance

Fare Amount

Driver Rating

Vehicle Type

Ride Status

Payment Method

Hour

Day

Month

🧹 Data Preprocessing

Data preprocessing was performed using Python and Pandas.

Steps Performed

Removed duplicate records

Handled missing values

Converted datetime columns

Created time-based features

Generated synthetic business metrics

Prepared data for SQL and Tableau analysis

📈 Exploratory Data Analysis (EDA) 

📊 Tableau Dashboard

Several analytical operations were performed to identify business insights.

Key Analyses

🚖 Peak Booking Hour Analysis

Identified the hours with maximum ride demand.

💰 Revenue Analysis

Calculated total revenue and revenue trends across ride categories.

🚗 Vehicle Type Distribution

Compared the performance of different vehicle categories.

❌ Ride Status Analysis

Analyzed completed vs cancelled rides.

🌍 Geo Hotspot Analysis

Visualized ride pickup density using maps.

🌟 Business Insights

The project generated several useful insights:

Ride demand increases significantly during peak office hours

Certain vehicle categories contribute more revenue

Ride cancellations are concentrated during high-demand periods

Geographic hotspots indicate densely active ride zones

Revenue patterns fluctuate across time intervals
