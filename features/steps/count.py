from behave import step
from selenium.webdriver.common.by import By

@step(u'that I access the website "{url}"')
def step_impl(context, url):
    context.driver.get(url)

@step(u'I enter {first_number} in the first field')
def step_impl(context, first_number):
    send_number(context, "sum1", first_number)

@step(u'I enter {second_number} in the second field')
def step_impl(context, second_number):
    send_number(context, "sum2", second_number)

@step(u'click the "{button_text}" button')
def step_impl(context, button_text):
    context.driver.find_element(By.XPATH, '//button[text()="' + button_text + '"]').click()

@step(u'the result will be {expected_result}')
def step_impl(context, expected_result):
    result = context.driver.find_element(By.XPATH, "//*[@id=\'addmessage\']").text
    assert expected_result == result

def send_number(context, element_id, value):
    context.driver.find_element(By.ID, element_id).send_keys(value)