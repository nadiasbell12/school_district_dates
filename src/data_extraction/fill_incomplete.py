# local imports
from scrape_publicholidays import get_dates

# downloaded packages
from selenium import webdriver
import pandas as pd

# python standard library
import os
import time

def main():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    # read in files from /migrated and fill out any missing rows
    for state_file in os.listdir(f'output/migrated'):
        df = pd.read_excel(f'output/migrated/{state_file}', index_col=0)
        idx_missing = df.startDate.isnull()
        if idx_missing.sum() > 0:
            df_missing = df.loc[idx_missing, :]
            for url in df_missing.url:
                district_url = df.loc[idx_missing, 'url'].values[0]
                start_date, end_date = get_dates(driver, district_url)
                df.loc[df.url == url, 'startDate'] = start_date
                df.loc[df.url == url, 'endDate'] = end_date
                time.sleep(240)
        
        # output in /output folder
        df.to_excel(f'output/{state_file}')

    driver.close()


if __name__ == '__main__':
    # execute only if run as a script
    main()
