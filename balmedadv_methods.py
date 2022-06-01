import datetime
from selenium import webdriver  # import selenium to the file
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import balmedadv_locators as locators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select # ----------add this import for drop down lists
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)


def setUp():
    print(f'Launch {locators.adv} Funnel')
    print(f'___________________________________________')
    # make browser full screen
    driver.maximize_window()
    # give browser up to 30 seconds to respond
    driver.implicitly_wait(30)
    # navigate to Balle Media Funnel
    driver.get(locators.bmfunnel_url)

    # check that Balle Media URL and the home page title are as expected
    if  driver.current_url == locators.bmfunnel_url :
        print(f'Yey! {locators.adv} Funnel launched successfully!')
        print(f'{locators.adv} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.adv} Funnel did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')
        tearDown()


def tearDown():
    if driver is not None:
        print(f'______________________________________________')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


def grow_your_clinic():
    print(f'****************************************************')
    if locators.bmfunnel_url in driver.current_url : # check we are on homepage
        driver.find_element(By.ID, 'modal_btn').click()
        print(f'Hello, You are on survey page1')
        sleep(0.25)
    else:
        print(f'Something is not right, check your code ')
        sleep(0.25)


def page_one():
    print(f'*************Survey Page1********************************************')
    driver.find_element(By.ID, 'first_name').send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.ID, 'last_name').send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.ID, 'phone').send_keys(locators.phone_number)
    sleep(0.25)
    driver.find_element(By.ID, 'email').send_keys(locators.email)
    sleep(0.25)
    driver.find_element(By.XPATH, '//button[normalize-space()="Continue"]').click()
    sleep(0.25)
    print(f'Congrats! You are moving one step ahead, Continue to Page 2')

def page_two():
    print(f'*************Survey Page2********************************************')
    assert driver.find_element(By.XPATH, '//h1[contains(., " Step 2 of 5")]').is_displayed()
    sleep(0.25)
    print(f'This is Page 2 , fill in the details')
    driver.find_element(By.ID, 'website').send_keys(locators.website)
    sleep(0.25)
    Select(driver.find_element(By.ID,'how_long_in_business')).select_by_value('2 - 5 Years')
    sleep(0.25)
    Select(driver.find_element(By.ID, 'paying_patients')).select_by_value('51-100')
    sleep(0.25)
    driver.find_element(By.ID, 'area_you_serve').send_keys(locators.area)
    sleep(0.25)
    driver.find_element(By.ID, 'how_are_you_getting_clients').send_keys(locators.subject)
    sleep(0.25)
    Select(driver.find_element(By.ID, 'current_advertising')).select_by_value('$1,001 - $5,000')
    sleep(0.25)
    driver.find_element(By.XPATH, '//button[normalize-space()="Continue"]').click()
    sleep(0.25)
    print(f'Congrats! You are moving one step ahead, Continue to Page 3')

def page_three():
    print(f'**************Survey Page3***********************************************')
    assert driver.find_element(By.XPATH, '//h1[contains(., " Step 3 of 5")]').is_displayed()
    sleep(0.25)
    print(f'This is Page 3 , fill in the details of your revenue')
    Select(driver.find_element(By.ID, 'current_monthly_revenue')).select_by_value('10000')
    sleep(0.25)
    driver.find_element(By.ID, 'target_monthly_revenue').send_keys(locators.revenue)
    sleep(0.25)
    driver.find_element(By.XPATH, '//button[normalize-space()="Continue"]').click()
    sleep(0.25)
    print(f'Congrats! You are moving again one step ahead, Continue to Page 4')

def page_four():
    print(f'***************Survey Page4*********************************************')
    assert driver.find_element(By.XPATH, '//h1[contains(., " Step 4 of 5")]').is_displayed()
    sleep(0.25)
    print(f'This is Page 4 , we are nearly finished')
    driver.find_element(By.ID, 'daily_painful_problems').send_keys(locators.subject1)
    sleep(0.25)
    driver.find_element(By.ID, 'biggest_obstacle').send_keys(locators.subject1)
    sleep(0.25)
    Select(driver.find_element(By.ID, 'how_willing')).select_by_value('I have access to the financial resources')
    sleep(0.25)
    driver.find_element(By.ID, 'how_soon_get_started').send_keys(locators.start)
    sleep(0.25)
    driver.find_element(By.ID, 'why_choose_you').send_keys(locators.text)
    sleep(0.25)
    driver.find_element(By.XPATH, '//button[normalize-space()="Continue"]').click()
    sleep(0.25)
    print(f'Hurrey! We are almost finished, Continue to Page 5')

def page_five():
    print(f'****************This is a Booking Confirmation Page*******************************')
    assert driver.find_element(By.XPATH, f'//h1[contains(., "Thank you")]').text
    booking_confirmation = driver.find_element(By.XPATH, f'//h1[contains(., "Thank you")]').text
    print(booking_confirmation)
    if locators.first_name in booking_confirmation:
        print(f' You have booked an appointment: {booking_confirmation}')
        print(f' Congratulation! The booking is confirmed')
    else:
        print(f'Something is not right, check your code')
        sleep(0.25)

    assert driver.find_element(By.XPATH, f'//h2[contains(., "Check your inbox for your appointment")]').text
    email_confirmation = driver.find_element(By.XPATH, f'//h2[contains(., "Check your inbox for your appointment")]').text
    print(email_confirmation)
    print(f'Hello! Let us meet on the day of appointment to discuss details. ')






#
# setUp()
# grow_your_clinic()
# page_one()
# page_two()
# page_three()
# page_four()
# page_five()
# tearDown()