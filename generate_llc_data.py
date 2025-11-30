import json

# Configuration
OUTPUT_FILE = 'src/data/llc.json'

# US States with accurate LLC filing data
STATES_DATA = [
    {"state": "Alabama", "fee": "$200", "time": "7-10 business days", "tax": "No annual franchise tax"},
    {"state": "Alaska", "fee": "$250", "time": "15 business days", "tax": "$100 biennial report fee"},
    {"state": "Arizona", "fee": "$50", "time": "5-7 business days", "tax": "No annual franchise tax"},
    {"state": "Arkansas", "fee": "$45", "time": "7-10 business days", "tax": "$150 annual franchise tax"},
    {"state": "California", "fee": "$70", "time": "5-7 business days", "tax": "$800 annual franchise tax"},
    {"state": "Colorado", "fee": "$50", "time": "3-5 business days", "tax": "$10 periodic report fee"},
    {"state": "Connecticut", "fee": "$120", "time": "7-10 business days", "tax": "$80 annual report fee"},
    {"state": "Delaware", "fee": "$90", "time": "5-7 business days", "tax": "$300 annual franchise tax"},
    {"state": "Florida", "fee": "$125", "time": "5-7 business days", "tax": "$138.75 annual report fee"},
    {"state": "Georgia", "fee": "$100", "time": "7-10 business days", "tax": "$50 annual registration fee"},
    {"state": "Hawaii", "fee": "$50", "time": "5-7 business days", "tax": "$15 annual report fee"},
    {"state": "Idaho", "fee": "$100", "time": "7-10 business days", "tax": "No annual franchise tax"},
    {"state": "Illinois", "fee": "$150", "time": "10-15 business days", "tax": "$75 annual report fee"},
    {"state": "Indiana", "fee": "$95", "time": "7-10 business days", "tax": "$50 biennial report fee"},
    {"state": "Iowa", "fee": "$50", "time": "5-7 business days", "tax": "$45 biennial report fee"},
    {"state": "Kansas", "fee": "$160", "time": "7-10 business days", "tax": "$50 annual report fee"},
    {"state": "Kentucky", "fee": "$40", "time": "7-10 business days", "tax": "$15 annual report fee"},
    {"state": "Louisiana", "fee": "$100", "time": "10-15 business days", "tax": "$35 annual report fee"},
    {"state": "Maine", "fee": "$175", "time": "7-10 business days", "tax": "$85 annual report fee"},
    {"state": "Maryland", "fee": "$100", "time": "7-10 business days", "tax": "$300 annual personal property tax"},
    {"state": "Massachusetts", "fee": "$500", "time": "7-10 business days", "tax": "$500 annual report fee"},
    {"state": "Michigan", "fee": "$50", "time": "5-7 business days", "tax": "$25 annual statement fee"},
    {"state": "Minnesota", "fee": "$135", "time": "7-10 business days", "tax": "No annual franchise tax"},
    {"state": "Mississippi", "fee": "$50", "time": "7-10 business days", "tax": "No annual franchise tax"},
    {"state": "Missouri", "fee": "$50", "time": "5-7 business days", "tax": "No annual franchise tax"},
    {"state": "Montana", "fee": "$35", "time": "5-7 business days", "tax": "$20 annual report fee"},
    {"state": "Nebraska", "fee": "$100", "time": "7-10 business days", "tax": "$13 biennial report fee"},
    {"state": "Nevada", "fee": "$75", "time": "5-7 business days", "tax": "$350 annual business license fee"},
    {"state": "New Hampshire", "fee": "$100", "time": "7-10 business days", "tax": "$100 annual report fee"},
    {"state": "New Jersey", "fee": "$125", "time": "10-15 business days", "tax": "$75 annual report fee"},
    {"state": "New Mexico", "fee": "$50", "time": "10-15 business days", "tax": "No annual franchise tax"},
    {"state": "New York", "fee": "$200", "time": "7-10 business days", "tax": "$9 biennial statement fee"},
    {"state": "North Carolina", "fee": "$125", "time": "7-10 business days", "tax": "$200 annual report fee"},
    {"state": "North Dakota", "fee": "$135", "time": "7-10 business days", "tax": "$50 annual report fee"},
    {"state": "Ohio", "fee": "$99", "time": "5-7 business days", "tax": "No annual franchise tax"},
    {"state": "Oklahoma", "fee": "$100", "time": "7-10 business days", "tax": "$25 annual certificate fee"},
    {"state": "Oregon", "fee": "$100", "time": "7-10 business days", "tax": "$100 annual report fee"},
    {"state": "Pennsylvania", "fee": "$125", "time": "7-10 business days", "tax": "No annual franchise tax"},
    {"state": "Rhode Island", "fee": "$150", "time": "10-15 business days", "tax": "$50 annual report fee"},
    {"state": "South Carolina", "fee": "$110", "time": "7-10 business days", "tax": "No annual franchise tax"},
    {"state": "South Dakota", "fee": "$150", "time": "7-10 business days", "tax": "$50 annual report fee"},
    {"state": "Tennessee", "fee": "$300", "time": "7-10 business days", "tax": "$300 annual franchise tax"},
    {"state": "Texas", "fee": "$300", "time": "5-7 business days", "tax": "No annual franchise tax (revenue-based)"},
    {"state": "Utah", "fee": "$54", "time": "5-7 business days", "tax": "$18 annual renewal fee"},
    {"state": "Vermont", "fee": "$125", "time": "7-10 business days", "tax": "$35 annual report fee"},
    {"state": "Virginia", "fee": "$100", "time": "7-10 business days", "tax": "$50 annual registration fee"},
    {"state": "Washington", "fee": "$200", "time": "5-7 business days", "tax": "$69 annual report fee"},
    {"state": "West Virginia", "fee": "$100", "time": "7-10 business days", "tax": "$25 annual report fee"},
    {"state": "Wisconsin", "fee": "$130", "time": "7-10 business days", "tax": "$25 annual report fee"},
    {"state": "Wyoming", "fee": "$100", "time": "5-7 business days", "tax": "$60 annual license tax"}
]

def generate_llc_records():
    records = []
    print("🚀 Generating LLC Formation Records for All 50 States...")

    for state_data in STATES_DATA:
        state = state_data["state"]
        fee = state_data["fee"]
        time = state_data["time"]
        tax = state_data["tax"]
        
        # Generate slug
        slug = f"form-llc-in-{state.lower().replace(' ', '-')}"
        
        # Generate title
        title = f"How to Form an LLC in {state}: 2025 Cost & Guide"
        
        # Generate content
        content = (
            f"Starting an LLC in {state} costs {fee} and takes {time}. "
            f"You must file the Articles of Organization with the {state} Secretary of State. "
            f"Annual requirements: {tax}. "
            f"We recommend using a professional LLC formation service to avoid rejection and ensure compliance with {state} state regulations. "
            f"Professional services typically handle name searches, registered agent services, and ongoing compliance reminders."
        )
        
        records.append({
            "slug": slug,
            "brand": state,
            "title": title,
            "content": content,
            "code": "LLC",
            "fee": fee,
            "time": time,
            "tax": tax
        })
    
    print(f"✅ Generated {len(records)} LLC formation records")
    return records

def main():
    records = generate_llc_records()
    
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(records, f, indent=2)
        
    print(f"\n✅ Successfully saved {len(records)} records to {OUTPUT_FILE}")
    print(f"🎉 LLC Formation Database is ready!")

if __name__ == "__main__":
    main()
