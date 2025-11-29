import json

# Configuration
OUTPUT_FILE = 'src/data/saas.json'

# Software Categories with Alternatives
SOFTWARE_ALTERNATIVES = {
    "Design": {
        "Photoshop": ["Affinity Photo", "GIMP", "Pixlr", "Photopea", "Canva"],
        "Illustrator": ["Affinity Designer", "Inkscape", "Vectornator", "CorelDRAW", "Sketch"],
        "Canva": ["Adobe Express", "Crello", "VistaCreate", "PicMonkey", "Snappa"],
        "Figma": ["Adobe XD", "Sketch", "InVision", "Framer", "Penpot"]
    },
    "Business": {
        "Salesforce": ["HubSpot CRM", "Pipedrive", "Zoho CRM", "Microsoft Dynamics", "Freshsales"],
        "HubSpot": ["Salesforce", "ActiveCampaign", "Marketo", "Pardot", "Keap"],
        "QuickBooks": ["Xero", "FreshBooks", "Wave", "Zoho Books", "Sage"],
        "Microsoft Office": ["Google Workspace", "LibreOffice", "WPS Office", "Zoho Workplace", "OnlyOffice"],
        "Slack": ["Microsoft Teams", "Discord", "Mattermost", "Rocket.Chat", "Chanty"],
        "Asana": ["Monday.com", "ClickUp", "Trello", "Notion", "Basecamp"],
        "Zoom": ["Google Meet", "Microsoft Teams", "Webex", "GoToMeeting", "Skype"]
    },
    "Development": {
        "GitHub": ["GitLab", "Bitbucket", "SourceForge", "Gitea", "Azure DevOps"],
        "VS Code": ["Sublime Text", "Atom", "WebStorm", "Vim", "Notepad++"],
        "Postman": ["Insomnia", "Paw", "HTTPie", "Thunder Client", "REST Client"],
        "Jira": ["Linear", "Asana", "Monday.com", "ClickUp", "Trello"],
        "Docker": ["Podman", "LXC", "Kubernetes", "containerd", "rkt"]
    },
    "Marketing": {
        "Mailchimp": ["ConvertKit", "ActiveCampaign", "Sendinblue", "GetResponse", "AWeber"],
        "Semrush": ["Ahrefs", "Moz Pro", "Ubersuggest", "SpyFu", "Mangools"],
        "Ahrefs": ["Semrush", "Moz Pro", "Majestic", "SpyFu", "SE Ranking"],
        "Hootsuite": ["Buffer", "Sprout Social", "Later", "SocialBee", "CoSchedule"],
        "Google Analytics": ["Matomo", "Plausible", "Fathom", "Clicky", "Adobe Analytics"]
    }
}

def generate_alternatives():
    alternatives = []
    print("🚀 Generating SaaS Alternative Pages...")

    for category, software_dict in SOFTWARE_ALTERNATIVES.items():
        category_count = 0
        
        for software, competitors in software_dict.items():
            slug = f"alternatives-to-{software.lower().replace(' ', '-')}"
            title = f"Top 5 Alternatives to {software} in 2025"
            
            # Pick top competitor for content
            top_pick = competitors[0]
            
            content = (
                f"Looking to replace {software}? We compare the top competitors offering better pricing, features, or ease of use. "
                f"Our analysis covers {', '.join(competitors[:3])}, and more. "
                f"Top pick: {top_pick} offers excellent value with a user-friendly interface and competitive pricing. "
                f"Whether you're switching due to cost, features, or platform preferences, these {software} alternatives provide robust solutions for {category.lower()} professionals."
            )
            
            alternatives.append({
                "slug": slug,
                "brand": "Software Alternatives",
                "title": title,
                "content": content,
                "code": "ALT",
                "category": category,
                "original_software": software,
                "alternatives": competitors
            })
            category_count += 1
        
        print(f"  ✅ Generated {category_count} alternative pages for {category}")
    
    return alternatives

def main():
    # Load existing data
    try:
        with open(OUTPUT_FILE, 'r') as f:
            existing_data = json.load(f)
            print(f"📄 Loaded {len(existing_data)} existing comparisons.")
    except FileNotFoundError:
        existing_data = []
        print("📄 No existing data found. Starting fresh.")

    # Generate new alternatives
    new_alternatives = generate_alternatives()
    
    # Check for duplicates
    existing_slugs = set(item['slug'] for item in existing_data)
    unique_new = [a for a in new_alternatives if a['slug'] not in existing_slugs]
    
    print(f"\n📊 Summary:")
    print(f"  - New alternatives generated: {len(new_alternatives)}")
    print(f"  - Duplicates filtered: {len(new_alternatives) - len(unique_new)}")
    print(f"  - Unique alternatives to add: {len(unique_new)}")
    
    # Combine and save
    all_data = existing_data + unique_new
    
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(all_data, f, indent=2)
        
    print(f"\n✅ Successfully saved {len(all_data)} total comparisons to {OUTPUT_FILE}")
    print(f"🎉 Added {len(unique_new)} new alternative pages!")

if __name__ == "__main__":
    main()
