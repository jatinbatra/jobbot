# job_bot.py
import os
import requests
import time

def apply_to_jobs():
    # Your application details
    my_details = {
        "name": os.environ.get('NAME'),
        "email": os.environ.get('EMAIL'),
        "resume_url": os.environ.get('RESUME_URL')
    }
    
    # Greenhouse API endpoint
    url = "https://harvest.greenhouse.io/v1/jobs"
    api_key = os.environ.get('GREENHOUSE_API_KEY')
    
    # Get jobs
    response = requests.get(url, auth=(api_key, ''))
    
    if response.status_code == 200:
        jobs = response.json()
        
        # Filter for PM jobs
        pm_jobs = [job for job in jobs if 'product' in job['title'].lower()]
        
        print(f"Found {len(pm_jobs)} Product Management jobs")
        
        # Apply to each job
        for job in pm_jobs:
            print(f"Applying to: {job['title']}")
            # Your application logic here
            time.sleep(1)  # Wait between applications

while True:
    apply_to_jobs()
    time.sleep(3600)  # Run every hour
