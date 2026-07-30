from playwright.sync_api import Page, expect

def test_successful_login(page: Page):
    # 1. Navigate to the practice website
    page.goto("https://www.saucedemo.com/")

    # 2. Fill in the login form fields
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")

    # 3. Click the login button
    page.locator("#login-button").click()

    # 4. Assert: Verify we were redirected to the inventory page
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    # 5. Assert: Verify the page header text displays "Products"
    header = page.locator(".title")
    expect(header).to_have_text("Products")


    def test_invalid_password_error(page: Page):
    # 1. Navigate to the practice website
    page.goto("https://www.saucedemo.com/")

    # 2. Fill in the right username, but a WRONG password
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("completely_wrong_password")

    # 3. Click the login button
    page.locator("#login-button").click()

    # 4. Assert: Verify the error message container is visible on screen
    error_message = page.locator("[data-test='error']")
    expect(error_message).to_be_visible()

    # 5. Assert: Verify the exact text inside the error message
    expect(error_message).to_contain_text("Epic sadface: Username and password do not match")