class CheckoutPage:
    def __init__(self, page):
        self.page = page
        
        # --- LOCATORS ---
        # Inventory & Cart Elements
        self.add_backpack_btn = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")
        self.backpack_name = page.locator( '[data-test="inventory-item-name"]' ).filter(has_text="Sauce Labs Backpack")
        self.checkout_btn = page.locator("[data-test='checkout']")
        
        # Checkout Form Elements
        self.first_name_input = page.locator("[data-test='firstName']")
        self.last_name_input = page.locator("[data-test='lastName']")
        self.postal_code_input = page.locator("[data-test='postalCode']")
        self.continue_btn = page.locator("[data-test='continue']")
        
        # Final Order Elements
        self.finish_btn = page.locator("[data-test='finish']")
        self.success_message = page.locator(".complete-header")

    # --- ACTIONS ---
    def add_backpack_to_cart(self):
        self.add_backpack_btn.click()

    def go_to_cart(self):
        self.cart_link.click()

    def start_checkout(self):
        self.checkout_btn.click()
        
    def fill_personal_info(self, first_name, last_name, postal_code):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_btn.click()

    def finish_order(self):
        self.finish_btn.click()