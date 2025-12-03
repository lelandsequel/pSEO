import pandas as pd
from datetime import datetime

# 1. Get Today's Date for the Campaign Start
today = datetime.now().strftime('%Y-%m-%d')

# 2. Define the Full Column List (Exact Match to Template)
template_columns = [
    'Campaign ID', 'Campaign Objective', 'Campaign Name', 'Campaign Status', 'Lifetime Spend Limit',
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

# 3. Generate Data
data = []

# Site A: Appliance Error (50 records)
for i in range(1, 51):
    slug = f"whirlpool-f{i:02d}-error"
    data.append({
        "Pin Title": f"Fix Whirlpool Error F{i:02d}",
        "Pin Description": f"How to fix Whirlpool Washer Error F{i:02d}. Step-by-step guide.",
        "Promoted Pin URL": f"https://applianceerror.com/{slug}",
        "Media File Name": f"https://applianceerror.com/social/{slug}.png"
    })

# Site B: Error Code Help (50 records)
for i in range(1, 51):
    slug = f"p{i:04d}-obd2-code"
    data.append({
        "Pin Title": f"Fix OBD2 Code P{i:04d}",
        "Pin Description": f"Meaning, Causes, and Fixes for OBD2 Code P{i:04d}.",
        "Promoted Pin URL": f"https://errorcodehelp.com/{slug}",
        "Media File Name": f"https://errorcodehelp.com/social/{slug}.png"
    })

# Site C: SaaS Guide (50 records)
for i in range(1, 51):
    slug = f"tool-{i}-vs-tool-{i+1}"
    data.append({
        "Pin Title": f"Tool {i} vs Tool {i+1} Comparison",
        "Pin Description": "Unbiased comparison of features, pricing, and pros/cons.",
        "Promoted Pin URL": f"https://saasguide.org/{slug}",
        "Media File Name": f"https://saasguide.org/social/{slug}.png"
    })

# 4. Create Final DataFrame
df_final = pd.DataFrame(columns=template_columns)
df_source = pd.DataFrame(data)

# Map Content
df_final['Pin Title'] = df_source['Pin Title']
df_final['Pin Description'] = df_source['Pin Description']
df_final['Media File Name'] = df_source['Media File Name']
df_final['Promoted Pin URL'] = df_source['Promoted Pin URL']

# Map Required Campaign/Ad Group Fields
df_final['Campaign Name'] = "PSEO Traffic Gen"
df_final['Campaign Objective'] = "AWARENESS"
df_final['Campaign Status'] = "ACTIVE"  # Changed to ACTIVE to ensure it processes
df_final['Campaign Start Date'] = today
df_final['Campaign Start Time'] = "00:00"

df_final['Ad Group Name'] = "PSEO Pins"
df_final['Ad Group Status'] = "ACTIVE"
df_final['Ad Group Start Date*'] = today
df_final['Ad Group Start Time'] = "00:00"
df_final['Ad Group Budget Type'] = "DAILY"
df_final['Ad Group Budget'] = "1000000"  # $10.00 USD (in micros)
df_final['Bid strategy type'] = "AUTOMATIC_BID"
df_final['Ad Format'] = "IMAGE"
df_final['Promoted Pin Status'] = "ACTIVE"
df_final['Is Ad-only Pin'] = "FALSE"  # Important: Makes them Organic Pins too

# 5. Export
df_final.to_csv('pinterest_bulk_upload_v2.csv', index=False)
print("✅ Created 'pinterest_bulk_upload_v2.csv'")
print(f"   📅 Campaign Start Date: {today}")
print(f"   💰 Daily Budget: $10.00")
print(f"   📊 Total Pins: {len(df_final)}")
print(f"   🎯 Status: ACTIVE (ready to run)")
