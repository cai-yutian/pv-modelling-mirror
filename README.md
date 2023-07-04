# PV System Power Modelling
Synthetic data creation for different types of PV degradation and use these data to train models for classification. 

## Setup and Usage
1. Use Poetry (https://python-poetry.org/) to install dependencies
```bash
poetry install
```
2. Refer to the notebooks to view data synthesis and model training 

## Raw Data Source 
There are 2 main data sources:  
1. Time series data generated using NREL's PVWatts model (https://developer.nrel.gov/docs/solar/pvwatts/v8/)  
2. (To be implemented) Data from NREL's PV Data Acquisition project (https://developer.nrel.gov/docs/solar/pvdaq-v3/) 

## Data Processing
Degradation rates for PID, LETID and LID are mixed in with the raw data to create different time series data for each degradation type. 

## Degradation Rate Classification  
(To be implemented)  
List of libraries and methods to try:  
- Darts (https://unit8co.github.io/darts/) 
- rdtools (https://rdtools.readthedocs.io/en/stable/)