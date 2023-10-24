from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Specify path to Chrome Driver
PATH = '/home/kosho/Desktop/Coding/Bislin/chromedriver'

# URL to scrape
url = "http://walter.bislins.ch/bloge/index.asp?page=Display+Geo+Data&data=Causeway+North"

# Initialize WebDriver with the specified chrome driver's executable file
browser = webdriver.Chrome(executable_path=PATH)
# Open the webpage
browser.get(url)

# Waits up to 2 seconds for elements to become available before throwing an exception
browser.implicitly_wait(2)

# Container for position data
positions = []

# Helper function that prepares the webpage for scraping
def get_ready():
    # Click a specific element on the page
    browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div/div[3]/div/div/div[3]/b/a').click()
    # Provide some time for the page to load
    browser.implicitly_wait(5)

# Collecting the positions data from the page
def grab_positions():
    for i in range(2,2059):
        str_i = str(i)
        # Grab data from specific cells in the table.
        data = [browser.find_element(By.XPATH, f'/html/body/div[3]/div[2]/div/div/div[3]/div/div/div[3]/table/tbody/tr[{str_i}]/td[{j}]').text for j in range(3, 8)]
        print(data)
        positions.append(data)
    # Print completion status
    print("done")
    # Save list of positions into a DataFrame and then to a CSV file
    df = pd.DataFrame(positions)
    df.to_csv('leads.csv')

# Call our functions
get_ready()
grab_positions()

# Close the browser
browser.quit()
