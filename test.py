from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import time

def login_and_access_menu():
  
    # urls = [
    #     "https://www.douglas.de/de/c/parfum/01?q=:relevance:flags:discountFlag",
    #     "https://www.douglas.de/de/c/parfum/01?q=:relevance:flags:discountFlag:flags:computedNewFlag",
    #     "https://www.douglas.de/de/c/parfum/01?q=:relevance:flags:discountFlag:flags:computedNewFlag:flags:computedLimited"
    # ]
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        
        context = browser.new_context(no_viewport=True)
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        
        page = context.new_page()

        # Login
        page.goto("https://www.douglas.de/de")
      
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

        # for url in urls:
        #     page.goto(url)
        #     page.wait_for_timeout(50000)
            # page.wait_for_load_state('networkidle')
            # print(f"Loaded URL: {url}")

        try:
          page.get_by_test_id("flags").click()
          sale_checkbox = page.get_by_role("checkbox", name="Sale")
          sale_checkbox.wait_for(state="visible", timeout=50000)
          sale_checkbox.check()
            
        except PlaywrightTimeoutError as e:
          print(f"An element failed to load or become interactable: {e}")

        # page.wait_for_load_state('networkidle')

        try:
          
          page.get_by_test_id("flags").click(timeout=20000)
          neu_checkbox = page.get_by_role("checkbox", name="NEU")
          neu_checkbox.wait_for(state="visible", timeout=10000)
          neu_checkbox.check()
          
        except PlaywrightTimeoutError as e:
          print((f"An element failed to load or become interactable: {e}"))
          
        # page.wait_for_load_state('networkidle')
  
          
        try:
        
          page.get_by_test_id("flags").click(timeout=20000)
          limited_checkbox = page.get_by_role("checkbox", name="Limitiert")
          limited_checkbox.wait_for(state="visible", timeout=10000)
          limited_checkbox.check()
          
        except PlaywrightTimeoutError as e:
          print((f"An element failed to load or become interactable: {e}"))
          
        page.wait_for_load_state('networkidle')

        
        page.screenshot(path="Perfum1.png", full_page=True)
        
        timestamp = int(time.time())
        trace_filename = f"trace_{timestamp}.zip"
        context.tracing.stop(path=trace_filename)
        # context.tracing.stop(path = "trace_1.zip")
        browser.close()

if __name__ == "__main__":
    login_and_access_menu()