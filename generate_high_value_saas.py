import json
import itertools

# Configuration
OUTPUT_FILE = 'src/data/saas.json'

# High-Value Categories
CATEGORIES = {
    "Hosting Comparison": {
        "tools": ["Bluehost", "SiteGround", "Hostinger", "Kinsta", "WP Engine", "GoDaddy", "Namecheap"],
        "features": ["uptime", "speed", "customer support", "pricing", "free domain", "30-day money-back guarantee"]
    },
    "VPN Comparison": {
        "tools": ["NordVPN", "ExpressVPN", "Surfshark", "CyberGhost", "ProtonVPN", "IPVanish"],
        "features": ["speed", "privacy", "streaming capabilities", "server locations", "price", "no-logs policy"]
    },
    "Website Builder Comparison": {
        "tools": ["Shopify", "Wix", "Squarespace", "WordPress", "Webflow"],
        "features": ["ease of use", "templates", "e-commerce features", "pricing", "customization options"]
    }
}

def generate_content(tool_a, tool_b, category):
    """Generate realistic comparison content."""
    if "Hosting" in category:
        return (
            f"Comparing {tool_a} and {tool_b} for web hosting needs in 2025. "
            f"{tool_a} offers competitive pricing with a free domain on annual plans, while {tool_b} is known for superior uptime and speed. "
            f"Both providers include a 30-day money-back guarantee, but differ in their customer support approach and server infrastructure. "
            f"Consider your specific needs for WordPress optimization, scalability, and budget when choosing between these two hosts."
        )
    elif "VPN" in category:
        return (
            f"Comparing {tool_a} and {tool_b} for VPN services in 2025. "
            f"{tool_a} excels in streaming capabilities and server locations, while {tool_b} is praised for its speed and strict no-logs policy. "
            f"Both VPNs offer strong encryption and privacy features, but pricing structures and simultaneous connection limits vary. "
            f"Choose based on your priorities: streaming access, privacy guarantees, or value for money."
        )
    else:  # Website Builder
        return (
            f"Comparing {tool_a} and {tool_b} for website building in 2025. "
            f"{tool_a} provides an intuitive drag-and-drop interface with extensive templates, while {tool_b} offers more advanced customization options. "
            f"E-commerce features, pricing tiers, and ease of use differ significantly between these platforms. "
            f"Consider your technical skill level and business requirements when selecting your website builder."
        )

def generate_comparisons():
    comparisons = []
    print("🚀 Generating High-Value SaaS Comparisons...")

    for category, data in CATEGORIES.items():
        tools = data["tools"]
        # Generate all unique pairs
        pairs = list(itertools.combinations(tools, 2))
        
        for tool_a, tool_b in pairs:
            slug = f"{tool_a.lower().replace(' ', '-')}-vs-{tool_b.lower().replace(' ', '-')}"
            title = f"{tool_a} vs {tool_b}: Which is Best for 2025?"
            content = generate_content(tool_a, tool_b, category)
            
            comparisons.append({
                "slug": slug,
                "brand": category,
                "title": title,
                "content": content,
                "code": "VS",
                "category": category
            })
            
        print(f"  ✅ Generated {len(pairs)} comparisons for {category}")
    
    return comparisons

def main():
    # Load existing data
    try:
        with open(OUTPUT_FILE, 'r') as f:
            existing_data = json.load(f)
            print(f"📄 Loaded {len(existing_data)} existing comparisons.")
    except FileNotFoundError:
        existing_data = []
        print("📄 No existing data found. Starting fresh.")

    # Generate new comparisons
    new_comparisons = generate_comparisons()
    
    # Check for duplicates
    existing_slugs = set(item['slug'] for item in existing_data)
    unique_new = [c for c in new_comparisons if c['slug'] not in existing_slugs]
    
    print(f"\n📊 Summary:")
    print(f"  - New comparisons generated: {len(new_comparisons)}")
    print(f"  - Duplicates filtered: {len(new_comparisons) - len(unique_new)}")
    print(f"  - Unique comparisons to add: {len(unique_new)}")
    
    # Combine and save
    all_data = existing_data + unique_new
    
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(all_data, f, indent=2)
        
    print(f"\n✅ Successfully saved {len(all_data)} total comparisons to {OUTPUT_FILE}")
    print(f"🎉 Added {len(unique_new)} new comparisons!")

if __name__ == "__main__":
    main()
