from playwright.sync_api import Page, expect

def test_full_checkout_flow(page: Page):
    # 1. Login (We must be logged in to shop)
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    # 2. Add an item to the cart (Sauce Labs Backpack)
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()

    # 3. Assert the shopping cart badge updates to '1'
    cart_badge = page.locator(".shopping_cart_badge")
    expect(cart_badge).to_have_text("1")

    # 4. Navigate to the cart page
    page.locator(".shopping_cart_link").click()

    # 5. Assert we are on the cart page and the correct item is there
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    item_name = page.locator(".inventory_item_name")
    expect(item_name).to_have_text("Sauce Labs Backpack")

    # 6. Proceed to Checkout
    page.locator("[data-test='checkout']").click()

    # 7. Fill out the checkout information form
    page.locator("[data-test='firstName']").fill("Mihle")
    page.locator("[data-test='lastName']").fill("Potwana")
    page.locator("[data-test='postalCode']").fill("8001") # Cape Town postal code!
    
    page.locator("[data-test='continue']").click()

    # 8. Assert we are on the final overview page, then finish the order
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    page.locator("[data-test='finish']").click()

    # 9. Final Assertion: Verify the success message appears
    success_message = page.locator(".complete-header")
    expect(success_message).to_have_text("Thank you for your order!")