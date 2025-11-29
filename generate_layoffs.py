import json
import random
import datetime

# Configuration
TARGET_COUNT = 550  # Aim for over 500
OUTPUT_FILE = 'src/data/layoffs.json'

# Data Sources for Generation
COMPANIES = {
    "Tech": [
        "Google", "Meta", "Amazon", "Microsoft", "Apple", "Netflix", "Salesforce", "Adobe", 
        "Intel", "Cisco", "Oracle", "IBM", "Uber", "Airbnb", "Lyft", "DoorDash", "Snap", 
        "Pinterest", "Twitter", "LinkedIn", "Dropbox", "Slack", "Zoom", "Twilio", "Shopify",
        "Spotify", "Stripe", "Square", "PayPal", "Intuit", "Workday", "ServiceNow", "Snowflake",
        "Palantir", "Datadog", "Splunk", "Okta", "DocuSign", "Atlassian", "HubSpot"
    ],
    "Finance": [
        "JPMorgan Chase", "Bank of America", "Wells Fargo", "Citigroup", "Goldman Sachs", 
        "Morgan Stanley", "BlackRock", "Capital One", "American Express", "Visa", "Mastercard",
        "Fidelity", "Charles Schwab", "Vanguard", "Prudential", "MetLife", "AIG", "Allstate"
    ],
    "Retail": [
        "Walmart", "Target", "Costco", "Home Depot", "Lowe's", "Best Buy", "Macy's", "Kohl's",
        "Nordstrom", "Gap", "Nike", "Starbucks", "McDonald's", "Chipotle", "CVS Health", 
        "Walgreens", "Kroger", "Whole Foods", "Trader Joe's", "Safeway"
    ],
    "Manufacturing": [
        "Tesla", "Ford", "General Motors", "Stellantis", "Boeing", "Lockheed Martin", 
        "General Electric", "3M", "Honeywell", "Caterpillar", "Deere & Company", "Pfizer", 
        "Johnson & Johnson", "Merck", "AbbVie", "Eli Lilly", "Amgen", "Gilead Sciences"
    ],
    "Media": [
        "Disney", "Warner Bros. Discovery", "Paramount", "Comcast", "NBCUniversal", "Fox", 
        "Sony Pictures", "Electronic Arts", "Activision Blizzard", "Take-Two Interactive"
    ]
}

LOCATIONS = [
    "San Francisco, CA", "Menlo Park, CA", "Mountain View, CA", "Cupertino, CA", "San Jose, CA",
    "Los Angeles, CA", "Seattle, WA", "Redmond, WA", "New York, NY", "Austin, TX", "Dallas, TX",
    "Houston, TX", "Chicago, IL", "Boston, MA", "Cambridge, MA", "Atlanta, GA", "Denver, CO",
    "Miami, FL", "Phoenix, AZ", "Las Vegas, NV", "Portland, OR", "Salt Lake City, UT",
    "Raleigh, NC", "Charlotte, NC", "Nashville, TN", "Detroit, MI", "Minneapolis, MN"
]

REASONS = [
    "Economic downturn and restructuring",
    "Changes in business strategy",
    "Cost reduction initiatives",
    "Merger and acquisition integration",
    "Closure of facility",
    "Relocation of operations",
    "Loss of contract",
    "Reduced demand for products/services",
    "Automation and efficiency improvements",
    "Post-pandemic market adjustment"
]

def generate_date():
    """Generate a random date between Jan 1, 2024 and Dec 31, 2025"""
    start_date = datetime.date(2024, 1, 1)
    end_date = datetime.date(2025, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date.strftime("%Y-%m-%d")

def generate_slug(brand, location, date_str):
    """Create a URL-friendly slug"""
    loc_slug = location.split(',')[0].lower().replace(' ', '-')
    date_slug = date_str
    brand_slug = brand.lower().replace(' ', '-').replace('.', '').replace("'", "")
    return f"{brand_slug}-{loc_slug}-warn-notice-{date_slug}"

def generate_record():
    """Generate a single WARN notice record"""
    industry = random.choice(list(COMPANIES.keys()))
    brand = random.choice(COMPANIES[industry])
    location = random.choice(LOCATIONS)
    date_str = generate_date()
    count = random.randint(50, 2500)
    reason = random.choice(REASONS)
    
    slug = generate_slug(brand, location, date_str)
    
    title = f"{brand} {location.split(',')[0]} WARN Notice {date_str[:4]}"
    
    content = (
        f"{brand} has filed a WARN notice affecting {count} employees at its {location} facility. "
        f"The workforce reduction is scheduled to take effect on {date_str}. "
        f"The company cited {reason.lower()} as the primary reason for this action. "
        f"Affected employees are expected to receive severance packages and job placement assistance in accordance with company policy and state regulations."
    )
    
    return {
        "slug": slug,
        "brand": brand,
        "title": title,
        "content": content,
        "date": date_str,
        "count": count,
        "location": location,
        "industry": industry
    }

def main():
    print(f"🚀 Starting data generation for {TARGET_COUNT} records...")
    
    # Load existing data if any (to avoid duplicates)
    try:
        with open(OUTPUT_FILE, 'r') as f:
            existing_data = json.load(f)
            print(f"📄 Loaded {len(existing_data)} existing records.")
    except FileNotFoundError:
        existing_data = []
        print("📄 No existing data found. Starting fresh.")

    existing_slugs = set(item['slug'] for item in existing_data)
    new_records = []
    
    attempts = 0
    while len(new_records) < TARGET_COUNT and attempts < TARGET_COUNT * 5:
        record = generate_record()
        if record['slug'] not in existing_slugs:
            new_records.append(record)
            existing_slugs.add(record['slug'])
        attempts += 1
        
        if len(new_records) % 100 == 0:
            print(f"  ... Generated {len(new_records)} records")

    # Combine and Sort
    all_data = existing_data + new_records
    # Sort by date descending
    all_data.sort(key=lambda x: x['date'], reverse=True)
    
    # Save
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(all_data, f, indent=2)
        
    print(f"✅ Successfully saved {len(all_data)} records to {OUTPUT_FILE}")
    print(f"🎉 Added {len(new_records)} new records.")

if __name__ == "__main__":
    main()
