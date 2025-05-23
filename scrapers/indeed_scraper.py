import requests
from bs4 import BeautifulSoup
from filters import is_valid_job

def scrape_indeed(query="marketing", location="Madrid", pages=3):
    jobs = []
    headers = {"User-Agent": "Mozilla/5.0"}
    base_url = "https://es.indeed.com/jobs"
    for page in range(pages):
        params = {"q": query, "l": location, "start": page * 10}
        resp = requests.get(base_url, params=params, headers=headers)
        print(f"[INDEED] Page {page} - Status {resp.status_code}")
        if resp.status_code != 200:
            break
        soup = BeautifulSoup(resp.text, "html.parser")
        cards = soup.select("a.tapItem")
        print(f"[INDEED] Page {page} - Cards found: {len(cards)}")
        for card in cards:
            title = card.select_one("h2.jobTitle").get_text(strip=True)
            company = card.select_one(".companyName").get_text(strip=True) 
            loc = card.select_one(".companyLocation").get_text(strip=True)
            summary = card.select_one(".job-snippet").get_text(" ", strip=True)
            url = "https://es.indeed.com" + card.get("href")
            combined = f"{title} {summary}"
            if is_valid_job(combined):
                jobs.append({
                    "source": "Indeed",
                    "title": title,
                    "company": company,
                    "location": loc,
                    "summary": summary,
                    "url": url
                })
    return jobs