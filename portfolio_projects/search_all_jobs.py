from linkedin_api import Linkedin
import os
import json
from requests.cookies import cookiejar_from_dict

# Hardcoded credentials/cookies from the context
COOKIE_LI_AT = "AQEDAQXs8LABapz2AAABmC0pZ-MAAAGcdfLyT04Ad_9CWahTFOSz8AlGcCXaNsCG8i7zH7J3sTHt1XFXqyoUz6ieDvD1vmN5_mYsoLnv6goOEil4Zy8dGiuGpND-AGIcUDxIfoKaNKH6q2ZYqZJHTMew"
COOKIE_JSESSIONID = "ajax:9061117612665943071"

def debug_logic():
    cookies = {'li_at': COOKIE_LI_AT, 'JSESSIONID': COOKIE_JSESSIONID, 'jsessionid': COOKIE_JSESSIONID}
    api = Linkedin("dummy", "dummy", cookies=cookiejar_from_dict(cookies))
    
    # Test 1: Get Profile
    print("Test 1: Fetching profile 'williamhgates'...")
    try:
        profile = api.get_profile("williamhgates")
        print(f"Profile found: {profile.get('firstName')} {profile.get('lastName')}")
    except Exception as e:
        print(f"Profile fetch failed: {e}")

    # Test 2: Generic Search
    print("Test 2: Searching 'Python' jobs in 'United States'...")
    try:
        jobs = api.search_jobs("Python", location_name="United States", limit=1)
        print(f"Jobs found: {len(jobs)}")
        if jobs:
            print(jobs[0])
    except Exception as e:
        print(f"Search failed: {e}")

if __name__ == "__main__":
    debug_logic()
