from playwright.sync_api import sync_playwright, Page, expect
import os

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    # Get the absolute path to the HTML file
    file_path = os.path.abspath('unidades/cabo-frio/index.html')

    # Navigate to the local HTML file
    page.goto(f'file://{file_path}')

    # Locate the email link
    email_link = page.get_by_role("link", name="dev@razaoticas.com")

    # Assert that the link is visible and contains the correct email
    expect(email_link).to_be_visible()
    expect(email_link).to_have_text("dev@razaoticas.com")

    # Take a screenshot for visual verification
    page.screenshot(path="jules-scratch/verification/verification.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
