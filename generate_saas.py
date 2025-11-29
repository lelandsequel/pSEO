import json
import itertools

# Configuration
OUTPUT_FILE = 'src/data/saas.json'

CATEGORIES = {
    "Project Management": ["Monday", "Asana", "ClickUp", "Trello", "Jira"],
    "CRM": ["Salesforce", "HubSpot", "Pipedrive", "Zoho"],
    "Marketing": ["Mailchimp", "ConvertKit", "ActiveCampaign"]
}

def generate_comparisons():
    comparisons = []
    print("🚀 Generating SaaS Comparisons...")

    for category, tools in CATEGORIES.items():
        # Generate all unique pairs
        pairs = list(itertools.combinations(tools, 2))
        
        for tool_a, tool_b in pairs:
            slug = f"{tool_a.lower()}-vs-{tool_b.lower()}"
            title = f"{tool_a} vs {tool_b}: 2025 Review"
            
            content = (
                f"Comparing {tool_a} and {tool_b} for {category.lower()} needs. "
                f"{tool_a} is often praised for its intuitive interface and ease of use, while {tool_b} offers robust customization options. "
                "Pricing structures differ, so consider your team size and specific feature requirements before choosing."
            )
            
            comparisons.append({
                "slug": slug,
                "brand": "SaaS Comparison",
                "title": title,
                "content": content,
                "code": "VS",
                "category": category
            })
            
    print(f"✅ Generated {len(comparisons)} comparisons.")
    return comparisons

def main():
    data = generate_comparisons()
    
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(data, f, indent=2)
        
    print(f"💾 Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
