import json

# Configuration
OUTPUT_FILE = 'src/data/saas.json'

# Software Categories
CATEGORIES = [
    "CRM",
    "Project Management",
    "Website Builder",
    "Email Marketing",
    "Accounting",
    "Video Editor"
]

# User Personas/Industries
PERSONAS = [
    "Real Estate Agents",
    "Startups",
    "Nonprofits",
    "Small Business",
    "Photographers",
    "Students",
    "Lawyers",
    "Contractors",
    "Restaurants",
    "E-Commerce"
]

# Specific needs mapping
SPECIFIC_NEEDS = {
    "CRM": {
        "Real Estate Agents": "property tracking and client follow-ups",
        "Startups": "lead nurturing and pipeline management",
        "Nonprofits": "donor management and fundraising",
        "Small Business": "customer relationship tracking",
        "Photographers": "client booking and project management",
        "Students": "networking and internship tracking",
        "Lawyers": "case management and client communication",
        "Contractors": "project bids and client contracts",
        "Restaurants": "reservation management and customer loyalty",
        "E-Commerce": "customer segmentation and retention"
    },
    "Project Management": {
        "Real Estate Agents": "listing management and team collaboration",
        "Startups": "agile workflows and sprint planning",
        "Nonprofits": "volunteer coordination and event planning",
        "Small Business": "task delegation and deadline tracking",
        "Photographers": "shoot scheduling and client deliverables",
        "Students": "group project coordination",
        "Lawyers": "case timelines and document management",
        "Contractors": "job scheduling and crew management",
        "Restaurants": "kitchen operations and staff scheduling",
        "E-Commerce": "inventory management and order fulfillment"
    },
    "Website Builder": {
        "Real Estate Agents": "property listings and virtual tours",
        "Startups": "landing pages and product showcases",
        "Nonprofits": "donation pages and volunteer sign-ups",
        "Small Business": "online presence and contact forms",
        "Photographers": "portfolio galleries and booking systems",
        "Students": "personal portfolios and resumes",
        "Lawyers": "professional profiles and consultation booking",
        "Contractors": "service showcases and quote requests",
        "Restaurants": "online menus and reservation systems",
        "E-Commerce": "product catalogs and shopping carts"
    },
    "Email Marketing": {
        "Real Estate Agents": "listing alerts and market updates",
        "Startups": "product launches and investor updates",
        "Nonprofits": "donor newsletters and campaign updates",
        "Small Business": "customer newsletters and promotions",
        "Photographers": "portfolio updates and booking reminders",
        "Students": "networking and event invitations",
        "Lawyers": "legal updates and consultation reminders",
        "Contractors": "project updates and seasonal promotions",
        "Restaurants": "menu updates and special offers",
        "E-Commerce": "abandoned cart recovery and product launches"
    },
    "Accounting": {
        "Real Estate Agents": "commission tracking and expense management",
        "Startups": "burn rate tracking and investor reporting",
        "Nonprofits": "grant management and donation tracking",
        "Small Business": "invoicing and tax preparation",
        "Photographers": "session pricing and expense tracking",
        "Students": "budget management and expense tracking",
        "Lawyers": "billable hours and trust accounting",
        "Contractors": "job costing and payroll management",
        "Restaurants": "inventory costs and profit margins",
        "E-Commerce": "sales tax and multi-channel revenue tracking"
    },
    "Video Editor": {
        "Real Estate Agents": "property tour videos and social media content",
        "Startups": "pitch videos and product demos",
        "Nonprofits": "impact stories and fundraising videos",
        "Small Business": "promotional videos and testimonials",
        "Photographers": "wedding videos and highlight reels",
        "Students": "class projects and creative portfolios",
        "Lawyers": "deposition reviews and case presentations",
        "Contractors": "before/after project videos",
        "Restaurants": "menu videos and social media content",
        "E-Commerce": "product demos and unboxing videos"
    }
}

def generate_persona_guides():
    guides = []
    print("🚀 Generating Persona-Based Buying Guides...")
    count = 0

    for category in CATEGORIES:
        for persona in PERSONAS:
            # Generate slug
            slug = f"best-{category.lower().replace(' ', '-')}-for-{persona.lower().replace(' ', '-')}"
            
            # Generate title
            title = f"7 Best {category} Tools for {persona} (2025)"
            
            # Get specific need
            specific_need = SPECIFIC_NEEDS.get(category, {}).get(persona, "industry-specific requirements")
            
            # Generate content
            content = (
                f"If you are in the {persona.lower()} industry, you need {category.lower()} software that handles {specific_need}. "
                f"We compared the top options to help you find the perfect fit for your specific needs. "
                f"Our analysis covers pricing, features, ease of use, and industry-specific functionality. "
                f"Whether you're looking for free options or enterprise solutions, this guide will help you make an informed decision for your {persona.lower()} business."
            )
            
            guides.append({
                "slug": slug,
                "brand": "Best Software Guide",
                "title": title,
                "content": content,
                "code": "TOP 7",
                "category": category,
                "persona": persona
            })
            
            count += 1
            if count % 20 == 0:
                print(f"  📊 Progress: {count} buying guides generated...")
    
    print(f"\n✅ Total persona buying guides generated: {count}")
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
    new_guides = generate_persona_guides()
    
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
    print(f"🎉 Added {len(unique_new)} new persona buying guides!")
    print(f"🚀 SaaS site now has {len(all_data)} total pages!")

if __name__ == "__main__":
    main()
