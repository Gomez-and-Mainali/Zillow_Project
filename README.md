# Zillow_Project

## Goal:
**Create a model that predicts the values of a single unit properties that the tax district assesses using the property data from those whose last transaction was during 
he months of May and June of 2017.**

## Data Dictionary:
- **parcelid:** Id assigned by local tax office that is unique to each property 
- **bedroomcnt:** Number of bedrooms
- **bathroomcnt:** Number of bathrooms including full
- **countyid:** Unique id to represent each county
- **zipcode:** Zipcode where the property is located
- **fips:** Federal Information Processing Standards that uniquely identifies a geographical area
- **lotsize:** Size of the property lot
- **finishedsquarefeet:** Size of the property/house
- **taxvaluedollarcnt:** total value of the property as assessed by the county for tax purpose


## Phases:
- **Planning**
  - Outline steps that must be taken to complete each phase of the pipeline
- **Acqusition**
  - With credentials to login, acquire data from the CodeUp database.
  - Create a cache function to store the data on the local machine 
  - All the function necessary to complete this phase are in **acquire.py** module
  
- **Preparation**
  - Prepare the data by taking care of the null values(impute or drop)
  - Change the name of the columns for better readability 
  - Remove repeated columns
  - Change data types
  - Drop outliers
  - Drop columns that dont contribute to the target varibales(zipcode, parcelid etc)
  - Split data into train, test, and validate
  - Create **prepare.py** module containing functions to do all of the above steps for reproducibility
  
- **Exploration**
  - Explore various variables to discover relationsips between dependent and independent variables
  - Run hypothesis test(atleast 1 T-test, and 1 Correlation test
  - Create vizualizations depicting relationships, correlations.
  - Notedown takeaways, discoveries
  - Scale data to get it ready for modeling
- **Modeling**
  - Use features identified by the stakeholders to create a model
  - Create models using features identified as having strong relationship with targget variable during the exploration phase to create models
  - Validate with top performing models
  - Test with one top performing model on validate data
- **Evaluation**
  - Evaluate model using Root Mean Squared Error metric
- **Summary/Findings**
  - Drivers of the property value are:
    - Squarefeet of the house
    - Number of bathhrooms
    - Number of bedrooms
    - County the property is
  - The average property value in LA County is significantly lower than Orange and Ventura County
 

## How to reproduce?
- Download **acquire.py** module and use it to acquire the data. Requires credentials to access the databse
- Download **prepare.py** module and use its functions to prepare the data
