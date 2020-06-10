# COVID_school_district_analytics
This repository is a resource for collecting and scraping data sources that provide information on state and district wide closures due to the COVID-19 pandemic.


## Folder Structure
COVID_school_district_analytics
|   .gitignore
|   README.md
|       
+---output
|       Alabama_School_Dates.xlsx
|       Idaho_School_Dates.xlsx
|       Nebraska_School_Dates.xlsx
|       
\---src
    |   chromedriver.exe
    |   debug.log
    |   Pipfile
    |   Pipfile.lock
    |   run.sh
    |   
    \---data_extraction
            scrape_publicholidays.py
            States.yaml

## Directions
1. Clone repo to your local machine:
> git clone https://github.com/nadiasbell12/COVID_school_district_analytics.git

2. Navigate into src and create a new folder. Name it "output" (all lower case).

