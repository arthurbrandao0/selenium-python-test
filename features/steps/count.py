from behave import step
from selenium.webdriver.common.by import By

@step(u'que eu acesse o site "{url}"')
def step_impl(context, url):
    context.driver.get(url)

@step(u'eu informar {firt_number} no primeiro campo')
def step_impl(context, firt_number):
    context.driver.find_element(By.ID, "sum1").send_keys(firt_number)

@step(u'eu informar {second_number} no segundo campo')
def step_impl(context, second_number):
    context.driver.find_element(By.ID, "sum2").send_keys(second_number)

@step(u'clicar no botão "{button_text}"')
def step_impl(context, button_text):
    context.driver.find_element(By.XPATH, '//button[text()="' + button_text + '"]').click()

@step(u'o resultado será {expected_result}')
def step_impl(context, expected_result):
    result = context.driver.find_element(By.XPATH, "//*[@id=\'addmessage\']").text
    assert expected_result == result