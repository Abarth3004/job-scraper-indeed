import pandas as pd

def export_jobs_to_excel(jobs):
    df = pd.DataFrame(jobs)
    df.to_excel("jobs_madrid_filtered.xlsx", index=False)
    print("✅ Generated jobs_madrid_filtered.xlsx with", len(jobs), "rows")