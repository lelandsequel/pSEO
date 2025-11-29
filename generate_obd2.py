import json

# Configuration
OUTPUT_FILE = 'src/data/layoffs.json'
START_CODE = 1
END_CODE = 500

def get_obd2_description(code_num):
    """Return a realistic description for standard OBD2 codes."""
    # Simplified logic for demo purposes, mapping ranges to systems
    if code_num < 100:
        return "Fuel and Air Metering"
    elif code_num < 200:
        return "Fuel and Air Metering (Injector Circuit)"
    elif code_num < 300:
        return "Ignition System or Misfire"
    elif code_num < 400:
        return "Auxiliary Emission Controls"
    elif code_num < 500:
        return "Vehicle Speed Control and Idle Control System"
    else:
        return "Computer Output Circuits"

def generate_obd2_codes():
    codes = []
    print(f"🚀 Generating OBD2 Codes P{START_CODE:04d} - P{END_CODE:04d}...")

    for i in range(START_CODE, END_CODE + 1):
        code_str = f"P{i:04d}"
        system = get_obd2_description(i)
        
        # Specific overrides for common codes to make it look real
        if i == 300:
            title_desc = "Random/Multiple Cylinder Misfire Detected"
        elif i == 171:
            title_desc = "System Too Lean (Bank 1)"
        elif i == 420:
            title_desc = "Catalyst System Efficiency Below Threshold (Bank 1)"
        elif i == 442:
            title_desc = "Evaporative Emission Control System Leak Detected (Small Leak)"
        elif i == 101:
            title_desc = "Mass or Volume Air Flow Circuit Range/Performance"
        else:
            title_desc = f"{system} Generic Error"

        title = f"{code_str}: {title_desc}"
        slug = f"{code_str.lower()}-obd2-code"
        
        content = (
            f"The {code_str} code indicates a issue within the {system}. "
            f"This is a generic powertrain code, which means it covers all makes and models of vehicles. "
            f"When this code is triggered, the Check Engine Light will illuminate on your dashboard. "
            f"Diagnosing {code_str} typically requires an OBD2 scanner to read the specific freeze frame data."
        )

        codes.append({
            "slug": slug,
            "brand": "OBD2",
            "title": title,
            "content": content,
            "code": code_str
        })
        
        if i % 50 == 0:
            print(f"  ... Generated {i} codes")

    return codes

def main():
    data = generate_obd2_codes()
    
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(data, f, indent=2)
        
    print(f"✅ Successfully saved {len(data)} OBD2 codes to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
