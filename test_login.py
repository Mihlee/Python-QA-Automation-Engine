import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_successful_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


# --- DATA-DRIVEN NEGATIVE TEST ---
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("standard_user", "wrong_password", "Epic sadface: Username and password do not match"),
        ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
        ("invalid_user", "secret_sauce", "Epic sadface: Username and password do not match"),
    ]
)
def test_invalid_login_scenarios(page: Page, username, password, expected_error):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(username, password)

    # Asserts that each specific error message matches the test input data
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text(expected_error)