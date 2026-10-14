import re
from playwright.sync_api import Playwright, sync_playwright, expect

ROUND_MAX = 10

def run(playwright: Playwright) -> None:
    round_atual = 1
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rpachallenge.com/")
    page.get_by_role("button", name="Start").click()

    #Colocar loop aqui
    while round_atual <= ROUND_MAX:
        page.locator("label", has_text="Last name").locator("xpath=following-sibling::input").fill("Challenge") #Last name
        page.locator("label", has_text="First name").locator("xpath=following-sibling::input").fill("RPA") #First name
        page.locator("label", has_text="Email").locator("xpath=following-sibling::input").fill("teste@email.com") #Email
        page.locator("label", has_text="Company Name").locator("xpath=following-sibling::input").fill("Empresa1") #Company Name
        page.locator("label", has_text="Phone number").locator("xpath=following-sibling::input").fill("9988776655") #Phone number
        page.locator("label", has_text="Role in Company").locator("xpath=following-sibling::input").fill("Analista RPA")#Role in Company 
        page.locator("label", has_text="Address").locator("xpath=following-sibling::input").fill("rua dos coqueiros, 555") #Address
        page.get_by_role("button", name="Submit").click()
        round_atual += 1

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)