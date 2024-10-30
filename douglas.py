from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import time

def login_and_access_menu():
  
    urls = [
        "https://www.douglas.de/de/c/parfum/01?q=:relevance:flags:discountFlag",
        "https://www.douglas.de/de/c/parfum/01?q=:relevance:flags:discountFlag:flags:computedNewFlag",
        "https://www.douglas.de/de/c/parfum/01?q=:relevance:flags:discountFlag:flags:computedNewFlag:flags:computedLimited"
    ]
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        # browser = p.chromium.launch(channel="msedge", headless=False, args=["--start-maximized"])
        
        context = browser.new_context(viewport={"width": 1280, "height": 800}, record_video_dir="videos/")
        # context.tracing.start(screenshots=True, snapshots=True, sources=True)

        page = context.new_page()

        # Login
        page.goto("https://www.douglas.de/de", timeout=60000)
      
        page.wait_for_load_state('networkidle')

     
        try:
        
          page.get_by_test_id("uc-accept-all-button").click(timeout=50000)
          print("Click successful!")
        except TimeoutError:
          print("Click failed: Element not found within the timeout period.")
          
        # page.screenshot(path="login.png", full_page=True)
        page.get_by_role("link", name="PARFUM", exact=True).click()
        # page.goto("https://www.douglas.de/de/c/parfum/01")
        
        page.wait_for_load_state('networkidle')

        for url in urls:
            page.goto(url)
            page.wait_for_timeout(50000)
            # page.wait_for_load_state('networkidle')
            print(f"Loaded URL: {url}")

        # context.tracing.stop(path = "trace24.zip")
        context.close()
        browser.close()

if __name__ == "__main__":
    login_and_access_menu()