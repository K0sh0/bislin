import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from gspread.oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Google Drive API permissions
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive',
         'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/spreadsheets']

# Get connection with the Google Sheets API 
creds = ServiceAccountCredentials.from_json_keyfile_name('mod.json', scope)
client = gspread.authorize(creds)

# Access the specific Google Sheet using its URL
sheet = client.open_by_url("SheetLink").sheet1

# Path to the Chrome driver
PATH ='C:/Users/Kosho/Desktop/code/chromedriver.exe'

# Target URL for scraping data
url = "https://onlinemschool.com/math/assistance/cartesian_coordinate/p_line/"
browser = webdriver.Chrome(executable_path=PATH)
browser.get(url)

# List to store distance data
distances = []

# Loop twice to fill the form using the values from Google Sheet
for i in range(2):
    # Fetch the values from Google Sheet and fill the form
    for cell in ['I', 'K', 'O', 'Q', 'U', 'W', 'Y']:
        value = sheet.get_values(cell + str(i + 2))
        field = browser.find_element(By.XPATH, '/html/body/div[2]/article/section[1]/div/div[3]/div/input[' + str(i + 1) + ']')
        field.clear()
        field.send_keys(value)
        time.sleep(.3)
    
    # Click the button to calculate distance
    browser.find_element(By.XPATH, '/html/body/div[2]/article/section[1]/div/p/input').click()
    time.sleep(2)

    # Fetch the distance from the resulting page
    distance = browser.find_element(By.XPATH, '/html/body/div[2]/article/div[4]/div[3]/div/div[2]/div[6]').text
    
    # Process the string to obtain the numerical distance
    if('≈' in distance):
        distance = distance.split('≈')[1]
    else:
        distance = distance.split('=')[-1]
    
    # Append distance to the list
    distances.append(distance)
    time.sleep(2)

# Quit the browser 
browser.quit()

# Export distances to CSV
df = pd.DataFrame(distances)
df.to_csv('distances.csv')
