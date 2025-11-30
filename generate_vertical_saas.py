import json

# Configuration
OUTPUT_FILE = 'src/data/saas.json'

# Software Categories (B2B)
CATEGORIES = [
    "CRM",
    "Project Management",
    "Accounting",
    "Website Builder",
    "Scheduling Software",
    "Payroll Software",
    "Inventory Management"
]

# High-Value Industries (Rich & Non-Technical)
INDUSTRIES = [
    "Dentists",
    "Lawyers",
    "Plumbers",
    "Electricians",
    "Gym Owners",
    "Real Estate Agents",
    "Restaurants",
    "Hotels",
    "Landscapers",
    "Photographers",
    "Consultants",
    "Nonprofits",
    "Churches",
    "Schools"
]

# Platforms
PLATFORMS = ["Mac", "Windows", "iPad", "Android"]

def generate_industry_guides():
    guides = []
    print("🚀 Generating Industry-Specific Buying Guides...")
    count = 0

    # Industry-specific guides
    for category in CATEGORIES:
        for industry in INDUSTRIES:
            # Generate slug
            slug = f"best-{category.lower().replace(' ', '-')}-for-{industry.lower().replace(' ', '-')}"
            
            # Generate title
            title = f"5 Best {category} Tools for {industry} (2025 Review)"
            
            # Generate content
            content = (
                f"Running a {industry.lower()} business requires specialized {category.lower()} software. "
                f"We tested the top options for compliance, ease of use, and pricing specific to the {industry.lower()} industry. "
                f"Our analysis covers features that matter most to {industry.lower()}, including industry-specific workflows and integrations. "
                f"Whether you're a solo practitioner or managing a team, these {category.lower()} solutions are tailored for {industry.lower()} professionals."
            )
            
            guides.append({
                "slug": slug,
                "brand": "Industry Guide",
                "title": title,
                "content": content,
                "code": "TOP 5",
                "category": category,
                "industry": industry
            })
            
            count += 1
            if count % 20 == 0:
                print(f"  📊 Progress: {count} guides generated...")
    
    # Platform-specific guides
    for category in CATEGORIES:
        for platform in PLATFORMS:
            # Generate slug
            slug = f"best-{category.lower().replace(' ', '-')}-for-{platform.lower()}"
            
            # Generate title
            title = f"Best {category} for {platform} (2025 Guide)"
            
            # Generate content
            content = (
                f"Looking for {category.lower()} software optimized for {platform}? "
                f"We tested the top {category.lower()} tools that work seamlessly on {platform} devices. "
                f"Our analysis covers native apps, cloud compatibility, and {platform}-specific features. "
                f"Find the perfect {category.lower()} solution that takes full advantage of your {platform} hardware and ecosystem."
            )
            
            guides.append({
                "slug": slug,
                "brand": "Platform Guide",
                "title": title,
                "content": content,
                "code": "TOP 5",
                "category": category,
                "platform": platform
            })
            
            count += 1
            if count % 20 == 0:
                print(f"  📊 Progress: {count} guides generated...")
    
    print(f"\n✅ Total vertical guides generated: {count}")
    return guides

def main():
    # Load existing data
    try:
        with open(OUTPUT_FILE, 'r') as f:
            existing_data = json.load(f)
            print(f"📄 Loaded {len(existing_data)} existing comparisons.")
    except FileNotFoundError:
        existing_data = []
        print("📄 No existing data found. Starting fresh.")

    # Generate new guides
    new_guides = generate_industry_guides()
    
    # Check for duplicates
    existing_slugs = set(item['slug'] for item in existing_data)
    unique_new = [g for g in new_guides if g['slug'] not in existing_slugs]
    
    print(f"\n📊 Summary:")
    print(f"  - New guides generated: {len(new_guides)}")
    print(f"  - Duplicates filtered: {len(new_guides) - len(unique_new)}")
    print(f"  - Unique guides to add: {len(unique_new)}")
    
    # Combine and save
    all_data = existing_data + unique_new
    
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(all_data, f, indent=2)
        
    print(f"\n✅ Successfully saved {len(all_data)} total comparisons to {OUTPUT_FILE}")
    print(f"🎉 Added {len(unique_new)} new vertical guides!")
    print(f"🚀 SaaS site now has {len(all_data)} total pages!")

if __name__ == "__main__":
    main()
