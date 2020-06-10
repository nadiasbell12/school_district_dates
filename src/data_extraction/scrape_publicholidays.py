# package imports
from selenium import webdriver
import pandas as pd
import numpy as np
import yaml

# python standard library
import re, time
from datetime import datetime

def extract_links(driver, url):
    """[Get all the links from the table so we can navigate to each without having to go 'back']

    Arguments:
        driver {[driver object]} -- [used to navigate webpages]

    Returns:
        [dictionary] -- [keys are the school district names, values are the links that bring you to each school district's information]
    """
    # navigate to url and locate the table with the school districts
    driver.get(url)
    mytable = driver.find_element_by_css_selector('table[id^=tablepress-]')

    link_dict = {}
    # iterate through rows and columns
    for row in mytable.find_elements_by_css_selector('tr'):
        for cell in row.find_elements_by_tag_name('td'):
            try:
                element = cell.find_element_by_tag_name('a')
                link = element.get_attribute('href')
                link_dict[element.text] = [link]
            except:
                pass
    
    return link_dict

def get_dates(driver, url):
    # modify to get start date
    driver.get(url)
    obj = driver.find_elements_by_xpath('//*[@id="row-inner-travel"]/article/div[1]/table[1]')
    print(len(obj))
    table = (obj[0].text)
    start_date = re.search('First Day of School (?P<start_date>.+)\n', table).group('start_date').strip()
    end_date = re.search('Last Day of School (?P<end_date>.+)', table).group('end_date').strip()
    start_date_formatted = datetime.strptime(start_date, "%d %b %Y")
    end_date_formatted = datetime.strptime(end_date, "%d %b %Y")

    return start_date_formatted, end_date_formatted

def main():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    # this chunk was used to create States.yaml
    # state_url_dict = extract_links(driver, "https://publicholidays.us/school-holidays/")
    # with open('data_extraction/States.yaml', 'w') as f:
    #     data = yaml.dump(state_url_dict, f)

    # read in the yaml file to control which states to process
    with open('data_extraction/States.yaml') as f:
        state_url_dict = yaml.load(f, Loader=yaml.FullLoader)
    
    for state, url in state_url_dict.items():
        # obtain dictionary with each district as the keys and urls for that district as the values
        district_url_dict = extract_links(driver, url[0])

        for district_name, url in district_url_dict.items():
            print(district_name)
            try:
                start_date, end_date = get_dates(driver, url[0])
            except:
                start_date, end_date = np.nan, np.nan
            district_url_dict[district_name].append(start_date)
            district_url_dict[district_name].append(end_date)
            time.sleep(240)
        # format into dataframe
        dates_df = pd.DataFrame.from_dict(district_url_dict, orient='index')
        dates_df.columns = ['url', 'startDate', 'endDate']
        dates_df.to_excel(f'C:/Users/bsmit/Projects/COVID/COVID_school_district_analytics/output/{state}_School_Dates.xlsx')
    
    driver.close()


if __name__ == '__main__':
    # execute only if run as a script
    main()
