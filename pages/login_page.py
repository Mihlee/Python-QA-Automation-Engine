class LoginPage:
    def __init__(self, page):
        self.page = page
        # Store all the locators here
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")

    def navigate(self):
        # Action: Go to the page
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        # Action: Fill credentials and click submit
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()