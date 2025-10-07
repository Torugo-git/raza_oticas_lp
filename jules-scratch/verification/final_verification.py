from playwright.sync_api import sync_playwright, expect
import os
import time

def run_verification():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # 1. Verify the fixed index.html page
        index_path = "file://" + os.path.abspath("home/ubuntu/index.html")
        page.goto(index_path)

        # Give the JS time to initialize
        time.sleep(1)

        # Check carousel functionality
        first_slide = page.locator(".carousel-slide").nth(0)
        second_slide = page.locator(".carousel-slide").nth(1)

        # Initial state
        expect(first_slide).to_be_visible()

        # Click next
        page.click(".next", force=True)
        time.sleep(0.5) # Wait for transition
        expect(second_slide).to_be_visible()

        # Click prev
        page.click(".prev", force=True)
        time.sleep(0.5)
        expect(first_slide).to_be_visible()

        # Click dot
        page.locator(".dot").nth(2).click(force=True)
        time.sleep(0.5)
        expect(page.locator(".carousel-slide").nth(2)).to_be_visible()

        # Check dots container style
        dots_container = page.locator(".dots-container")
        style = dots_container.evaluate("element => window.getComputedStyle(element).backgroundColor")
        assert style == "rgba(0, 0, 0, 0)"

        page.screenshot(path="jules-scratch/verification/index_page_final_fix.png")

        # 2. Re-verify the franqueado.html page
        franqueado_path = "file://" + os.path.abspath("home/ubuntu/franqueado.html")
        page.goto(franqueado_path)

        video_banner = page.locator("section.hero video.hero-background-video")
        expect(video_banner).to_be_visible()

        page.screenshot(path="jules-scratch/verification/franqueado_page_final_fix.png")

        browser.close()

run_verification()
