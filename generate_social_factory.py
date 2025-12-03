#!/usr/bin/env python3
"""
Social Factory - Generate Pinterest-ready images and bulk upload CSV
"""

import json
import os
from pathlib import Path
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# Configuration
SITES = {
    'appliance': {
        'data_file': 'src/data/errors.json',
        'base_url': 'https://applianceerror.com',
        'color': '#3B82F6',  # Blue
        'name': 'Appliance'
    },
    'car': {
        'data_file': 'src/data/layoffs.json',
        'base_url': 'https://errorcodehelp.com',
        'color': '#6366F1',  # Indigo
        'name': 'Car/OBD2'
    },
    'saas': {
        'data_file': 'src/data/saas.json',
        'base_url': 'https://saasguide.org',
        'color': '#A855F7',  # Purple
        'name': 'SaaS'
    }
}

# Image settings
IMAGE_WIDTH = 1080
IMAGE_HEIGHT = 1920
OUTPUT_DIR = Path('public/social')
RECORDS_PER_SITE = 50

def create_social_image(title, color, output_path):
    """Create a Pinterest-optimized social image with title text"""
    # Create image with solid background
    img = Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT), color)
    draw = ImageDraw.Draw(img)
    
    # Try to use a nice font, fall back to default if not available
    try:
        # Try common system fonts
        font_size = 80
        font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', font_size)
    except:
        try:
            font = ImageFont.truetype('/Library/Fonts/Arial Bold.ttf', 80)
        except:
            # Fall back to default font
            font = ImageFont.load_default()
    
    # Wrap text to fit within image width with padding
    max_width = IMAGE_WIDTH - 100  # 50px padding on each side
    words = title.split()
    lines = []
    current_line = []
    
    for word in words:
        test_line = ' '.join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        text_width = bbox[2] - bbox[0]
        
        if text_width <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]
    
    if current_line:
        lines.append(' '.join(current_line))
    
    # Calculate total text height
    line_height = 100
    total_height = len(lines) * line_height
    
    # Start position (centered vertically)
    y = (IMAGE_HEIGHT - total_height) // 2
    
    # Draw each line centered
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        x = (IMAGE_WIDTH - text_width) // 2
        
        # Draw text with shadow for better readability
        draw.text((x + 2, y + 2), line, font=font, fill='#000000')  # Shadow
        draw.text((x, y), line, font=font, fill='#FFFFFF')  # Main text
        
        y += line_height
    
    # Save image
    img.save(output_path, 'PNG', optimize=True)

def main():
    """Main function to generate social images and CSV"""
    print("🎨 Social Factory - Starting...")
    print("=" * 60)
    
    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"✓ Created output directory: {OUTPUT_DIR}")
    
    # Collect all data for CSV
    csv_data = []
    total_images = 0
    
    # Process each site
    for site_key, site_config in SITES.items():
        print(f"\n📊 Processing {site_config['name']} site...")
        print(f"   Data file: {site_config['data_file']}")
        print(f"   Color: {site_config['color']}")
        
        # Load data
        with open(site_config['data_file'], 'r') as f:
            data = json.load(f)
        
        # Process first N records
        records_to_process = data[:RECORDS_PER_SITE]
        print(f"   Processing {len(records_to_process)} records...")
        
        for idx, record in enumerate(records_to_process, 1):
            slug = record['slug']
            title = record['title']
            
            # Generate image
            image_filename = f"{slug}.png"
            image_path = OUTPUT_DIR / image_filename
            
            try:
                create_social_image(title, site_config['color'], image_path)
                total_images += 1
                
                # Add to CSV data
                csv_data.append({
                    'Title': title,
                    'Description': f"Click to see the full guide for {title}. Get expert insights and solutions.",
                    'Link': f"{site_config['base_url']}/{slug}",
                    'Image URL': f"{site_config['base_url']}/social/{image_filename}"
                })
                
                if idx % 10 == 0:
                    print(f"   ✓ Created {idx}/{len(records_to_process)} images")
                    
            except Exception as e:
                print(f"   ✗ Error creating image for {slug}: {e}")
        
        print(f"   ✓ Completed {site_config['name']} site: {len(records_to_process)} images")
    
    # Generate CSV
    print(f"\n📝 Generating Pinterest CSV...")
    df = pd.DataFrame(csv_data)
    csv_filename = 'pinterest_upload_master.csv'
    df.to_csv(csv_filename, index=False)
    print(f"   ✓ CSV saved: {csv_filename}")
    print(f"   ✓ Total rows: {len(df)}")
    
    # Summary
    print("\n" + "=" * 60)
    print("✅ Social Factory Complete!")
    print(f"   📸 Images created: {total_images}")
    print(f"   📁 Images directory: {OUTPUT_DIR}")
    print(f"   📊 CSV file: {csv_filename}")
    print(f"   🎯 Ready for Pinterest bulk upload!")
    print("=" * 60)

if __name__ == '__main__':
    main()
