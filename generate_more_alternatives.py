import json

# Configuration
OUTPUT_FILE = 'src/data/saas.json'

# New Software Categories with Alternatives
NEW_SOFTWARE_ALTERNATIVES = {
    "Video/VFX": {
        "Premiere Pro": ["DaVinci Resolve", "Final Cut Pro", "Filmora", "HitFilm", "Kdenlive"],
        "After Effects": ["DaVinci Fusion", "Blender", "HitFilm", "Natron", "Cavalry"],
        "Final Cut Pro": ["DaVinci Resolve", "Premiere Pro", "Filmora", "iMovie", "Kdenlive"],
        "DaVinci Resolve": ["Premiere Pro", "Final Cut Pro", "Filmora", "Vegas Pro", "Lightworks"]
    },
    "3D/CAD": {
        "Maya": ["Blender", "Cinema 4D", "3ds Max", "Houdini", "Modo"],
        "AutoCAD": ["FreeCAD", "LibreCAD", "SketchUp", "Fusion 360", "SolidWorks"],
        "Cinema 4D": ["Blender", "Maya", "Houdini", "3ds Max", "Modo"],
        "Blender": ["Maya", "Cinema 4D", "3ds Max", "Houdini", "ZBrush"],
        "SketchUp": ["AutoCAD", "FreeCAD", "Fusion 360", "Revit", "ArchiCAD"]
    },
    "E-Commerce": {
        "Shopify": ["WooCommerce", "BigCommerce", "Wix eCommerce", "Squarespace Commerce", "Magento"],
        "WooCommerce": ["Shopify", "BigCommerce", "PrestaShop", "OpenCart", "Magento"],
        "BigCommerce": ["Shopify", "WooCommerce", "Magento", "Wix eCommerce", "Volusion"],
        "Magento": ["Shopify", "WooCommerce", "BigCommerce", "PrestaShop", "OpenCart"]
    },
    "Productivity": {
        "Evernote": ["Notion", "OneNote", "Bear", "Obsidian", "Apple Notes"],
        "OneNote": ["Evernote", "Notion", "Google Keep", "Bear", "Simplenote"],
        "Airtable": ["Notion", "Coda", "Monday.com", "ClickUp", "SmartSheet"],
        "Monday.com": ["Asana", "ClickUp", "Trello", "Airtable", "Notion"]
    },
    "Creative": {
        "Lightroom": ["Capture One", "Luminar AI", "ON1 Photo RAW", "Affinity Photo", "DxO PhotoLab"],
        "InDesign": ["Affinity Publisher", "Scribus", "QuarkXPress", "Lucidpress", "Canva"],
        "CorelDRAW": ["Illustrator", "Affinity Designer", "Inkscape", "Vectornator", "Sketch"]
    }
}

def generate_alternatives():
    alternatives = []
    print("🚀 Generating NEW Alternative Pages...")
    count = 0

    for category, software_dict in NEW_SOFTWARE_ALTERNATIVES.items():
        category_count = 0
        
        for software, competitors in software_dict.items():
            slug = f"alternatives-to-{software.lower().replace(' ', '-')}"
            title = f"Best Free & Paid Alternatives to {software} (2025)"
            
            # Pick top competitor for content
            top_pick = competitors[0]
            
            content = (
                f"Why pay for {software}? Check out these competitors that offer similar features for a fraction of the price. "
                f"We've analyzed {', '.join(competitors[:3])}, and more to help you find the perfect alternative. "
                f"Top pick: {top_pick} provides excellent value with comparable functionality at a lower cost. "
                f"Whether you're looking for free options or more affordable paid plans, these {software} alternatives deliver professional results without breaking the bank."
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
            count += 1
            
            if count % 20 == 0:
                print(f"  📊 Progress: {count} alternatives generated...")
        
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
    print(f"🚀 SaaS site now has {len(all_data)} total pages!")

if __name__ == "__main__":
    main()
