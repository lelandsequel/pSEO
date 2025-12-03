import pandas as pd
from datetime import datetime
import urllib.request

# 1. Get Today's Date
today = datetime.now().strftime('%Y-%m-%d')

# 2. Define Columns (Standard Template)
columns = [
    'Action', 'Campaign ID', 'Campaign Objective', 'Campaign Name', 'Campaign Status', 'Lifetime Spend Limit',
    'Daily Spend Limit', 'Campaign Order Line ID', 'Campaign Third Party Tracking Urls', 'Campaign Budget',
    'Default Ad Group Budget', 'Campaign Start Date', 'Campaign Start Time', 'Campaign End Date',
    'Campaign End Time', 'Performance+ daily budget', 'Campaign Keyword (Match Type NEGATIVE_PHRASE)',
    'Campaign Keyword (Match Type NEGATIVE_EXACT)', 'Ad Group ID', 'Ad Group Name', 'Ad Group Start Date*',
    'Ad Group Start Time', 'Ad Group End Date*', 'Ad Group End Time', 'Ad Group Budget', 'Ad Group Pacing Type',
    'Ad Group Budget Type', 'Ad Group Status', 'Max Bid', 'Monthly Frequency Cap', 'Ad Group Third Party Tracking Urls',
    'Performance+ Targeting', 'Ad Placement', 'Goal Value', 'Conversion Tag ID', 'Conversion Event',
    'Conversion Optimization', 'Click Window Days', 'Engagement Window Days', 'View Window Days',
    'Frequency Target Time Range', 'Frequency Target', 'Bid strategy type', 'Targeting Template ID', 'Promo Id',
    'Locations', 'Geos', 'Genders', 'AgeBuckets', 'Languages', 'Devices', 'Interests', 'Included Audiences',
    'Excluded Audiences', 'Dynamic Retargeting Lookback', 'Dynamic Retargeting Exclusion',
    'Dynamic Retargeting Event Tag Types', 'Ad Group Keyword (Match Type BROAD)', 'Ad Group Keyword (Match Type EXACT)',
    'Ad Group Keyword (Match Type PHRASE)', 'Ad Group Keyword (Match Type NEGATIVE_PHRASE)',
    'Ad Group Keyword (Match Type NEGATIVE_EXACT)', 'Existing Pin ID', 'Media File Name', 'Pin Title',
    'Pin Description', 'Organic Pin URL', 'Image Alternative Text', 'Is Ad-only Pin', 'Promoted Pin Status',
    'Promoted Pin ID', 'Ad Format', 'Promoted Pin Name', 'Promoted Pin URL', 'Promoted Pin Third Party Tracking Urls',
    'Is Removable Pin Promotion', 'Carousel Card 1 Image File Name', 'Carousel Card 1 Title',
    'Carousel Card 1 Description', 'Carousel Card 1 Organic Pin URL', 'Carousel Card 1 Destination URL',
    'Carousel Card 1 Android Deep Link', 'Carousel Card 1 iOS Deep Link', 'Carousel Card 2 Image File Name',
    'Carousel Card 2 Title', 'Carousel Card 2 Description', 'Carousel Card 2 Organic Pin URL',
    'Carousel Card 2 Destination URL', 'Carousel Card 2 Android Deep Link', 'Carousel Card 2 iOS Deep Link',
    'Carousel Card 3 Image File Name', 'Carousel Card 3 Title', 'Carousel Card 3 Description',
    'Carousel Card 3 Organic Pin URL', 'Carousel Card 3 Destination URL', 'Carousel Card 3 Android Deep Link',
    'Carousel Card 3 iOS Deep Link', 'Carousel Card 4 Image File Name', 'Carousel Card 4 Title',
    'Carousel Card 4 Description', 'Carousel Card 4 Organic Pin URL', 'Carousel Card 4 Destination URL',
    'Carousel Card 4 Android Deep Link', 'Carousel Card 4 iOS Deep Link', 'Carousel Card 5 Image File Name',
    'Carousel Card 5 Title', 'Carousel Card 5 Description', 'Carousel Card 5 Organic Pin URL',
    'Carousel Card 5 Destination URL', 'Carousel Card 5 Android Deep Link', 'Carousel Card 5 iOS Deep Link',
    'Collections Secondary Creative Destination Url', 'Title Card Organic PinID', 'Card 1 Organic PinID',
    'Card 2 Organic PinID', 'Card 3 Organic PinID', 'Card 4 Organic PinID', 'Quiz pin question 1 text',
    'Question 1 options text', 'Quiz pin question 2 text', 'Question 2 options text', 'Quiz pin question 3 text',
    'Question 3 options text', 'Result 1 organic Pin ID', 'Result 1 iOS deep link url',
    'Result 1 Android deep link url', 'Result 1 destination url', 'Result 2 organic Pin ID',
    'Result 2 iOS deep link url', 'Result 2 Android deep link url', 'Result 2 destination url',
    'Result 3 organic Pin ID', 'Result 3 iOS deep link url', 'Result 3 Android deep link url',
    'Result 3 destination url', 'Grid Click Type', 'CTA Selection', 'Keyword Status',
    'Keyword (Match Type BROAD)', 'Keyword (Match Type EXACT)', 'Keyword (Match Type PHRASE)',
    'Keyword (Match Type NEGATIVE_PHRASE)', 'Keyword (Match Type NEGATIVE_EXACT)', 'Product Group ID',
    'Product Group Reference ID', 'Product Group Name', 'Product Group Status', 'Tracking Template',
    'Shopping Collections Hero Pin ID', 'Shopping Collections Hero Pin URL', 'Slideshow Collections Title',
    'Slideshow Collections Description', 'Status', 'Version'
]

# 3. Generate Data Rows
rows = []

# --- ROW 1: CAMPAIGN ---
campaign_row = {col: '' for col in columns}
campaign_row['Action'] = 'CREATE'
campaign_row['Campaign Name'] = 'PSEO Traffic Gen'
campaign_row['Campaign Objective'] = 'AWARENESS'
campaign_row['Campaign Status'] = 'ACTIVE'
campaign_row['Campaign Start Date'] = today
campaign_row['Campaign Start Time'] = '00:00'
campaign_row['Daily Spend Limit'] = '1000000'
rows.append(campaign_row)

# --- ROW 2: AD GROUP ---
adgroup_row = {col: '' for col in columns}
adgroup_row['Action'] = 'CREATE'
adgroup_row['Campaign Name'] = 'PSEO Traffic Gen'
adgroup_row['Ad Group Name'] = 'PSEO Pins'
adgroup_row['Ad Group Status'] = 'ACTIVE'
adgroup_row['Ad Group Start Date*'] = today
adgroup_row['Ad Group Start Time'] = '00:00'
adgroup_row['Ad Group Budget Type'] = 'DAILY'
adgroup_row['Ad Group Budget'] = '1000000'
adgroup_row['Bid strategy type'] = 'AUTOMATIC_BID'
rows.append(adgroup_row)

# --- ROW 3+: PINS ---
# Site A: Appliance Error
for i in range(1, 51):
    slug = f"whirlpool-f{i:02d}-error"
    url = f"https://www.applianceerror.com/{slug}"
    pin_row = {col: '' for col in columns}
    pin_row['Action'] = 'CREATE'
    pin_row['Ad Group Name'] = 'PSEO Pins'
    pin_row['Pin Title'] = f"Fix Whirlpool Error F{i:02d}"
    pin_row['Pin Description'] = f"How to fix Whirlpool Washer Error F{i:02d}. Step-by-step guide."
    pin_row['Media File Name'] = f"https://www.applianceerror.com/social/{slug}.png"
    pin_row['Promoted Pin URL'] = url
    pin_row['Organic Pin URL'] = url  # <--- ADDED: Required for new pins
    pin_row['Image Alternative Text'] = f"Fix Whirlpool Error F{i:02d}" # <--- ADDED: Good practice
    pin_row['Ad Format'] = 'IMAGE'
    pin_row['Promoted Pin Status'] = 'ACTIVE'
    pin_row['Is Ad-only Pin'] = 'FALSE'
    rows.append(pin_row)

# Site B: Error Code Help
for i in range(1, 51):
    slug = f"p{i:04d}-obd2-code"
    url = f"https://www.errorcodehelp.com/{slug}"
    pin_row = {col: '' for col in columns}
    pin_row['Action'] = 'CREATE'
    pin_row['Ad Group Name'] = 'PSEO Pins'
    pin_row['Pin Title'] = f"Fix OBD2 Code P{i:04d}"
    pin_row['Pin Description'] = f"Meaning, Causes, and Fixes for OBD2 Code P{i:04d}."
    pin_row['Media File Name'] = f"https://www.errorcodehelp.com/social/{slug}.png"
    pin_row['Promoted Pin URL'] = url
    pin_row['Organic Pin URL'] = url # <--- ADDED
    pin_row['Image Alternative Text'] = f"Fix OBD2 Code P{i:04d}" # <--- ADDED
    pin_row['Ad Format'] = 'IMAGE'
    pin_row['Promoted Pin Status'] = 'ACTIVE'
    pin_row['Is Ad-only Pin'] = 'FALSE'
    rows.append(pin_row)

# Site C: SaaS Guide
for i in range(1, 51):
    slug = f"tool-{i}-vs-tool-{i+1}"
    url = f"https://www.saasguide.org/{slug}"
    pin_row = {col: '' for col in columns}
    pin_row['Action'] = 'CREATE'
    pin_row['Ad Group Name'] = 'PSEO Pins'
    pin_row['Pin Title'] = f"Tool {i} vs Tool {i+1} Comparison"
    pin_row['Pin Description'] = "Unbiased comparison of features, pricing, and pros/cons."
    pin_row['Media File Name'] = f"https://www.saasguide.org/social/{slug}.png"
    pin_row['Promoted Pin URL'] = url
    pin_row['Organic Pin URL'] = url # <--- ADDED
    pin_row['Image Alternative Text'] = f"Tool {i} vs Tool {i+1} Comparison" # <--- ADDED
    pin_row['Ad Format'] = 'IMAGE'
    pin_row['Promoted Pin Status'] = 'ACTIVE'
    pin_row['Is Ad-only Pin'] = 'FALSE'
    rows.append(pin_row)

# 4. Create DataFrame & Export
df_final = pd.DataFrame(rows, columns=columns)
output_file = 'pinterest_bulk_upload_v8_FIXED.csv'
df_final.to_csv(output_file, index=False)

print(f"✅ Created {output_file}")
print(f"   - Structure: Hierarchical (Campaign -> Ad Group -> Pins)")
print(f"   - Added 'Organic Pin URL' to fix Error 1619")
print(f"   - Added 'Image Alternative Text'")
print(f"   - Total Rows: {len(df_final)}")

# 5. Check Image Accessibility (Sample)
print("\n🔍 Checking image accessibility...")
sample_url = rows[2]['Media File Name']
try:
    req = urllib.request.Request(sample_url, method='HEAD')
    req.add_header('User-Agent', 'Mozilla/5.0')
    
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                print(f"   ✅ Image verified accessible: {sample_url}")
            else:
                print(f"   ⚠️ Image check returned status: {response.status} for {sample_url}")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"   ⚠️ WARNING: Image returned 404 Not Found: {sample_url}")
            print("      Pinterest will FAIL to upload images if they are not live.")
            print("      Please ensure your deployment has finished and 'public/social' is live.")
        else:
            print(f"   ⚠️ Image check returned status: {e.code} for {sample_url}")
            
except Exception as e:
    print(f"   ⚠️ Could not check image: {e}")
