import json
import itertools

# Configuration
OUTPUT_FILE = 'src/data/saas.json'

# AI Tool Categories
AI_TOOLS = {
    "AI Writing": ["ChatGPT", "Jasper", "Copy.ai", "Writesonic", "Claude", "Gemini"],
    "AI Image": ["Midjourney", "DALL-E 3", "Stable Diffusion", "Leonardo.ai", "Adobe Firefly"],
    "AI Video": ["Runway", "Pika", "HeyGen", "Synthesia", "Sora"],
    "AI Coding": ["GitHub Copilot", "Cursor", "Tabnine", "Replit Ghostwriter"],
    "AI Productivity": ["Notion AI", "Mem.ai", "Otter.ai", "Fireflies.ai"]
}

def generate_content(tool_a, tool_b, category):
    """Generate realistic AI tool comparison content."""
    if "Writing" in category:
        return (
            f"Comparing {tool_a} and {tool_b} for AI-powered content creation in 2025. "
            f"{tool_a} excels in output quality and natural language generation, while {tool_b} offers competitive pricing with a flexible credit system. "
            f"Both tools provide free trials, but differ in their subscription models and feature sets. "
            f"Consider your content volume, budget, and specific use cases (blog posts, social media, marketing copy) when choosing between these AI writers."
        )
    elif "Image" in category:
        return (
            f"Comparing {tool_a} and {tool_b} for AI image generation in 2025. "
            f"{tool_a} is known for photorealistic outputs and artistic control, while {tool_b} provides faster generation speeds and easier prompting. "
            f"Pricing models vary: subscription vs. credit-based systems. Both offer free trials to test quality. "
            f"Choose based on your needs: commercial use rights, image resolution, style flexibility, and generation speed."
        )
    elif "Video" in category:
        return (
            f"Comparing {tool_a} and {tool_b} for AI video generation in 2025. "
            f"{tool_a} offers advanced motion control and cinematic quality, while {tool_b} focuses on ease of use and quick turnaround. "
            f"Both platforms support text-to-video and image-to-video workflows, but pricing and export quality differ. "
            f"Consider your video production needs: marketing content, social media clips, or professional filmmaking."
        )
    elif "Coding" in category:
        return (
            f"Comparing {tool_a} and {tool_b} for AI-assisted coding in 2025. "
            f"{tool_a} provides intelligent code completion and context-aware suggestions, while {tool_b} offers multi-language support and faster response times. "
            f"Both integrate with popular IDEs, but pricing models and accuracy rates vary. Free trials available. "
            f"Choose based on your tech stack, coding frequency, and team collaboration needs."
        )
    else:  # Productivity
        return (
            f"Comparing {tool_a} and {tool_b} for AI productivity tools in 2025. "
            f"{tool_a} excels in workflow automation and smart organization, while {tool_b} focuses on meeting transcription and note-taking accuracy. "
            f"Both offer free tiers with limited features, but premium plans unlock advanced AI capabilities. "
            f"Consider your primary use case: meeting notes, task management, or knowledge organization."
        )

def generate_ai_comparisons():
    comparisons = []
    print("🚀 Generating AI Tool Comparisons...")

    for category, tools in AI_TOOLS.items():
        # Generate all unique pairs
        pairs = list(itertools.combinations(tools, 2))
        
        for tool_a, tool_b in pairs:
            slug = f"{tool_a.lower().replace(' ', '-').replace('.', '')}-vs-{tool_b.lower().replace(' ', '-').replace('.', '')}"
            title = f"{tool_a} vs {tool_b}: Best AI Tool for 2025?"
            content = generate_content(tool_a, tool_b, category)
            
            comparisons.append({
                "slug": slug,
                "brand": "AI Tool Comparison",
                "title": title,
                "content": content,
                "code": "VS",
                "category": category
            })
            
        print(f"  ✅ Generated {len(pairs)} comparisons for {category}")
    
    return comparisons

def main():
    # Load existing data
    try:
        with open(OUTPUT_FILE, 'r') as f:
            existing_data = json.load(f)
            print(f"📄 Loaded {len(existing_data)} existing comparisons.")
    except FileNotFoundError:
        existing_data = []
        print("📄 No existing data found. Starting fresh.")

    # Generate new comparisons
    new_comparisons = generate_ai_comparisons()
    
    # Check for duplicates
    existing_slugs = set(item['slug'] for item in existing_data)
    unique_new = [c for c in new_comparisons if c['slug'] not in existing_slugs]
    
    print(f"\n📊 Summary:")
    print(f"  - New comparisons generated: {len(new_comparisons)}")
    print(f"  - Duplicates filtered: {len(new_comparisons) - len(unique_new)}")
    print(f"  - Unique comparisons to add: {len(unique_new)}")
    
    # Combine and save
    all_data = existing_data + unique_new
    
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(all_data, f, indent=2)
        
    print(f"\n✅ Successfully saved {len(all_data)} total comparisons to {OUTPUT_FILE}")
    print(f"🎉 Added {len(unique_new)} new AI tool comparisons!")

if __name__ == "__main__":
    main()
