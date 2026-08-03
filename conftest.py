import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page

# Load variables from .env file
load_dotenv()

@pytest.fixture
def logged_in_page(page: Page):
    # Fetch environment variables (with fallback defaults if missing)
    username = os.getenv("SAUCE_USERNAME", "standard_user")
    password = os.getenv("SAUCE_PASSWORD", "secret_sauce")

    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill(username)
    page.locator("#password").fill(password)
    page.locator("#login-button").click()
    yield page