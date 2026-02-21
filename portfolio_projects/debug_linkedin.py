from linkedin_api import Linkedin
import traceback
import sys

# The cookie provided by the user
cookie = "AQEDAQXs8LABapz2AAABmC0pZ-MAAAGcdfLyT04Ad_9CWahTFOSz8AlGcCXaNsCG8i7zH7J3sTHt1XFXqyoUz6ieDvD1vmN5_mYsoLnv6goOEil4Zy8dGiuGpND-AGIcUDxIfoKaNKH6q2ZYqZJHTMew"
jsessionid = "ajax:9061117612665943071"

try:
    print(f"Python executable: {sys.executable}")
    print("Attempting login with cookie...")
    # Passing the cookie to the Linkedin constructor
    import requests
    cookies = {'li_at': cookie, 'JSESSIONID': jsessionid, 'jsessionid': jsessionid}
    # linkedin_api internally uses a requests session. If we pass a dict of cookies to the constructor,
    # it *should* work if the library handles it, but let's see how linkedin_api initiates.
    # It seems to do `self.client = Client(...)` and Client does `self.session = requests.Session(); self.session.cookies = ...`
    # if we pass cookies to Linkedin(), it passes them to Client(). 
    # Client() init: `self.session.cookies.update(cookies)` if cookies is dict.
    # The error "extract_cookies_to_jar" happens when a request is made and it tries to update the jar.
    # It implies self.session.cookies was replaced by a dict instead of updated/merged into a requestsCookieJar?
    # Let's try passing a CookieJar explicitly to be safe, or just relying on the library to handle dicts if we don't mess it up.
    # Wait, the traceback says `extract_cookies_to_jar(self.cookies, ...)` where self.cookies is the session.cookies.
    # If session.cookies is a dict, it fails. It must be a CookieJar.
    # So we should ensure we are not overwriting session.cookies with a dict.
    
    # Actually, the library code I saw in the traceback: `self.client._set_session_cookies(cookies)` might be the key.
    # Let's assume we need to modify the library usage or our code.
    
    # In `linkedin_server.py`, I am doing:
    # return Linkedin("dummy", "dummy", cookies=cookies)
    
    # If I look at `linkedin_api` source code (or assume):
    # It likely does `self.client = Client(..., cookies=cookies)`
    # And Client likely does `self.session.cookies = cookies` if not careful? 
    # Or `self.session.cookies.update(cookies)`.
    
    # The traceback:
    # File "requests\sessions.py", line 718, in send
    # extract_cookies_to_jar(self.cookies, request, r.raw)
    
    # This means `self.cookies` (the session cookies) is a dict.
    # Requests session.cookies IS a RequestsCookieJar by default.
    # If some code did `session.cookies = {...}`, then it becomes a dict and breaks `extract_cookies_to_jar`.
    
    # Conclusion: linkedin_api might be overwriting the session cookies with the passed dict?
    # No, I should check if I can just pass the dict.
    # If I pass a dict to `requests.Session().cookies.update()`, it works.
    
    # Let's try converting to a CookieJar before passing it to Linkedin constructor.
    from requests.cookies import cookiejar_from_dict
    jar = cookiejar_from_dict(cookies)
    api = Linkedin("dummy", "dummy", cookies=jar)
    print("Login object created successfully.")
    
    print("Attempting search_jobs...")
    jobs = api.search_jobs(keywords="Time Series", limit=1)
    print(f"Success! Found {len(jobs)} jobs.")
    
except Exception:
    print("An error occurred:")
    traceback.print_exc()
