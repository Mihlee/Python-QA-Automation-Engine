from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_successful_login(page: Page):
    login_page = LoginPage(page)
    
    # Use the blueprint actions!
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # Assertions stay in the test file
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


def test_invalid_password_error(page: Page):
    login_page = LoginPage(page)
    
    login_page.navigate()
    login_page.login("standard_user", "completely_wrong_password")

    # We can even use the locators saved in the blueprint!
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("Epic sadface: Username and password do not match")