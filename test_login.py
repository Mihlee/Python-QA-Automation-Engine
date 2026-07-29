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