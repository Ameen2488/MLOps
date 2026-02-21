from fastmcp import FastMCP
from linkedin_api import Linkedin
import os

# Initialize FastMCP server
mcp = FastMCP("LinkedIn")

def get_linkedin_client():
    """Helper to get authenticated LinkedIn client"""
    cookie = os.environ.get("LINKEDIN_COOKIE")
    email = os.environ.get("LINKEDIN_EMAIL")
    password = os.environ.get("LINKEDIN_PASSWORD")

    if cookie:
        from requests.cookies import cookiejar_from_dict
        cookies = {'li_at': cookie}
        jsessionid = os.environ.get("LINKEDIN_JSESSIONID")
        if jsessionid:
            cookies['JSESSIONID'] = jsessionid
            cookies['jsessionid'] = jsessionid # Try both just in case
        
        return Linkedin("dummy", "dummy", cookies=cookiejar_from_dict(cookies))

    if not email or not password:
        raise ValueError("Either LINKEDIN_COOKIE or (LINKEDIN_EMAIL and LINKEDIN_PASSWORD) environment variables must be set")
    
    return Linkedin(email, password)

@mcp.tool()
def get_profile(public_id: str) -> dict:
    """Get a LinkedIn profile by public ID (the part after /in/ in the URL)."""
    try:
        api = get_linkedin_client()
        profile = api.get_profile(public_id)
        return profile
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def search_jobs(keywords: str, location_name: str = "United States", limit: int = 5) -> list:
    """Search for jobs on LinkedIn."""
    try:
        api = get_linkedin_client()
        jobs = api.search_jobs(keywords=keywords, location_name=location_name, limit=limit)
        return jobs
    except Exception as e:
        return [{"error": str(e)}]

@mcp.tool()
def get_company(public_id: str) -> dict:
    """Get a LinkedIn company profile by public ID."""
    try:
        api = get_linkedin_client()
        company = api.get_company(public_id)
        return company
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    mcp.run()
