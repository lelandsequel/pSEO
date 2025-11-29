import requests
from bs4 import BeautifulSoup
import json
import time
import random
import re

def scrape_all_errors():
    """
    Scrape ALL error codes from all brands on the washing machine error codes page.
    """
    url = "https://www.applianceservicecentre.co.uk/washing-machine-error-codes"
    
    print(f"Fetching {url}...")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Regex patterns for different brand formats
    patterns = [
        re.compile(r"^\s*([A-Za-z0-9]+)\s*[—–-]\s*([^:]+):\s*(.+)$"),  # Whirlpool: F01 — Title: Description
        re.compile(r"^\s*([A-Za-z0-9]+)\s*:\s*([^-]+)\s*-\s*(.+)$")    # Samsung: DC: Title - Description
    ]

    errors = []
    seen_codes = set()  # Track unique codes across all brands
    
    # List of all brands to scrape
    brands = [
        "Beko Error Codes",
        "Hotpoint Error Codes",
        "Samsung Error Codes",
        "Indesit Error Codes",
        "LG Error Codes",
        "Whirlpool Error Codes",
        "Bosch Error Codes",
        "Hoover Error Codes",
        "Bush Error Codes",
        "Candy Error Codes",
        "Electrolux Error Codes",
        "Miele Error Codes",
        "AEG Error Codes",
        "Zanussi Error Codes",
        "Siemens Error Codes",
        "Neff Error Codes"
    ]
    
    for brand_header in brands:
        # Extract brand name from header (e.g. "Whirlpool Error Codes" -> "Whirlpool")
        brand_name = brand_header.replace(" Error Codes", "")
        
        print(f"\nScraping {brand_header}...")
        header = soup.find(string=re.compile(brand_header))
        
        if not header:
            print(f"  ❌ Could not find '{brand_header}' section.")
            continue

        # Try to find the content div for this brand
        content_div = None
        
        # Map of brands to their first known error codes
        first_code_map = {
            "Whirlpool": "F01",
            "Samsung": "4E",
            "LG": "IE",
            "Hotpoint": "F01",
            "Indesit": "F01",
            "Beko": "E40",
            "Bosch": "F16",
            "AEG": "E10",
            "Zanussi": "E10",
            "Electrolux": "E10",
            "Siemens": "F16",
            "Miele": "F01",
            "Hoover": "E01",
            "Candy": "E01",
            "Bush": "E01",
            "Neff": "F16"
        }
        
        first_code = first_code_map.get(brand_name)
        
        if first_code:
            code_node = soup.find(string=re.compile(first_code))
            if code_node:
                temp = code_node.find_parent()
                if temp and temp.parent:
                    content_div = temp.parent
                else:
                    content_div = temp
            else:
                print(f"  ⚠️  Could not find first code {first_code} for {brand_header}")
        
        # Fallback: Try to find the next div after the header's container
        if not content_div:
            curr = header.find_parent()
            if curr and curr.parent:
                for sibling in curr.parent.next_siblings:
                    if sibling.name == 'div':
                        content_div = sibling
                        break
        
        if not content_div:
            print(f"  ❌ Could not find content div for {brand_header}")
            continue

        print(f"  ✓ Found content div for {brand_header}")
        
        text_content = content_div.get_text(separator="\n")
        brand_lines = text_content.split("\n")
        
        brand_count = 0
        for line in brand_lines:
            line = line.strip()
            if not line:
                continue
                
            match = None
            for p in patterns:
                match = p.match(line)
                if match:
                    break
            
            if match:
                code = match.group(1).strip()
                title = match.group(2).strip()
                fixes = match.group(3).strip()
                
                # Create unique identifier: brand-code
                unique_id = f"{brand_name}-{code}".lower()
                
                if unique_id not in seen_codes:
                    seen_codes.add(unique_id)
                    slug = code.lower().replace(" ", "-")
                    
                    errors.append({
                        "code": code,
                        "brand": brand_name,
                        "title": title,
                        "fixes": fixes,
                        "slug": slug
                    })
                    brand_count += 1
        
        print(f"  ✓ Scraped {brand_count} codes from {brand_header}")
        
        # Rate limiting
        time.sleep(random.uniform(0.5, 1.5))
    
    print(f"\n{'='*60}")
    print(f"TOTAL: Found {len(errors)} unique error codes across {len(brands)} brands")
    print(f"{'='*60}\n")
    
    return errors

def main():
    errors = scrape_all_errors()
    
    # Save to JSON
    output_path = "src/data/errors.json"
    with open(output_path, 'w') as f:
        json.dump(errors, f, indent=2)
    
    print(f"✅ Saved {len(errors)} error codes to {output_path}")
    
    # Show sample
    if errors:
        print("\nSample entries:")
        for error in errors[:5]:
            print(f"  {error['brand']} {error['code']}: {error['title'][:50]}...")

if __name__ == "__main__":
    main()
