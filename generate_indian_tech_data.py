import json

occupations = [
    # SOFTWARE ENGINEERING
    {
        "title": "Software Engineers (General)",
        "slug": "software-engineers",
        "category": "software-engineering",
        "pay": 800000,
        "jobs": 1500000,
        "outlook": 12,
        "outlook_desc": "Much faster than average",
        "education": "Bachelor's degree",
        "exposure": 8,
        "exposure_rationale": "Writing and testing code is entirely digital and highly exposed to AI coding assistants. Routine programming tasks are rapidly moving toward automation, though system design and logic architecture still require human oversight."
    },
    {
        "title": "Frontend Developers",
        "slug": "frontend-developers",
        "category": "software-engineering",
        "pay": 700000,
        "jobs": 350000,
        "outlook": 10,
        "outlook_desc": "Faster than average",
        "education": "Bachelor's degree",
        "exposure": 8,
        "exposure_rationale": "Generative AI models are increasingly capable of translating design mockups directly into functional frontend code. Routine UI component creation is highly susceptible to automation."
    },
    {
        "title": "Backend Developers",
        "slug": "backend-developers",
        "category": "software-engineering",
        "pay": 900000,
        "jobs": 450000,
        "outlook": 12,
        "outlook_desc": "Much faster than average",
        "education": "Bachelor's degree",
        "exposure": 8,
        "exposure_rationale": "Backend logic, API design, and database queries are completely digital. AI tools can rapidly generate boilerplate code, optimize SQL queries, and assist in debugging complex server-side issues."
    },
    {
        "title": "Full Stack Developers",
        "slug": "full-stack-developers",
        "category": "software-engineering",
        "pay": 1000000,
        "jobs": 350000,
        "outlook": 15,
        "outlook_desc": "Much faster than average",
        "education": "Bachelor's degree",
        "exposure": 8,
        "exposure_rationale": "While full stack requires cross-domain knowledge, both frontend and backend tasks are highly exposed to AI productivity gains, reducing the overall time needed to build end-to-end applications."
    },
    {
        "title": "Mobile App Developers",
        "slug": "mobile-app-developers",
        "category": "software-engineering",
        "pay": 800000,
        "jobs": 200000,
        "outlook": 10,
        "outlook_desc": "Faster than average",
        "education": "Bachelor's degree",
        "exposure": 8,
        "exposure_rationale": "App development frameworks (like React Native and Flutter) are well-understood by modern LLMs, allowing for rapid generation of mobile UIs and business logic."
    },
    {
        "title": "Quality Assurance (QA) Engineers",
        "slug": "qa-engineers",
        "category": "software-engineering",
        "pay": 600000,
        "jobs": 400000,
        "outlook": 8,
        "outlook_desc": "Faster than average",
        "education": "Bachelor's degree",
        "exposure": 9,
        "exposure_rationale": "Writing test cases, automating UI tests, and identifying edge cases are areas where AI test generation tools excel. Manual testing is being rapidly replaced by AI-driven automated test suites."
    },
    
    # DATA SCIENCE & AI
    {
        "title": "Data Scientists",
        "slug": "data-scientists",
        "category": "data-science",
        "pay": 1200000,
        "jobs": 150000,
        "outlook": 28,
        "outlook_desc": "Much faster than average",
        "education": "Bachelor's degree or higher",
        "exposure": 9,
        "exposure_rationale": "Data science is a fully digital occupation centered on statistical modeling and data analysis, areas where AI is rapidly achieving parity. AI can automate significant portions of the data pipeline."
    },
    {
        "title": "Machine Learning Engineers",
        "slug": "machine-learning-engineers",
        "category": "data-science",
        "pay": 1500000,
        "jobs": 80000,
        "outlook": 35,
        "outlook_desc": "Much faster than average",
        "education": "Master's degree preferred",
        "exposure": 8,
        "exposure_rationale": "While ML Engineers literally build AI, the task of implementing standard model architectures and tuning hyperparameters is increasingly automated by AutoML and code generation models."
    },
    {
        "title": "Data Analysts",
        "slug": "data-analysts",
        "category": "data-science",
        "pay": 650000,
        "jobs": 250000,
        "outlook": 18,
        "outlook_desc": "Much faster than average",
        "education": "Bachelor's degree",
        "exposure": 9,
        "exposure_rationale": "The core tasks of querying data, generating reports, and building dashboards are highly susceptible to AI automation. LLMs can instantly convert natural language questions into complex SQL and visual charts."
    },
    {
        "title": "Data Engineers",
        "slug": "data-engineers",
        "category": "data-science",
        "pay": 1100000,
        "jobs": 100000,
        "outlook": 22,
        "outlook_desc": "Much faster than average",
        "education": "Bachelor's degree",
        "exposure": 8,
        "exposure_rationale": "Building ETL pipelines and managing data infrastructure is digital work. AI can generate complex data transformation scripts and optimize database configurations, increasing engineer productivity."
    },
    {
        "title": "AI Researchers",
        "slug": "ai-researchers",
        "category": "data-science",
        "pay": 1800000,
        "jobs": 20000,
        "outlook": 25,
        "outlook_desc": "Much faster than average",
        "education": "Ph.D or Master's degree",
        "exposure": 7,
        "exposure_rationale": "While pushing the boundaries of scientific knowledge requires profound human creativity, the literature review, code implementation, and experiment tracking phases are heavily assisted by AI."
    },

    # CLOUD & DEVOPS
    {
        "title": "DevOps Engineers",
        "slug": "devops-engineers",
        "category": "cloud-devops",
        "pay": 1100000,
        "jobs": 150000,
        "outlook": 20,
        "outlook_desc": "Much faster than average",
        "education": "Bachelor's degree",
        "exposure": 8,
        "exposure_rationale": "Infrastructure as Code (IaC) and CI/CD pipelines are inherently digital. AI can generate configuration files (like Terraform/Kubernetes) and automatically resolve deployment errors."
    },
    {
        "title": "Cloud Architects",
        "slug": "cloud-architects",
        "category": "cloud-devops",
        "pay": 2000000,
        "jobs": 60000,
        "outlook": 15,
        "outlook_desc": "Much faster than average",
        "education": "Bachelor's degree",
        "exposure": 7,
        "exposure_rationale": "Designing resilient cloud architectures requires high-level strategic thinking, but AI is quickly becoming capable of analyzing system requirements and proposing optimized cloud topologies."
    },
    {
        "title": "Cybersecurity Analysts",
        "slug": "cybersecurity-analysts",
        "category": "cloud-devops",
        "pay": 850000,
        "jobs": 120000,
        "outlook": 32,
        "outlook_desc": "Much faster than average",
        "education": "Bachelor's degree",
        "exposure": 8,
        "exposure_rationale": "Monitoring network traffic and analyzing threat logs is heavily data-driven. AI excels at pattern recognition for anomaly detection and can automate incident response playbooks."
    },
    {
        "title": "Network Engineers",
        "slug": "network-engineers",
        "category": "cloud-devops",
        "pay": 600000,
        "jobs": 200000,
        "outlook": 6,
        "outlook_desc": "Faster than average",
        "education": "Bachelor's degree",
        "exposure": 7,
        "exposure_rationale": "Network design and configuration is largely digital and automatable via Software Defined Networking (SDN). However, physical hardware installation and troubleshooting provide some buffer."
    },
    {
        "title": "Database Administrators",
        "slug": "database-administrators",
        "category": "cloud-devops",
        "pay": 800000,
        "jobs": 90000,
        "outlook": 4,
        "outlook_desc": "As fast as average",
        "education": "Bachelor's degree",
        "exposure": 9,
        "exposure_rationale": "AI can already automate routine DBA tasks like performance tuning, index optimization, and security monitoring, leading to massive productivity gains and reducing the need for manual oversight."
    },

    # PRODUCT & DESIGN
    {
        "title": "Product Managers (Tech)",
        "slug": "product-managers",
        "category": "product-design",
        "pay": 1600000,
        "jobs": 150000,
        "outlook": 10,
        "outlook_desc": "Faster than average",
        "education": "Bachelor's or Master's degree",
        "exposure": 6,
        "exposure_rationale": "While AI can draft PRDs, analyze user data, and summarize meetings, the core role demands intense cross-functional collaboration, stakeholder alignment, and complex human empathy that AI cannot replace."
    },
    {
        "title": "UI/UX Designers",
        "slug": "ui-ux-designers",
        "category": "product-design",
        "pay": 750000,
        "jobs": 150000,
        "outlook": 8,
        "outlook_desc": "Faster than average",
        "education": "Bachelor's degree",
        "exposure": 8,
        "exposure_rationale": "Generative AI is rapidly advancing in visual design, capable of generating entire user interfaces, icons, and layout options in seconds, heavily altering the digital design workflow."
    },
    {
        "title": "Systems Analysts",
        "slug": "systems-analysts",
        "category": "product-design",
        "pay": 950000,
        "jobs": 250000,
        "outlook": 9,
        "outlook_desc": "Much faster than average",
        "education": "Bachelor's degree",
        "exposure": 8,
        "exposure_rationale": "Analyzing technical requirements and modeling systems can be performed entirely on a computer. AI is highly capable of generating system diagrams and technical documentation."
    },
    {
        "title": "IT Project Managers",
        "slug": "it-project-managers",
        "category": "product-design",
        "pay": 1400000,
        "jobs": 250000,
        "outlook": 8,
        "outlook_desc": "Faster than average",
        "education": "Bachelor's degree",
        "exposure": 6,
        "exposure_rationale": "Project management involves risk assessment, resource allocation, and timeline tracking—tasks AI can optimize. The human element of motivating teams and handling interpersonal conflicts provides a strong buffer."
    },
    {
        "title": "Tech Sales & Solutions Engineers",
        "slug": "tech-sales",
        "category": "product-design",
        "pay": 1000000,
        "jobs": 150000,
        "outlook": 12,
        "outlook_desc": "Much faster than average",
        "education": "Bachelor's degree",
        "exposure": 6,
        "exposure_rationale": "While AI can generate sales pitches, analyze client data, and provide technical answers, B2B enterprise sales remain heavily dependent on relationship-building and human trust."
    },
    
    # IT SUPPORT
    {
        "title": "IT Support Specialists",
        "slug": "it-support-specialists",
        "category": "product-design",
        "pay": 450000,
        "jobs": 350000,
        "outlook": -2,
        "outlook_desc": "Decline",
        "education": "Postsecondary nondegree award",
        "exposure": 9,
        "exposure_rationale": "Diagnosing software issues and guiding users through digital workflows are highly susceptible to AI chatbots and automated troubleshooting. Physical hardware setup provides a small residual need for human staff."
    }
]

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(occupations, f, indent=2)

print("Data written to data.json successfully.")
