import os
# Fix for "missing $HOME" error
if "HOME" not in os.environ:
    os.environ["HOME"] = os.path.expanduser("~")

import json
import time
from playwright.sync_api import sync_playwright

COOKIE_LI_AT = "AQEDAQXs8LABapz2AAABmC0pZ-MAAAGcdfLyT04Ad_9CWahTFOSz8AlGcCXaNsCG8i7zH7J3sTHt1XFXqyoUz6ieDvD1vmN5_mYsoLnv6goOEil4Zy8dGiuGpND-AGIcUDxIfoKaNKH6q2ZYqZJHTMew"
COOKIE_JSESSIONID = "ajax:9061117612665943071"

def scrape_linkedin():
    locations = ["India", "United Arab Emirates", "Saudi Arabia", "Germany"]
    keyword = "Time Series"
    results = {}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
        
        # Add cookies to context
        context.add_cookies([
            {"name": "li_at", "value": COOKIE_LI_AT, "domain": ".linkedin.com", "path": "/"},
            {"name": "JSESSIONID", "value": COOKIE_JSESSIONID, "domain": ".linkedin.com", "path": "/"},
        ])

        page = context.new_page()

        for loc in locations:
            print(f"Scraping {loc}...")
            url = f"https://www.linkedin.com/jobs/search/?keywords={keyword}&location={loc}"
            try:
                page.goto(url, timeout=30000)
                # content = page.content()
                # with open(f"debug_{loc}.html", "w", encoding="utf-8") as f: f.write(content)
                
                # Check for job cards
                # Selectors change often, but typically: .job-card-container or .jobs-search-results__list-item
                # Or just generic extraction
                
                # Wait for at least one job card or "No jobs found"
                try:
                    page.wait_for_selector(".job-card-container, .jobs-search__results-list, section.results-list", timeout=10000)
                except:
                    print(f"Timeout waiting for results in {loc}")

                # Extract
                job_elements = page.query_selector_all(".job-card-container")
                if not job_elements:
                     # Try alternative selectors for guest view or different layouts
                     job_elements = page.query_selector_all("li")
                
                job_list = []
                for el in job_elements[:5]:
                    title_el = el.query_selector(".job-card-list__title, h3, .base-search-card__title")
                    company_el = el.query_selector(".job-card-container__primary-description, h4, .base-search-card__subtitle")
                    loc_el = el.query_selector(".job-card-container__metadata-item, .job-search-card__location")
                    link_el = el.query_selector("a.job-card-list__title, a.base-card__full-link")
                    
                    if title_el:
                        title = title_el.inner_text().strip()
                        company = company_el.inner_text().strip() if company_el else "Unknown"
                        location = loc_el.inner_text().strip() if loc_el else "Unknown"
                        link = link_el.get_attribute("href") if link_el else ""
                        
                        if title:
                            job_list.append({
                                "title": title,
                                "company": company,
                                "location": location,
                                "link": link
                            })
                
                results[loc] = job_list
                print(f"Found {len(job_list)} jobs in {loc}")
                
            except Exception as e:
                print(f"Error scraping {loc}: {e}")
                results[loc] = []
                
            time.sleep(2) # be nice

        browser.close()
        
    # Save results
    with open("jobs_data.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
        
    print("Scraping complete. Results saved to jobs_data.json")

if __name__ == "__main__":
    scrape_linkedin()
