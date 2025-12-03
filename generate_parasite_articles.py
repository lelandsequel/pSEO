import json
import os
from pathlib import Path

# Configuration
DATA_FILE = 'src/data/saas.json'
OUTPUT_DIR = Path('public/parasite_articles')
LIMIT = 50

def generate_article(record):
    """Generate a Parasite SEO article from a SaaS record."""
    slug = record.get('slug', '')
    title = record.get('title', '')
    content_data = record.get('content', '') or record.get('description', '')
    
    # Extract tool names from title (assuming "Tool A vs Tool B")
    if ' vs ' in title:
        parts = title.split(' vs ')
        tool_a = parts[0].strip()
        tool_b = parts[1].strip()
    else:
        # Fallback if title format is different
        tool_a = title
        tool_b = "the alternative"

    # Viral Template
    headline = f"Stop Overpaying for {tool_a}. Why {tool_b} is the better choice in 2025."
    
    markdown_content = f"""# {headline}

I analyzed the pricing, features, and support for both. The winner surprised me.

## The Data

{content_data}

## The Verdict

If you're tired of overpaying for {tool_a}, {tool_b} might be exactly what you need.

I built a full database of alternatives. See the full breakdown and get the best deal here:
https://saasguide.org/{slug}
"""
    return slug, markdown_content

def main():
    print("🚀 Starting Parasite SEO Article Generator...")
    
    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"✓ Output directory ready: {OUTPUT_DIR}")
    
    # Load data
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        print(f"✓ Loaded data from {DATA_FILE}")
    except FileNotFoundError:
        print(f"❌ Error: Data file not found at {DATA_FILE}")
        return

    # Process records
    count = 0
    for record in data[:LIMIT]:
        slug, content = generate_article(record)
        
        if not slug:
            continue
            
        filename = OUTPUT_DIR / f"{slug}.md"
        with open(filename, 'w') as f:
            f.write(content)
            
        count += 1
        if count % 10 == 0:
            print(f"   Generated {count} articles...")

    print("=" * 40)
    print(f"✅ Success! Generated {count} articles in {OUTPUT_DIR}")
    print("=" * 40)

if __name__ == "__main__":
    main()
