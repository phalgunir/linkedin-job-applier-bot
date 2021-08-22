import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

MY_EMAIL = 'dummy_email@gmail.com'
MY_PASSWORD = 'dummy_password'
MY_PHONE_NUMBER = '12345678'
JOB_SEARCH_KEYWORD = 'Python Developer'
JOB_SEARCH_LOCATION = 'London'
login_page_url = 'https://www.linkedin.com/checkpoint/lg/login'

chrome_driver_path = '/Applications/chromedriver'
chrome_path = '/Applications/Google Chrome.app'
driver = webdriver.Chrome(chrome_driver_path)


def login_to_linkedin():
    """Opens the LinkedIn login page and logs in using your username and password"""
    driver.get(login_page_url)
    driver.find_element_by_id('username').send_keys(MY_EMAIL)
    driver.find_element_by_id('password').send_keys(MY_PASSWORD)
    time.sleep(2)
    driver.find_element_by_tag_name('button').click()


def search_for_jobs():
    """Loads the linkedin jobs page and searches for the JOB_SEARCH_KEYWORD in JOB_SEARCH_LOCATION with 'Easy Apply' filter"""
    # finds the 'jobs' page tab from the top menu bar
    top_menu = driver.find_elements_by_class_name('global-nav__primary-link-text')
    for item in top_menu:
        if item.text.lower() == 'jobs':
            item.click()
    time.sleep(2)

    # enters the search keyword and location and clicks 'search'
    driver.find_element_by_css_selector('.jobs-search-box__input--keyword input').send_keys(JOB_SEARCH_KEYWORD)
    driver.find_element_by_css_selector('.jobs-search-box__input--location input').send_keys(JOB_SEARCH_LOCATION)
    time.sleep(2)
    driver.find_element_by_css_selector('.jobs-search-box__submit-button').click()
    time.sleep(2)

    # applies the 'Easy Apply' filter to the search results
    job_filter_buttons = driver.find_elements_by_css_selector('.search-filters-bar button')
    for job_filter in job_filter_buttons:
        if job_filter.text.lower() == 'easy apply':
            job_filter.click()


def save_job():
    """Saves the job posting."""
    try:
        # click on the save button in the job posting
        driver.find_element_by_css_selector('.jobs-search__right-rail .jobs-save-button').click()
    except NoSuchElementException:
        print("You've already applied to this job. Skipped it")
    else:
        time.sleep(2)
        try:
            # dismiss the 'Job Saved/Unsaved' pop up at the bottom
            driver.find_element_by_css_selector('.artdeco-toast-item button').click()
        except NoSuchElementException:
            print('No job saved/unsaved popup present.')
        print('Saved job.')


def apply_for_job():
    """If the job posting is a one-step application, applies to the job. Else, skips applying to it."""
    try:
        # click on the 'Easy Apply' button in the job posting
        driver.find_element_by_class_name('jobs-apply-button').click()
    except NoSuchElementException:
        print("You've already applied to this job. Skipped it")
    else:
        # input the phone number
        phone_no_field = driver.find_element_by_tag_name('input')
        phone_no_field.send_keys(Keys.COMMAND, 'a')
        phone_no_field.send_keys(Keys.DELETE)
        phone_no_field.send_keys(MY_PHONE_NUMBER)
        time.sleep(2)

        submit_button = driver.find_element_by_css_selector('.artdeco-button--primary span')

        # if bottom button is anything but 'submit application', skip applying to that job
        if submit_button.text.lower() != 'submit application':
            print('Complex application. Skipped applying to this job.')
            # click on 'close' button
            driver.find_element_by_class_name('artdeco-modal__dismiss').click()
            time.sleep(2)
            # confirm closing in the 'confirm' dialog box
            driver.find_elements_by_class_name('artdeco-modal__confirm-dialog-btn')[1].click()
            time.sleep(2)

        else:
            # submit application
            submit_button.click()
            time.sleep(2)
            # close the 'submitted application' dialog box
            close_button = driver.find_element_by_class_name('artdeco-modal__dismiss')
            close_button.click()
            print('Applied to job.')


# main
login_to_linkedin()
time.sleep(3)
search_for_jobs()
time.sleep(3)

# save/apply for all jobs in the job search results page
job_search_results = driver.find_elements_by_css_selector('.jobs-search-results__list-item')
for job in job_search_results:
    print('\n')
    print(job.text.split("\n")[0], job.text.split("\n")[1])
    job.click()
    time.sleep(3)   # is needed, waits for page load before saving/applying
    save_job()
    time.sleep(3)
    apply_for_job()
    time.sleep(3)

time.sleep(5)
driver.quit()
