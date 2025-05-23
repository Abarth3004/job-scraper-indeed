from scrapers.indeed_scraper import scrape_indeed
from export_excel import export_jobs_to_excel

def main():
    all_jobs = scrape_indeed(query="marketing OR communication OR digital media OR digital marketing", location="Madrid", pages=5)
    export_jobs_to_excel(all_jobs)

if __name__ == "__main__":
    main()