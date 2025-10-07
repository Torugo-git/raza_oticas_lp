from playwright.sync_api import sync_playwright, expect
import os
import time

def run_verification():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # 1. Verify the updated index.html page
        index_path = "file://" + os.path.abspath("home/ubuntu/index.html")
        page.goto(index_path)

        # Check carousel functionality
        carousel = page.locator(".carousel-container")
        expect(carousel).to_be_visible()

        # Give the JS time to initialize
        time.sleep(1)

        # Check initial state (first slide)
        first_slide = page.locator(".carousel-slide").nth(0)
        expect(first_slide).to_be_visible()

        # Check that the next button works
        page.click(".next", force=True)
        time.sleep(1.6) # Wait for animation (1.5s) + buffer
        second_slide = page.locator(".carousel-slide").nth(1)
        expect(second_slide).to_be_visible()
        expect(first_slide).not_to_be_visible()

        # Check that the prev button works
        page.click(".prev", force=True)
        time.sleep(1.6) # Wait for animation
        expect(first_slide).to_be_visible()
        expect(second_slide).not_to_be_visible()

        # Check dots container style
        dots_container = page.locator(".dots-container")
        expect(dots_container).to_have_css("background", "rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box") # More specific check for transparent

        page.screenshot(path="jules-scratch/verification/index_page_carousel_fixed.png")

        # 2. Re-verify the franqueado.html page
        franqueado_path = "file://" + os.path.abspath("home/ubuntu/franqueado.html")
        page.goto(franqueado_path)

        video_banner = page.locator("section.hero video.hero-background-video")
        expect(video_banner).to_be_visible()

        page.screenshot(path="jules-scratch/verification/franqueado_page_final_check.png")

        browser.close()

run_verification()
