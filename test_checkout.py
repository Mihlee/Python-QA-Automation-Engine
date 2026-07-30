from playwright.sync_api import expect
from pages.checkout_page import CheckoutPage

def test_full_checkout_flow(logged_in_page):
    # Setup our Page Object
    page = logged_in_page 
    checkout_page = CheckoutPage(page)

    # 1. Add item and assert it worked
    checkout_page.add_backpack_to_cart()
    expect(checkout_page.cart_badge).to_have_text("1")

    # 2. Go to cart and verify item
    checkout_page.go_to_cart()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(checkout_page.item_name).to_have_text("Sauce Labs Backpack")

    # 3. Proceed to checkout and fill out the form
    checkout_page.start_checkout()
    checkout_page.fill_personal_info("Mihle", "Potwana", "8001")

    # 4. Finish the order
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    checkout_page.finish_order()

    # 5. Final Assertions
    expect(checkout_page.success_message).to_have_text("Thank you for your order!")