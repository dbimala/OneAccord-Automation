from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
import helper


# Test Case1:Onboarding Church - Paid Church

driver.get("https://payment.staging.oneaccord.cc/the-one-plan?step=welcome")
driver.maximize_window()
wait = WebDriverWait(driver, 20)

cookie_accept_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Accept']"))
)
cookie_accept_button.click()
time.sleep(1)

wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Next']"))
).click()

wait.until(
    EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])[2]"))
).click()

wait.until(
    EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])[4]"))
).click()

wait.until(
    EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])[6]"))
).click()

wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[@data-testid='onboarding-bso-consent-accepted-yes-btn']")
    )
).click()

wait.until(
    EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Next'])[1]"))
).click()

wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "(//button[@data-testid='onboarding-affiliated-church-division-select'])",
        )
    )
).click()

divisionOptions = wait.until(
    EC.presence_of_all_elements_located(
        (
            By.XPATH,
            "//div[@data-testid='onboarding-affiliated-church-division-select-option']",
        )
    )
)
helper.selectRandom(divisionOptions)
time.sleep(1)

wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, 
         "//button[@data-testid='onboarding-affiliated-church-union-select']",
    )
)
).click()

unionOptions = wait.until(
    EC.presence_of_all_elements_located(
        (
            By.XPATH,"//div[@data-testid='onboarding-affiliated-church-union-select-option']",
        )
    )
)

helper.selectRandom(unionOptions)
time.sleep(1)

wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "(//button[@data-testid='onboarding-affiliated-church-conference-select'])",
        )
    )
).click()

ConferenceOptions = wait.until(
    EC.presence_of_all_elements_located(
        (
            By.XPATH,
            "//div[@data-testid='onboarding-affiliated-church-conference-select-option']",
        )
    )
)
helper.selectRandom(ConferenceOptions)
time.sleep(1)

wait .until(
    EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='onboarding-next-step-btn']"))
).click()
time.sleep(2)


church_name = helper.generate_random_church_name()
church_input = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='onboarding-church-name-input']"))
)
church_input.clear()
church_input.send_keys(church_name)
time.sleep(2)

wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='onboarding-church-address-input']"))
).click()
time.sleep(2)

driver.find_element(By.XPATH,"//input[@data-testid='address-picker-search-input']").send_keys("123 Main St, Springfield, USA")
time.sleep(2)

LocationOption = wait.until(
    EC.presence_of_all_elements_located(
        (
            By.XPATH,
            "//button[@data-testid='address-picker-suggestion-item']",
        )
    )
)
helper.selectRandom(LocationOption)
time.sleep(2)


driver.find_element(By.XPATH, "//button[@data-testid='address-picker-continue-btn']").click()
time.sleep(2)

wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='address-picker-save-btn']"))
).click()
time.sleep(2)

wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='radio-preferred-language-english']"))
).click()
time.sleep(2)

wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='onboarding-next-step-btn']"))
).click()
time.sleep(2)

wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='onboarding-assigned-pastor-yes-btn']"))
).click()
time.sleep(2)

firstname, lastname, email = helper.generate_random_user(None)
driver.find_element(By.XPATH, "//input[@data-testid='onboarding-pastor-first-name-input']").send_keys(firstname)

driver.find_element(By.XPATH, "//input[@data-testid='onboarding-pastor-last-name-input']").send_keys(lastname)
driver.find_element(By.XPATH, "//input[@data-testid='onboarding-pastor-email-input']").send_keys(email)
driver.find_element(By.XPATH, "//input[@data-testid='onboarding-pastor-phone-input']").send_keys("(312) 756-3418")
time.sleep(2)

wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='onboarding-managed-by-pastor-yes-radio']"))
).click()

wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='onboarding-terms-agreed-checkbox']"))
).click()

wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='onboarding-next-step-btn']"))
).click()
time.sleep(2)


# CheckOUt for the paid church

time.sleep(3)
textbox=driver.find_element(By.XPATH, "//input[@data-testid='onboarding-yearly-promo-code-input']")
textbox.send_keys("AMTBIM2025")

wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='onboarding-apply-yearly-promo-code-btn']"))
).click()


stripe_iframes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "iframe[src*='stripe.com']")))

print(f"Found {len(stripe_iframes)} Stripe iframes.")

def fill_stripe_input(input_name, value):

    found = False
    for iframe in stripe_iframes:
        driver.switch_to.frame(iframe)
        try:
            input_field = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.NAME, input_name))
            )
            input_field.send_keys(value)
            found = True
            print(f"Filled '{input_name}' successfully.")
            driver.switch_to.default_content()
            break
        except:
            driver.switch_to.default_content()
            continue
    if not found:
        print(f"❌ Could not find input with name: {input_name}")


fill_stripe_input('cardnumber', '4242 4242 4242 4242')
fill_stripe_input('exp-date', '12 / 28')
fill_stripe_input('cvc', '123')
time.sleep(2)

driver.find_element(By.XPATH, "//input[@data-testid='onboarding-checkout-cardholder-name-input']").send_keys(firstname + " " + lastname)
time.sleep(5)

wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='onboarding-subscribe-btn']"))
).click()
time.sleep(5)






