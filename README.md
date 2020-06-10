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

2. Navigate into src/

3. Create virtual environment and install requirements.
> pipenv run pip install -r requirements.txt

4. Create a new folder. Name it "output" (all lower case).

5. Indicate which states to process using States.yaml (simply comment out the state and its url)

6. Run by double clicking the run.sh program.