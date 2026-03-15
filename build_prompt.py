import json

def format_inr(n):
    if n >= 10000000:  # 1 Crore
        return f"₹{n/10000000:.2f}Cr"
    if n >= 100000:    # 1 Lakh
        return f"₹{n/100000:.1f}L"
    return f"₹{n:,.0f}"

def format_jobs(n):
    if n >= 1000000:
        return f"{n/1000000:.1f}M"
    if n >= 1000:
        return f"{int(n/1000)}K"
    return f"{n:,}"

def generate_markdown():
    with open('site/data.json', 'r') as f:
        data = json.load(f)

    # Sort data by exposure desc, then jobs desc
    data.sort(key=lambda x: (x.get('exposure', 0), x.get('jobs', 0)), reverse=True)

    total_jobs = sum(d.get('jobs', 0) for d in data)
    weighted_exposure = sum(d.get('exposure', 0) * d.get('jobs', 0) for d in data) / total_jobs

    md = [
        "# AI Exposure of the Indian Tech Job Market",
        "",
        "This document contains structured data on 22 core occupations within the Indian Technology & Data Science sector. ",
        "Workforce sizes are anchored to NASSCOM 2025-26 estimates, and salaries sourced from Indian job platforms. ",
        "Each role is scored for AI exposure on a 0-10 scale by an LLM (Gemini Flash).",
        "",
        "Live visualization: https://insrawat.github.io/jobs-Indian-Tech-Market",
        "GitHub: https://github.com/iNSRawat/jobs-Indian-Tech-Market",
        "",
        "## Aggregate statistics",
        "",
        f"- Total tech occupations: {len(data)}",
        f"- Total jobs: {format_jobs(total_jobs)}",
        f"- Job-weighted average AI exposure: {weighted_exposure:.1f}/10",
        "",
        "## All Occupations",
        "",
        "Sorted by AI exposure (descending), then by number of jobs (descending).",
        ""
    ]

    current_exposure = -1
    for i, d in enumerate(data, 1):
        if d['exposure'] != current_exposure:
            current_exposure = d['exposure']
            md.append(f"### Exposure {current_exposure}/10")
            md.append("")
            md.append("| # | Occupation | Pay | Jobs | Outlook | Education | Rationale |")
            md.append("|---|-----------|-----|------|---------|-----------|-----------|")
        
        pay_str = format_inr(d.get('pay', 0))
        jobs_str = format_jobs(d.get('jobs', 0))
        outlook_str = f"+{d.get('outlook', 0)}%" if d.get('outlook', 0) > 0 else f"{d.get('outlook', 0)}%"
        
        row = f"| {i} | {d['title']} | {pay_str} | {jobs_str} | {outlook_str} | {d['education']} | {d['exposure_rationale']} |"
        md.append(row)

    with open('prompt.md', 'w', encoding='utf-8') as f:
        f.write("\n".join(md))

if __name__ == "__main__":
    generate_markdown()
