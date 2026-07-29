from playwright.sync_api import expect

# Notice we ask for 'logged_in_page' instead of just 'page'
def test_full_checkout_flow(logged_in_page):
    # We rename it to 'page' just to keep the rest of the code the same
    page = logged_in_page 

    # 1. Add an item to the cart (Notice we skipped the login steps entirely!)
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()

    # 2. Assert the shopping cart badge updates to '1'
    cart_badge = page.locator(".shopping_cart_badge")
    expect(cart_badge).to_have_text("1")

    # 3. Navigate to the cart page
    page.locator(".shopping_cart_link").click()

    # 4. Assert we are on the cart page and the correct item is there
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    item_name = page.locator(".inventory_item_name")
    expect(item_name).to_have_text("Sauce Labs Backpack")

    # 5. Proceed to Checkout
    page.locator("[data-test='checkout']").click()

    # 6. Fill out the checkout information form
    page.locator("[data-test='firstName']").fill("Mihle")
    page.locator("[data-test='lastName']").fill("Potwana")
    page.locator("[data-test='postalCode']").fill("8001") 
    
    page.locator("[data-test='continue']").click()

    # 7. Assert we are on the final overview page, then finish the order
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    page.locator("[data-test='finish']").click()

    # 8. Final Assertion: Verify the success message appears
    success_message = page.locator(".complete-header")
    expect(success_message).to_have_text("Thank you for your order!")