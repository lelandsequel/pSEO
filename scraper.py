import requests
from bs4 import BeautifulSoup
import json
import os
import re

URL = "https://www.applianceservicecentre.co.uk/washing-machine-error-codes"
OUTPUT_FILE = "src/data/errors.json"

def scrape_errors():
    print(f"Fetching {URL}...")
    try:
        response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching URL: {e}")
        return

    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find the Whirlpool section
    # Based on observation, it's likely an accordion button followed by a content div.
    # We look for the text "Whirlpool Error Codes"
    
    # Regex for "Code — Title: Description"
    # Example: "F01 — Electronic circuit board fault: This code indicates..."
    # Note the em-dash or en-dash.
    # We'll try to match the start of the line.
    
    # Regex for "Code — Title: Description"
    # Example: "F01 — Electronic circuit board fault: This code indicates..."
    # Note the em-dash or en-dash.
    # We'll try to match the start of the line.
    
    # Relaxed pattern: Code followed by dash, then Title, then colon, then Description
    # We will handle different dash types
    patterns = [
        re.compile(r"^\s*([A-Za-z0-9]+)\s*[—–-]\s*([^:]+):\s*(.+)$"), # Whirlpool: F01 — Title: Description
        re.compile(r"^\s*([A-Za-z0-9]+)\s*:\s*([^-]+)\s*-\s*(.+)$")   # Samsung: DC: Title - Description
    ]

    errors = []
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
        "AEG Error Codes"
    ]
    
    for brand_header in brands:
        # Extract brand name from header (e.g. "Whirlpool Error Codes" -> "Whirlpool")
        brand_name = brand_header.replace(" Error Codes", "")
        
        print(f"Looking for {brand_header}...")
        header = soup.find(string=re.compile(brand_header))
        
        if not header:
            print(f"Could not find '{brand_header}' section.")
            continue

        print("Found header:", header)
        
        content_div = None
        
        # Try to find the container
        # Heuristic: look for a known code in that section or just the next large div
        # For Samsung, codes are like "4E", "5E", "UE"
        # For LG, "IE", "OE"
        
        # We can try to find the next sibling div of the header's parent
        # Or use the same heuristic as before but adapted
        
        # Let's try to find the next sibling element that contains text with ":"
        
        curr = header.find_parent()
        found_container = False
        
        # Traverse up and look for siblings
        # This is tricky because the structure might be nested
        
        # Let's try a different approach:
        # Find the header, then find all text nodes after it until the next header
        
        # Actually, the previous logic worked for Whirlpool because F01 and F02 were found.
        # Let's try to find the first code of the brand.
        
        first_code = None
        if "Whirlpool" in brand_header:
            first_code = "F01"
        elif "Samsung" in brand_header:
            first_code = "4E" # Common Samsung code
        elif "LG" in brand_header:
            first_code = "IE" # Common LG code
        elif "Hotpoint" in brand_header:
            first_code = "F01"
        elif "Indesit" in brand_header:
            first_code = "F01"
        elif "Beko" in brand_header:
            first_code = "C1" # Guessing common Beko code or just try to find the container via siblings
        elif "Bosch" in brand_header:
            first_code = "F16"
        
        # If we have a first code, try to find it
        if first_code:
            code_node = soup.find(string=re.compile(first_code))
            if code_node:
                # Find the container that holds this code
                # We assume it holds others too
                # We go up until we hit a div that has multiple children or text
                temp = code_node.find_parent()
                # Go up 2 levels
                if temp and temp.parent:
                     content_div = temp.parent
                else:
                     content_div = temp
            else:
                print(f"Could not find first code {first_code} for {brand_header}")
                # Fallback to sibling traversal
        
        if not content_div:
             # Fallback: Try to find the next div after the header's container
             # This is risky but might work if the structure is consistent
             if curr and curr.parent:
                 # Look at next siblings of the parent (the button's parent)
                 for sibling in curr.parent.next_siblings:
                     if sibling.name == 'div':
                         content_div = sibling
                         break
        
        if not content_div:
            print(f"Could not find content div for {brand_header}")
            continue

        print(f"Found content div for {brand_header}")
        
        text_content = content_div.get_text(separator="\n")
        brand_lines = text_content.split("\n")
        
        print(f"Processing {len(brand_lines)} lines for {brand_header}")
        
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
                
                # Avoid duplicates across brands if codes are identical?
                # Actually, F01 for Whirlpool might be different from F01 for Indesit.
                # So we should keep them, maybe prepend brand to code in ID if we were using it as ID,
                # but here we use code as slug. This might cause collisions.
                # The user didn't specify how to handle collisions.
                # For now, I will just overwrite or append.
                # If I append, [slug].astro will need to handle it.
                # But [slug].astro uses `params: { slug: item.code }`.
                # If multiple items have same code, Astro might complain or just pick one.
                # To avoid this, I should probably make the slug unique, e.g. "brand-code".
                # But the user asked for "F01", not "whirlpool-F01".
                # I will stick to the code for now, but maybe prioritize the first one found or just let them overwrite.
                # Wait, if I want to scale, I should probably support multiple brands.
                # But the current architecture `src/pages/[...slug].astro` maps `slug` to `item.code`.
                # If I have two "F01"s, `getStaticPaths` will return two paths with same slug "F01".
                # Astro will error on duplicate paths.
                # I MUST make the slug unique if there are collisions.
                # I will prepend brand to slug if it already exists?
                # Or better: make the slug `brand-code` for all, or just `code` if unique.
                # The user request said "Visit http://localhost:4321/F01".
                # So I should try to keep it simple.
                # I will just skip duplicates for now to satisfy the "scale" requirement without breaking the app.
                
                if not any(e['code'] == code for e in errors):
                    errors.append({
                        "code": code,
                        "brand": brand_name,
                        "title": title,
                        "fixes": fixes
                    })
                
                if len(errors) >= 200: # Cap at 200
                    break
        
        if len(errors) >= 200:
            break
    
    print(f"Found {len(errors)} errors.")
    
    if not errors:
        print("No errors parsed.")

    # Ensure directory exists
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    
    with open(OUTPUT_FILE, "w") as f:
        json.dump(errors, f, indent=2)
    
    print(f"Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    scrape_errors()
