#!/usr/bin/env python3
"""
Migrate Aion links.json:
- Consolidate 260 categories → ~35 main categories with subcategories
- Integrate niche_websites.json
- Fix misplaced links
- Add 'added' date field
"""

import json
import os
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)

LINKS_FILE = os.path.join(ROOT_DIR, 'links.json')
NICHE_FILE = os.path.join(ROOT_DIR, 'niche_websites.json')
OUTPUT_FILE = os.path.join(ROOT_DIR, 'links.json')

CATEGORY_MAP = {
    # ── Technology ──────────────────────────────────
    "Programming & Dev": ("Technology", "Programming"),
    "AI & LLMs": ("Technology", "AI & Machine Learning"),
    "Frontend": ("Technology", "Web Development"),
    "CMS & Blogs": ("Technology", "Web Development"),
    "No-Code": ("Technology", "Web Development"),
    "Databases": ("Technology", "Databases"),
    "DevOps": ("Technology", "DevOps"),
    "Containers": ("Technology", "DevOps"),
    "Developer Tools": ("Technology", "Developer Tools"),
    "Terminal": ("Technology", "Command Line"),
    "Text & Terminal": ("Technology", "Command Line"),
    "OS & Distros": ("Technology", "Operating Systems"),
    "Operating Systems": ("Technology", "Operating Systems"),
    "Unix & Linux": ("Technology", "Operating Systems"),
    "Data Science": ("Technology", "Data & Analytics"),
    "Home Automation": ("Technology", "Home Automation"),
    "Robotics": ("Technology", "Robotics"),
    "Virtual Reality": ("Technology", "VR & AR"),
    "Indie Web & Personal Sites": ("Technology", "Indie Web"),
    "Open Source": ("Technology", "Open Source"),

    # ── Security & Privacy ─────────────────────────
    "Privacy & Security": ("Security", "Privacy Tools"),
    "Cybersecurity": ("Security", "Cybersecurity"),
    "Privacy": ("Security", "Privacy Tools"),
    "Privacy Services": ("Security", "Privacy Services"),
    "Hacking": ("Security", "Hacking"),
    "Dark Web": ("Security", "Dark Web"),
    "Lock Picking & Physical Security": ("Security", "Physical Security"),
    "Security Forums": ("Security", "Forums"),
    "Security & Hacking Forums": ("Security", "Forums"),

    # ── Creative ────────────────────────────────────
    "Creative": ("Creative", "General"),
    "Creative Tools": ("Creative", "Tools"),
    "Design": ("Creative", "Design"),
    "Graphics & Design": ("Creative", "Design"),
    "Typography": ("Creative", "Design"),
    "Digital Art": ("Creative", "Digital Art"),
    "ASCII Art & Text Art": ("Creative", "ASCII Art"),
    "ASCII Art": ("Creative", "ASCII Art"),
    "Pixel Art": ("Creative", "Pixel Art"),
    "Animation": ("Creative", "Animation"),
    "Film Making": ("Creative", "Film & Video"),
    "Photography": ("Creative", "Photography"),
    "Astrophotography": ("Creative", "Photography"),
    "Art & Creative Communities": ("Creative", "Communities"),
    "Art & Culture": ("Creative", "Art & Culture"),
    "Art Movements": ("Creative", "Art Movements"),
    "Street Art": ("Creative", "Street Art"),
    "Political Cartoons": ("Creative", "Cartoons"),
    "Miniature Painting": ("Creative", "Miniature Painting"),

    # ── Music ───────────────────────────────────────
    "Music": ("Music", "General"),
    "Experimental Music": ("Music", "Experimental"),
    "Synth & Electronic Music": ("Music", "Electronic"),
    "Punk & Hardcore Music": ("Music", "Punk & Hardcore"),
    "Music Production": ("Music", "Production"),
    "Vinyl Records": ("Music", "Vinyl & Records"),

    # ── Gaming ──────────────────────────────────────
    "Gaming & Emulation": ("Gaming", "General"),
    "Gaming Communities": ("Gaming", "Communities"),
    "Games & Gaming": ("Gaming", "General"),
    "Fun & Games": ("Gaming", "General"),
    "Retro Console Homebrew": ("Gaming", "Retro"),
    "Lost Arcade Games": ("Gaming", "Retro"),
    "Indie Game Dev Tools": ("Gaming", "Development"),
    "Esports": ("Gaming", "Esports"),
    "Text Adventures & MUDs": ("Gaming", "Text Adventures"),

    # ── Tabletop & Card Games ───────────────────────
    "RPGs": ("Tabletop", "RPGs"),
    "Tabletop Games": ("Tabletop", "Board Games"),
    "Card Games": ("Tabletop", "Card Games"),
    "Board Game Apps": ("Tabletop", "Board Games"),
    "Chess": ("Tabletop", "Chess"),
    "Go Game": ("Tabletop", "Go"),

    # ── Entertainment ───────────────────────────────
    "Entertainment": ("Entertainment", "General"),
    "Anime & Manga": ("Entertainment", "Anime & Manga"),
    "Video & Streaming": ("Entertainment", "Video"),
    "Podcasts & Audio": ("Entertainment", "Podcasts"),
    "Podcasting": ("Entertainment", "Podcasts"),

    # ── Books & Reading ─────────────────────────────
    "Books & Fiction": ("Books", "Fiction"),
    "Fiction & Writing": ("Books", "Writing"),
    "Bookbinding & Paper Crafts": ("Books", "Bookbinding"),

    # ── Internet Culture ────────────────────────────
    "Weird Web": ("Internet Culture", "Weird Web"),
    "Weird & Interesting": ("Internet Culture", "Weird Web"),
    "Weird & Bizarre Sites": ("Internet Culture", "Weird Web"),
    "Weird Taxonomy": ("Internet Culture", "Weird Web"),
    "Weird Maps": ("Internet Culture", "Weird Web"),
    "Weird Photos": ("Internet Culture", "Weird Web"),
    "Online Culture": ("Internet Culture", "Culture"),
    "Hacker Culture": ("Internet Culture", "Culture"),
    "Meme Archives": ("Internet Culture", "Memes"),
    "Meme & Internet Culture": ("Internet Culture", "Memes"),
    "Subculture Sites": ("Internet Culture", "Subcultures"),
    "Creepy & Horror": ("Internet Culture", "Horror"),
    "Weird Fiction & Liminal": ("Internet Culture", "Weird Fiction"),
    "Liminal & Dreams": ("Internet Culture", "Liminal Spaces"),
    "Abandoned Places": ("Internet Culture", "Abandoned Places"),
    "Paranormal & UFO": ("Internet Culture", "Paranormal"),
    "Zine Culture & Indie Publishing": ("Internet Culture", "Zines"),
    "Underground Comics & Zines": ("Internet Culture", "Underground Comics"),

    # ── Retro & Vintage ─────────────────────────────
    "Retro Computing": ("Retro", "Computing"),
    "Retro Communities": ("Retro", "Communities"),
    "Retrocomputing Hardware": ("Retro", "Hardware"),
    "Retro Computing & Vintage Software": ("Retro", "Software"),
    "Vintage Tech": ("Retro", "Vintage Tech"),
    "Dead Media & Obsolete Tech": ("Retro", "Dead Media"),
    "Dial-up & BBS Culture": ("Retro", "BBS & Dial-up"),
    "Retro Internet": ("Retro", "Internet"),
    "Demoscene": ("Retro", "Demoscene"),
    "Vintage Cars": ("Retro", "Vintage"),
    "Vintage Fashion": ("Retro", "Fashion"),
    "Typewriter Culture": ("Retro", "Typewriters"),
    "Morse Code & Telegraphy": ("Retro", "Telegraphy"),
    "Microcomputers & SBCs": ("Retro", "SBCs"),
    "Calculator Hacking": ("Retro", "Calculator Hacking"),
    "Lost TV & Radio": ("Retro", "Lost Media"),
    "Lost Inventions": ("Retro", "Lost Inventions"),
    "Obsolete Professions": ("Retro", "Obsolete Professions"),
    "Archives & Preservation": ("Retro", "Archives"),
    "Obscure Archives": ("Retro", "Archives"),
    "Web Archiving": ("Retro", "Web Archiving"),
    "Digital Hoarding": ("Retro", "Digital Hoarding"),

    # ── Science & Nature ────────────────────────────
    "Science & Research": ("Science", "General"),
    "Weather & Science": ("Science", "Weather"),
    "Weather": ("Science", "Weather"),
    "Earth Observation": ("Science", "Earth Observation"),
    "Astronomy": ("Science", "Astronomy"),
    "Space Cams": ("Science", "Space"),
    "Nature & Outdoors": ("Science", "Nature"),
    "Nature Cams": ("Science", "Nature"),
    "Botany & Plant Care": ("Science", "Botany"),
    "Mycology": ("Science", "Mycology"),
    "Ocean & Marine": ("Science", "Marine"),
    "Geography": ("Science", "Geography"),
    "Fringe Science": ("Science", "Fringe"),

    # ── Hobbies & Sports ────────────────────────────
    "Birdwatching": ("Hobbies", "Birdwatching"),
    "Climbing": ("Hobbies", "Climbing"),
    "Hiking": ("Hobbies", "Hiking"),
    "Cycling": ("Hobbies", "Cycling"),
    "Kayaking": ("Hobbies", "Water Sports"),
    "Surfing": ("Hobbies", "Water Sports"),
    "Scuba Diving": ("Hobbies", "Water Sports"),
    "Sailing": ("Hobbies", "Sailing"),
    "Fishing": ("Hobbies", "Fishing"),
    "Skateboarding": ("Hobbies", "Extreme Sports"),
    "Parkour": ("Hobbies", "Extreme Sports"),
    "Archery": ("Hobbies", "Archery"),
    "Fencing": ("Hobbies", "Fencing"),
    "Martial Arts": ("Hobbies", "Martial Arts"),
    "Golf": ("Hobbies", "Golf"),
    "Motorcycles": ("Hobbies", "Motorcycles"),
    "Drone Racing": ("Hobbies", "Drone Racing"),
    "Amateur Rocketry": ("Hobbies", "Rocketry"),
    "Geocaching": ("Hobbies", "Geocaching"),
    "Train Spotting": ("Hobbies", "Trains"),
    "Esoteric Sports": ("Hobbies", "Esoteric Sports"),
    "Niche Fitness": ("Hobbies", "Fitness"),
    "Escape Rooms": ("Hobbies", "Escape Rooms"),
    "Jigsaw Puzzles": ("Hobbies", "Puzzles"),
    "Brain Teasers": ("Hobbies", "Puzzles"),
    "Math Puzzles": ("Hobbies", "Puzzles"),
    "Word Games": ("Hobbies", "Word Games"),
    "Trivia": ("Hobbies", "Trivia"),
    "Magic & Illusion": ("Hobbies", "Magic"),
    "Bonsai": ("Hobbies", "Bonsai"),

    # ── Crafts & Making ─────────────────────────────
    "Traditional Crafts": ("Crafts", "Traditional"),
    "Woodworking": ("Crafts", "Woodworking"),
    "Metalworking": ("Crafts", "Metalworking"),
    "Electronics": ("Crafts", "Electronics"),
    "3D Printing": ("Crafts", "3D Printing"),
    "3D & Making": ("Crafts", "3D Printing"),
    "Leatherworking": ("Crafts", "Leatherworking"),
    "Pottery & Ceramics": ("Crafts", "Pottery"),
    "Jewelry Making": ("Crafts", "Jewelry"),
    "Knife Making": ("Crafts", "Knifemaking"),
    "Soap Making": ("Crafts", "Soap Making"),
    "Candle Making": ("Crafts", "Candle Making"),
    "Calligraphy": ("Crafts", "Calligraphy"),
    "Luthiery": ("Crafts", "Luthiery"),
    "Furniture Building": ("Crafts", "Furniture"),
    "Permaculture": ("Crafts", "Permaculture"),

    # ── Food & Drink ────────────────────────────────
    "Cooking": ("Food", "Cooking"),
    "Cooking & Food Niche Sites": ("Food", "Cooking"),
    "Beer Brewing": ("Food", "Beer"),
    "Bread Baking": ("Food", "Bread"),
    "Cheesemaking": ("Food", "Cheese"),
    "Cocktails": ("Food", "Cocktails"),
    "Wine": ("Food", "Wine"),
    "Fermentation": ("Food", "Fermentation"),
    "Foraging": ("Food", "Foraging"),
    "Meat Smoking": ("Food", "Smoking"),

    # ── Lifestyle ───────────────────────────────────
    "Lifestyle & Living": ("Lifestyle", "General"),
    "Survival & Homesteading": ("Lifestyle", "Homesteading"),
    "Alternative Medicine": ("Lifestyle", "Alternative Medicine"),
    "Yoga & Meditation": ("Lifestyle", "Wellness"),
    "Urban Farming": ("Lifestyle", "Urban Farming"),
    "Gardening": ("Lifestyle", "Gardening"),
    "Genealogy": ("Lifestyle", "Genealogy"),
    "Historical Enactment": ("Lifestyle", "Reenactment"),
    "Micronations": ("Lifestyle", "Micronations"),
    "Obscure Holidays": ("Lifestyle", "Obscure Holidays"),
    "Alternative Education": ("Lifestyle", "Education"),
    "Alternative Currencies": ("Lifestyle", "Alternative Currencies"),

    # ── Languages ───────────────────────────────────
    "Dying Languages": ("Languages", "Dying Languages"),
    "Constructed Languages": ("Languages", "Constructed"),
    "Language & Etymology": ("Languages", "Etymology"),
    "Language Learning": ("Languages", "Learning"),

    # ── Communication ───────────────────────────────
    "Email & Messaging": ("Communication", "Email"),
    "Social Media": ("Communication", "Social Media"),
    "Fediverse": ("Communication", "Fediverse"),
    "Alternative Protocols": ("Communication", "Protocols"),
    "RSS": ("Communication", "RSS"),
    "Amateur Radio": ("Communication", "Amateur Radio"),
    "Radio & SDR": ("Communication", "Radio & SDR"),
    "World Radio": ("Communication", "World Radio"),
    "Shortwave Listening": ("Communication", "Shortwave"),

    # ── Internet Tools ──────────────────────────────
    "Search": ("Tools", "Search Engines"),
    "Tools": ("Tools", "General"),
    "Useful Tools": ("Tools", "General"),
    "Niche Tools": ("Tools", "Niche"),
    "Productivity": ("Tools", "Productivity"),
    "Office": ("Tools", "Productivity"),
    "Read Later": ("Tools", "Read Later"),
    "Mind Mapping": ("Tools", "Mind Mapping"),
    "Alt Frontends": ("Tools", "Alt Frontends"),
    "Directories": ("Tools", "Directories"),
    "Maps & Geography": ("Tools", "Maps"),
    "Time": ("Tools", "Time & Dates"),
    "Paste & Files": ("Tools", "File Sharing"),
    "News": ("Tools", "News"),
    "Tech News": ("Tools", "Tech News"),
    "Legal": ("Tools", "Legal"),
    "Curated Lists": ("Tools", "Curated Lists"),
    "Hidden Gems": ("Tools", "Hidden Gems"),
    "Miscellaneous": ("Tools", "Miscellaneous"),

    # ── Self-Hosting & Homelab ──────────────────────
    "Self-Hosting": ("Self-Hosting", "General"),
    "Homelab": ("Self-Hosting", "Homelab"),
    "Self-Hosting Apps": ("Self-Hosting", "Apps"),
    "Media Servers": ("Self-Hosting", "Media"),
    "File Sync": ("Self-Hosting", "File Sync"),

    # ── Crypto & Finance ────────────────────────────
    "Crypto": ("Finance", "Cryptocurrency"),
    "Finance": ("Finance", "General"),

    # ── Knowledge ───────────────────────────────────
    "Knowledge": ("Knowledge", "General"),
    "Knowledge & Learning": ("Knowledge", "Learning"),
    "Learning": ("Knowledge", "Learning"),
    "Wikis": ("Knowledge", "Wikis"),
    "Fandom Wikis": ("Knowledge", "Fandom"),

    # ── Forums & Communities ────────────────────────
    "Forums & Communities": ("Communities", "General"),
    "General Forums & Communities": ("Communities", "General"),
    "Tech Forums & Communities": ("Communities", "Tech"),
    "Linux & Unix Communities": ("Communities", "Linux"),
    "Forums": ("Communities", "General"),
    "Imageboards & Chans": ("Communities", "Imageboards"),

    # ── Catch-all unmapped ──────────────────────────
    "Blogging": ("Tools", "Blogging"),
    "Coin Collecting": ("Hobbies", "Collecting"),
    "Mechanical Keyboards": ("Crafts", "Keyboards"),
    "Niche Hobbies": ("Hobbies", "Niche"),
    "Science Videos": ("Science", "Videos"),
    "Software & Apps": ("Tools", "Software"),
    "Tiny Web": ("Internet Culture", "Tiny Web"),
    "Travel & Adventure": ("Lifestyle", "Travel"),
    "Security Forums": ("Security", "Forums"),
}

NICHE_CATEGORY_MAP = {
    "Underground Comics & Zines": ("Internet Culture", "Underground Comics"),
    "Typewriter Culture": ("Retro", "Typewriters"),
    "Punk & Hardcore Music": ("Music", "Punk & Hardcore"),
    "Weird Fiction & Liminal Spaces": ("Internet Culture", "Weird Fiction"),
    "Cottagecore & Homesteading": ("Lifestyle", "Homesteading"),
    "Tiny House Movement": ("Lifestyle", "Tiny House"),
    "Traditional Crafts": ("Crafts", "Traditional"),
    "Niche Podcasts": ("Entertainment", "Podcasts"),
    "Digital Nomad Tools": ("Lifestyle", "Digital Nomad"),
    "Esoteric & Occult": ("Internet Culture", "Esoteric"),
    "Abandoned Places": ("Internet Culture", "Abandoned Places"),
    "Micronations": ("Lifestyle", "Micronations"),
    "Lost Programming Languages": ("Retro", "Dead Languages"),
    "Alternative Medicine & Wellness": ("Lifestyle", "Alternative Medicine"),
    "Furniture Building": ("Crafts", "Furniture"),
    "Lost TV & Radio Shows": ("Retro", "Lost Media"),
    "Independent Radio": ("Communication", "Independent Radio"),
    "Alternative Education": ("Lifestyle", "Education"),
    "Niche Fitness": ("Hobbies", "Fitness"),
    "Vintage Fashion": ("Retro", "Fashion"),
    "Obsolete Professions": ("Retro", "Obsolete Professions"),
    "Fringe Science": ("Science", "Fringe"),
    "Alternative Currencies": ("Lifestyle", "Alternative Currencies"),
    "Lost Inventions": ("Retro", "Lost Inventions"),
    "Esoteric Sports": ("Hobbies", "Esoteric Sports"),
    "Obscure Holidays": ("Lifestyle", "Obscure Holidays"),
    "Historical Reenactment": ("Lifestyle", "Reenactment"),
    "Useless Websites": ("Internet Culture", "Weird Web"),
    "Art Movements": ("Creative", "Art Movements"),
    "Street Art": ("Creative", "Street Art"),
    "Experimental Music": ("Music", "Experimental"),
    "Lost Arcade Games": ("Gaming", "Retro"),
}


def main():
    with open(LINKS_FILE, 'r', encoding='utf-8') as f:
        links = json.load(f)
    print(f"Loaded {len(links)} links from links.json")

    with open(NICHE_FILE, 'r', encoding='utf-8') as f:
        niche_links = json.load(f)
    print(f"Loaded {len(niche_links)} links from niche_websites.json")

    # Fix misplaced links
    for link in links:
        name_lower = link['name'].lower()
        if link['category'] == 'Privacy & Security':
            if any(w in name_lower for w in ['bacon ipsum', 'blob maker', 'lorem ipsum', 'circuitlab', 'alternativeto']):
                link['category'] = 'Creative'
                link['_subcategory'] = 'Tools'
                print(f"  Fixed misplaced: {link['name']} → Creative/Tools")

    # Merge niche links
    existing_urls = {l['url'] for l in links}
    added_niche = 0
    for link in niche_links:
        if link['url'] not in existing_urls:
            links.append(link)
            existing_urls.add(link['url'])
            added_niche += 1
    print(f"Added {added_niche} niche links")

    # Migrate categories
    unmapped = set()
    migrated = 0
    for link in links:
        old_cat = link['category']

        # Check if already migrated
        if '_' in old_cat and link.get('subcategory'):
            continue

        # Try main map first, then niche map
        mapping = CATEGORY_MAP.get(old_cat) or NICHE_CATEGORY_MAP.get(old_cat)
        if mapping:
            link['category'] = mapping[0]
            link['subcategory'] = mapping[1]
            migrated += 1
        else:
            unmapped.add(old_cat)
            link['subcategory'] = old_cat

    if unmapped:
        print(f"\nUnmapped categories ({len(unmapped)}):")
        for cat in sorted(unmapped):
            print(f"  - {cat}")

    print(f"Migrated {migrated} links to new categories")

    # Sort by category then name
    links.sort(key=lambda x: (x['category'], x.get('subcategory', ''), x['name']))

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(links, f, ensure_ascii=False, indent=2)
    print(f"\nSaved {len(links)} links to {OUTPUT_FILE}")

    # Print summary
    cats = {}
    for l in links:
        key = l['category']
        if key not in cats:
            cats[key] = {}
        sub = l.get('subcategory', 'General')
        cats[key][sub] = cats[key].get(sub, 0) + 1

    print(f"\n=== New Categories ({len(cats)} main) ===")
    for cat in sorted(cats.keys()):
        total = sum(cats[cat].values())
        print(f"\n  {cat} ({total})")
        for sub, count in sorted(cats[cat].items()):
            print(f"    {sub}: {count}")


if __name__ == '__main__':
    main()
