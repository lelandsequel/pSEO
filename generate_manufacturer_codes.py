import json
import random

# Configuration
OUTPUT_FILE = 'src/data/layoffs.json'

# Manufacturer Specific Codes
MANUFACTURERS = {
    "BMW": {
        "code_types": [
            {"prefix": "CC-ID-", "range": (1, 50), "desc": "Central Control ID"},
            {"prefix": "", "range": (0x2A00, 0x2A50), "desc": "DMTL System", "hex": True},
            {"prefix": "", "range": (0x4F00, 0x4F30), "desc": "Transmission Control", "hex": True}
        ],
        "symptoms": [
            "Check Engine Light illuminated",
            "Rough idle or stalling",
            "Reduced engine performance",
            "Transmission shifting issues",
            "Service Engine Soon light"
        ]
    },
    "Ford": {
        "code_types": [
            {"prefix": "P1", "range": (100, 299), "desc": "Powertrain"},
            {"prefix": "P1", "range": (400, 699), "desc": "Fuel System"},
            {"prefix": "U1", "range": (100, 250), "desc": "Network Communication"}
        ],
        "symptoms": [
            "Check Engine Light on",
            "Poor fuel economy",
            "Hard starting condition",
            "Rough running engine",
            "Transmission problems"
        ]
    },
    "Mercedes": {
        "code_types": [
            {"prefix": "P1", "range": (100, 250), "desc": "Engine Control"},
            {"prefix": "B1", "range": (100, 200), "desc": "Body Control"},
            {"prefix": "C1", "range": (100, 180), "desc": "Chassis"}
        ],
        "symptoms": [
            "Service A/B indicator",
            "Check Engine Light",
            "ESP/ABS warning light",
            "Reduced power mode",
            "Air suspension malfunction"
        ]
    },
    "Honda": {
        "code_types": [
            {"prefix": "P1", "range": (100, 299), "desc": "VTEC System"},
            {"prefix": "P1", "range": (400, 599), "desc": "Fuel System"},
            {"prefix": "P3", "range": (100, 199), "desc": "Hybrid Battery"}
        ],
        "symptoms": [
            "Check Engine Light",
            "VTEC not engaging",
            "Poor acceleration",
            "IMA light (hybrid models)",
            "Battery charge issues"
        ]
    },
    "Toyota": {
        "code_types": [
            {"prefix": "P1", "range": (100, 299), "desc": "Engine Control"},
            {"prefix": "P3", "range": (100, 250), "desc": "Hybrid System"},
            {"prefix": "C1", "range": (200, 299), "desc": "ABS/VSC"}
        ],
        "symptoms": [
            "Check Engine Light",
            "Hybrid system warning",
            "Reduced power mode",
            "VSC/Traction control light",
            "Battery cooling fan issues"
        ]
    }
}

def generate_code_string(code_type, index):
    """Generate the actual code string."""
    if code_type.get("hex"):
        return f"{index:04X}"
    else:
        prefix = code_type["prefix"]
        if prefix:
            return f"{prefix}{index:03d}"
        else:
            return str(index)

def generate_manufacturer_codes():
    codes = []
    print("🚀 Generating Manufacturer Specific Codes...")

    for brand, data in MANUFACTURERS.items():
        brand_count = 0
        
        for code_type in data["code_types"]:
            start, end = code_type["range"]
            # Generate subset of codes in range
            num_codes = min(25, (end - start) // 2)
            selected_indices = random.sample(range(start, end), num_codes)
            
            for index in selected_indices:
                code_str = generate_code_string(code_type, index)
                slug = f"{brand.lower()}-code-{code_str.lower().replace('_', '-')}-fix"
                
                # Generate title
                system = code_type["desc"]
                title = f"{brand} Code {code_str}: {system} Issue"
                
                # Generate content
                symptom = random.choice(data["symptoms"])
                content = (
                    f"The {code_str} code in {brand} vehicles indicates a {system.lower()} malfunction. "
                    f"Common symptoms include: {symptom.lower()}. "
                    f"This is a manufacturer-specific code that requires a {brand}-compatible diagnostic scanner to properly diagnose. "
                    f"Professional diagnosis is recommended as this code may indicate multiple potential issues within the {system.lower()}."
                )
                
                codes.append({
                    "slug": slug,
                    "brand": brand,
                    "title": title,
                    "content": content,
                    "code": code_str
                })
                brand_count += 1
        
        print(f"  ✅ Generated {brand_count} codes for {brand}")
    
    return codes

def main():
    # Load existing data
    try:
        with open(OUTPUT_FILE, 'r') as f:
            existing_data = json.load(f)
            print(f"📄 Loaded {len(existing_data)} existing codes.")
    except FileNotFoundError:
        existing_data = []
        print("📄 No existing data found. Starting fresh.")

    # Generate new codes
    new_codes = generate_manufacturer_codes()
    
    # Check for duplicates
    existing_slugs = set(item['slug'] for item in existing_data)
    unique_new = [c for c in new_codes if c['slug'] not in existing_slugs]
    
    print(f"\n📊 Summary:")
    print(f"  - New codes generated: {len(new_codes)}")
    print(f"  - Duplicates filtered: {len(new_codes) - len(unique_new)}")
    print(f"  - Unique codes to add: {len(unique_new)}")
    
    # Combine and save
    all_data = existing_data + unique_new
    
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(all_data, f, indent=2)
        
    print(f"\n✅ Successfully saved {len(all_data)} total codes to {OUTPUT_FILE}")
    print(f"🎉 Added {len(unique_new)} new manufacturer-specific codes!")

if __name__ == "__main__":
    main()
