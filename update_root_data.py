import json
import csv
import os

def update_root_data():
    with open('site/data.json', 'r') as f:
        data = json.load(f)

    # Write occupations.json
    with open('occupations.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    # Write occupations.csv
    # Fields: title, slug, pay, jobs, outlook, education, exposure, exposure_rationale
    if not data:
        return
        
    keys = ['title', 'slug', 'pay', 'jobs', 'outlook', 'education', 'exposure', 'exposure_rationale']
    
    with open('occupations.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for d in data:
            row = {}
            for k in keys:
                row[k] = d.get(k, '')
            writer.writerow(row)

if __name__ == "__main__":
    update_root_data()
