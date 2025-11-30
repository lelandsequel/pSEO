import json

# Configuration
OUTPUT_FILE = 'src/data/layoffs.json'

# The Big 10 Codes (5 common + 5 cylinder misfires)
ERROR_CODES = {
    "P0300": "Random/Multiple Cylinder Misfire Detected",
    "P0420": "Catalyst System Efficiency Below Threshold",
    "P0171": "System Too Lean (Bank 1)",
    "P0455": "Evaporative Emission System Leak Detected (Large Leak)",
    "P0442": "Evaporative Emission System Leak Detected (Small Leak)",
    "P0301": "Cylinder 1 Misfire Detected",
    "P0302": "Cylinder 2 Misfire Detected",
    "P0303": "Cylinder 3 Misfire Detected",
    "P0304": "Cylinder 4 Misfire Detected",
    "P0305": "Cylinder 5 Misfire Detected"
}

# Top Selling Vehicles
VEHICLES = [
    {"make": "Ford", "model": "F-150"},
    {"make": "Chevy", "model": "Silverado"},
    {"make": "Ram", "model": "1500"},
    {"make": "Toyota", "model": "Camry"},
    {"make": "Honda", "model": "Accord"},
    {"make": "Nissan", "model": "Altima"},
    {"make": "Honda", "model": "CR-V"},
    {"make": "Toyota", "model": "RAV4"},
    {"make": "Nissan", "model": "Rogue"},
    {"make": "Honda", "model": "Civic"},
    {"make": "Toyota", "model": "Corolla"},
    {"make": "Jeep", "model": "Grand Cherokee"},
    {"make": "Ford", "model": "Explorer"}
]

# Years
YEARS = [2015, 2016, 2017, 2018, 2019, 2020]

def generate_content(year, make, model, code, description):
    """Generate vehicle-specific error code content."""
    return (
        f"Is your {year} {make} {model} throwing code {code}? This usually indicates {description.lower()}. "
        f"Common causes for this specific model include faulty ignition coils, worn spark plugs, or vacuum leaks. "
        f"For the {year} {make} {model}, this code often appears after 80,000+ miles due to normal wear and tear. "
        f"Recommended diagnostic tools: BlueDriver OBD2 Scanner or FOXWELL NT301. "
        f"Professional diagnosis is recommended to pinpoint the exact cause in your specific vehicle."
    )

def generate_car_matrix():
    records = []
    print("🚀 Generating Vehicle-Specific Error Code Matrix...")
    count = 0

    for vehicle in VEHICLES:
        make = vehicle["make"]
        model = vehicle["model"]
        
        for year in YEARS:
            for code, description in ERROR_CODES.items():
                # Generate slug
                slug = f"{year}-{make.lower()}-{model.lower().replace(' ', '-')}-{code.lower()}-fix"
                
                # Generate title
                title = f"{year} {make} {model} {code}: Diagnosis & Fix"
                
                # Generate brand
                brand = f"{make} {model}"
                
                # Generate content
                content = generate_content(year, make, model, code, description)
                
                records.append({
                    "slug": slug,
                    "brand": brand,
                    "title": title,
                    "content": content,
                    "code": code,
                    "year": year,
                    "make": make,
                    "model": model
                })
                
                count += 1
                if count % 100 == 0:
                    print(f"  📊 Progress: {count} vehicle-specific pages generated...")
    
    print(f"\n✅ Total vehicle-specific pages generated: {count}")
    return records

def main():
    # Load existing data
    try:
        with open(OUTPUT_FILE, 'r') as f:
            existing_data = json.load(f)
            print(f"📄 Loaded {len(existing_data)} existing codes.")
    except FileNotFoundError:
        existing_data = []
        print("📄 No existing data found. Starting fresh.")

    # Generate new records
    new_records = generate_car_matrix()
    
    # Check for duplicates
    existing_slugs = set(item['slug'] for item in existing_data)
    unique_new = [r for r in new_records if r['slug'] not in existing_slugs]
    
    print(f"\n📊 Summary:")
    print(f"  - New records generated: {len(new_records)}")
    print(f"  - Duplicates filtered: {len(new_records) - len(unique_new)}")
    print(f"  - Unique records to add: {len(unique_new)}")
    
    # Combine and save
    all_data = existing_data + unique_new
    
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(all_data, f, indent=2)
        
    print(f"\n✅ Successfully saved {len(all_data)} total codes to {OUTPUT_FILE}")
    print(f"🎉 Added {len(unique_new)} new vehicle-specific pages!")
    print(f"🚀 OBD2 site now has {len(all_data)} total pages!")

if __name__ == "__main__":
    main()
