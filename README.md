# COVID_school_district_analytics
This repository is a resource for collecting and scraping data sources that provide information on state and district wide closures due to the COVID-19 pandemic.


## Folder Structure
COVID_school_district_analytics
|   .gitignore
|   README.md
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
    \---output
            Alabama_School_Dates.xlsx
            etc.

## Directions
1. Clone repo to your local machine:
> git clone https://github.com/nadiasbell12/COVID_school_district_analytics.git

Note: Make sure you have pipenv installed. You can do that by running
> pip install pipenv
More info here: https://pypi.org/project/pipenv/

2. Navigate into src/

3. Double click setup.sh - this will create the virtual environment, install requirements, and create a folder named 'output'.

4. Indicate which states to process using States.yaml (simply comment out the state and its url)

5. Run scraping program by double clicking run.sh