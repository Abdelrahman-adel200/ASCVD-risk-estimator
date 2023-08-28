# inputs from user
month = int(input('What is your birthday month? '))
year = int(input('What is your birthday year? '))
sex = str(input('sex? male or female ')).lower()
systolic = int(input('systolic blood pressure: '))
cholesterol = float(input('total Cholesterol mmol/L: '))
hdl = float(input('HDL mmol/L: '))
ldl = float(input('LDL mmol/L: '))
smoke = str(input('Do you smoke? yes or no ')).lower()

# opening the webpage
from selenium import webdriver
import time
web = webdriver.Chrome()
web.get('https://heartscore.escardio.org/Calculate/quickcalculator.aspx?model=veryhigh')
time.sleep(1)

# inputting the data
month_x = web.find_element('xpath', '//*[@id="ctl00_ContentPlaceHolder1_CalculatorsQuick1_monthDDL"]')
month_x.send_keys(month)
time.sleep(1)

year_x = web.find_element('xpath', '//*[@id="ctl00_ContentPlaceHolder1_CalculatorsQuick1_yearDDL"]')
year_x.send_keys(year)
time.sleep(1)

if sex == 'male':
    sex_x = web.find_element('xpath', '//*[@id="ctl00_ContentPlaceHolder1_CalculatorsQuick1_rdbGender_0"]')
    sex_x.click()
    time.sleep(1)
elif sex == 'female':
    sex_x = web.find_element('xpath', '//*[@id="ctl00_ContentPlaceHolder1_CalculatorsQuick1_rdbGender_1"]')
    sex_x.click()
    time.sleep(1)

systolic_x = web.find_element('xpath', '//*[@id="ctl00_ContentPlaceHolder1_CalculatorsQuick1_cboSBP"]')
systolic_x.send_keys(systolic)
time.sleep(1)

cholesterol_x = web.find_element('xpath', '//*[@id="ctl00_ContentPlaceHolder1_CalculatorsQuick1_cboCholTotal"]')
cholesterol_x.send_keys(cholesterol)
time.sleep(1)

hdl_x = web.find_element('xpath', '//*[@id="ctl00_ContentPlaceHolder1_CalculatorsQuick1_cboHDL"]')
hdl_x.send_keys(hdl)
time.sleep(1)

ldl_x = web.find_element('xpath', '//*[@id="ctl00_ContentPlaceHolder1_CalculatorsQuick1_cboLDL"]')
ldl_x.send_keys(ldl)
time.sleep(1)

if smoke == 'yes':
    smoke_x = web.find_element('xpath', '//*[@id="ctl00_ContentPlaceHolder1_CalculatorsQuick1_rdbSmokerFullScore_0"]')
    smoke_x.click()
    time.sleep(1)
elif smoke == 'no':
    smoke_x = web.find_element('xpath', '//*[@id="ctl00_ContentPlaceHolder1_CalculatorsQuick1_rdbSmokerFullScore_1"]')
    smoke_x.click()
    time.sleep(1)

estimate = web.find_element('xpath', '//*[@id="ctl00_ContentPlaceHolder1_CalculatorsQuick1_btnCalculateFullScore"]')
estimate.click()

risk = float(input('What is your risk score? '))