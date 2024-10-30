from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import time

def login_and_access_menu(browser_name="chromium"):
  
    
    urls = [
        "https://www.douglas.de/de/c/parfum/01?q=:relevance:flags:discountFlag",
        "https://www.douglas.de/de/c/parfum/01?q=:relevance:flags:discountFlag:flags:computedNewFlag",
        "https://www.douglas.de/de/c/parfum/01?q=:relevance:flags:discountFlag:flags:computedNewFlag:flags:computedLimited"
    ]
    
    with sync_playwright() as p:
       
        if browser_name == "msedge":
            browser = p.chromium.launch(channel="msedge", headless=False, args=["--start-maximized"])
        else:
            browser = p.chromium.launch(headless=False, args=["--start-maximized"])

        
        context = browser.new_context(
            viewport={"width": 1280, "height": 800},
            record_video_dir="videos/",
            record_video_size={"width": 1280, "height": 800} 
        )
        
       
        page = context.new_page()

        
        page.goto("https://www.douglas.de/de")
        page.wait_for_load_state('networkidle')
        
      
        try:
            page.get_by_test_id("uc-accept-all-button").click(timeout=50000)
            print("Cookie acceptance click successful!")
        except TimeoutError:
            print("Cookie button not found within the timeout period.")
        
        
        page.get_by_role("link", name="PARFUM", exact=True).click()
        page.wait_for_load_state('networkidle')

        
        for url in urls:
            page.goto(url)
            page.wait_for_timeout(10000)  
            print(f"Loaded URL: {url}")

        
        context.close()
        browser.close()

if __name__ == "__main__":
    # Change "chromium" to "msedge" 
    login_and_access_menu(browser_name="chromium")
