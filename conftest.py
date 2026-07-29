import pytest
from playwright.sync_api import Page

@pytest.fixture
def logged_in_page(page: Page):
    # 1. Navigate and log in
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    
    # 2. Hand the logged-in page over to the test that called it
    yield page