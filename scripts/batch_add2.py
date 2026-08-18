#!/usr/bin/env python3
"""Batch add more links - focusing on thin categories"""
import json

LINKS_FILE = 'links.json'
JS_FILE = 'links.js'

with open(LINKS_FILE) as f:
    links = json.load(f)

existing_urls = {l['url'] for l in links}
new_links_list = []
added = 0

def add(name, url, desc, category):
    global added
    if url in existing_urls:
        return
    new_links_list.append({"name": name, "url": url, "desc": desc, "category": category})
    existing_urls.add(url)
    added += 1

# MEME & INTERNET CULTURE
add("Know Your Meme", "https://knowyourmeme.com/", "Internet meme encyclopedia", "Meme & Internet Culture")
add("Urban Dictionary", "https://www.urbandictionary.com/", "Internet slang definitions", "Meme & Internet Culture")
add("Imgur", "https://imgur.com/", "Image hosting and viral memes", "Meme & Internet Culture")
add("GIPHY", "https://giphy.com/", "Animated GIF search engine", "Meme & Internet Culture")
add("Niconico", "https://www.nicovideo.jp/", "Japanese video sharing culture", "Meme & Internet Culture")
add("TikTok", "https://www.tiktok.com/", "Short form video trends", "Meme & Internet Culture")
add("Tumblr", "https://www.tumblr.com/", "Blogging and fandom culture", "Meme & Internet Culture")

# CREEPY & HORROR
add("Creepypasta.com", "https://www.creepypasta.com/", "Horror stories archive", "Creepy & Horror")
add("r/nosleep", "https://www.reddit.com/r/nosleep/", "Horror stories community", "Creepy & Horror")
add("r/creepy", "https://www.reddit.com/r/creepy/", "Creepy images and media", "Creepy & Horror")
add("Lets Not Meet", "https://www.reddit.com/r/LetsNotMeet/", "Real life creepy encounters", "Creepy & Horror")
add("Unresolved Mysteries", "https://www.reddit.com/r/UnresolvedMysteries/", "Unsolved true crime", "Creepy & Horror")
add("Cryptid Wiki", "https://cryptidz.fandom.com/", "Cryptozoology creatures database", "Creepy & Horror")
add("Morbid Anatomy", "https://morbidanatomy.blogspot.com/", "Museum of morbid curiosities", "Creepy & Horror")
add("Ghost Stories", "https://www.reddit.com/r/Ghoststories/", "Real ghost encounter tales", "Creepy & Horror")
add("Humanoid Encounters", "https://www.reddit.com/r/Humanoidencounters/", "Strange creature encounters", "Creepy & Horror")

# EARTH OBSERVATION
add("Google Earth", "https://earth.google.com/", "Interactive global satellite imagery", "Earth Observation")
add("NASA Earth Observatory", "https://earthobservatory.nasa.gov/", "NASA satellite earth imagery", "Earth Observation")
add("Sentinel Hub", "https://www.sentinel-hub.com/", "ESA satellite data browser", "Earth Observation")
add("USGS Earth Explorer", "https://earthexplorer.usgs.gov/", "USGS satellite data", "Earth Observation")
add("Zoom Earth", "https://zoom.earth/", "Real-time satellite weather imagery", "Earth Observation")
add("NASA Worldview", "https://worldview.earthdata.nasa.gov/", "Interactive satellite viewer", "Earth Observation")
add("Land Viewer", "https://eos.com/landviewer/", "Satellite imagery analysis tool", "Earth Observation")
add("Mapbox", "https://www.mapbox.com/", "Custom mapping satellite data", "Earth Observation")
add("Soar Earth", "https://soar.earth/", "High resolution satellite imagery", "Earth Observation")

# BOARD GAME APPS
add("BoardGameArena", "https://boardgamearena.com/", "Online board game platform", "Board Game Apps")
add("Tabletopia", "https://tabletopia.com/", "Virtual board game simulator", "Board Game Apps")
add("Yucata", "https://www.yucata.de/", "Turn-based board game platform", "Board Game Apps")
add("Happy Meeple", "https://www.happymeeple.com/", "Board game community platform", "Board Game Apps")
add("Little Golem", "https://littlegolem.net/", "Abstract strategy games", "Board Game Apps")
add("Spiel By Web", "https://www.spielbyweb.com/", "PbeM board game platform", "Board Game Apps")
add("BoardSpace", "https://www.boardspace.net/", "Abstract board game server", "Board Game Apps")
add("ItsYourTurn", "https://www.itsyourturn.com/", "Turn-based board game site", "Board Game Apps")

# KAYAKING
add("American Whitewater", "https://www.americanwhitewater.org/", "Whitewater kayaking resources", "Kayaking")
add("Paddling.com", "https://paddling.com/", "Kayaking community and gear", "Kayaking")
add("Sea Kayaker Magazine", "https://www.seakayakermag.com/", "Sea kayaking techniques", "Kayaking")
add("British Canoeing", "https://www.britishcanoeing.org.uk/", "UK canoeing governing body", "Kayaking")
add("UK Rivers Guide", "https://www.ukriversguidebook.co.uk/", "UK river guide for paddlers", "Kayaking")
add("Canoe Kayak Canada", "https://canoekayak.ca/", "Canadian paddling organization", "Kayaking")
add("Kayak Session", "https://kayaksession.com/", "Whitewater kayak videos", "Kayaking")
add("Atlantic Kayak Tours", "https://atlantickayaktours.com/", "Sea kayaking resources", "Kayaking")
add("Paddle Australia", "https://paddleaustralia.org.au/", "Australian paddling association", "Kayaking")

# SKATEBOARDING
add("Thrasher Magazine", "https://www.thrashermagazine.com/", "Legendary skateboard magazine", "Skateboarding")
add("Transworld Skateboarding", "https://skateboarding.transworld.net/", "Skate media and videos", "Skateboarding")
add("Jenkem Magazine", "https://www.jenkemmag.com/", "Skateboarding culture magazine", "Skateboarding")
add("Skateboard Magazine", "https://skateboardmag.com/", "Skateboarding news culture", "Skateboarding")
add("Skateboarding.com", "https://www.skateboarding.com/", "Skate tips gear reviews", "Skateboarding")
add("Sidewalk Magazine", "https://sidewalkmag.com/", "UK skateboarding magazine", "Skateboarding")
add("Concrete Disciples", "https://concretedisciples.com/", "Skateboarding history", "Skateboarding")
add("The Skateboard Mag", "https://theskateboardmag.com/", "Skateboarding photo journal", "Skateboarding")
add("Skatehere", "https://www.skatehere.com/", "Skateboarding video archive", "Skateboarding")

# URBAN FARMING
add("Urban Farm", "https://urbanfarm.org/", "Urban farming resources", "Urban Farming")
add("City Farmer", "https://cityfarmer.org/", "Urban agriculture information", "Urban Farming")
add("Green Roofs", "https://www.greenroofs.com/", "Green roofing and urban ag", "Urban Farming")
add("Square Foot Gardening", "https://squarefootgardening.org/", "Intensive gardening method", "Urban Farming")
add("Tower Garden", "https://www.towergarden.com/", "Vertical aeroponic gardening", "Urban Farming")
add("Growing Power", "https://www.growingpower.org/", "Urban agriculture nonprofit", "Urban Farming")
add("Urban Vine", "https://urbanvine.co/", "Urban growing supplies", "Urban Farming")
add("AgriTurf", "https://agriturf.com/", "Urban gardening systems", "Urban Farming")

# MUSIC PRODUCTION
add("Vocaloid", "https://www.vocaloid.com/", "Yamaha voice synthesis software", "Music Production")
add("Valhalla DSP", "https://valhalladsp.com/", "High quality audio plugins", "Music Production")
add("iZotope", "https://www.izotope.com/", "Audio production AI tools", "Music Production")
add("Plugin Boutique", "https://www.pluginboutique.com/", "VST plugin marketplace", "Music Production")
add("Sonic Academy", "https://www.sonicacademy.com/", "Music production courses", "Music Production")
add("Attack Magazine", "https://www.attackmagazine.com/", "Electronic music production", "Music Production")
add("Vital Audio", "https://vital.audio/", "Free wavetable synthesizer", "Music Production")
add("Native Instruments", "https://www.native-instruments.com/", "Music production hardware", "Music Production")

# RETRO COMMUNITIES
add("Vintage Computer Federation", "https://vcfed.org/", "Vintage computer community", "Retro Communities")
add("Amiga.org", "https://www.amiga.org/", "Amiga computer community", "Retro Communities")
add("Atari Age", "https://atariage.com/", "Atari enthusiast community", "Retro Communities")
add("Apple II Enthusiasts", "https://apple2.org.za/", "Apple II community portal", "Retro Communities")
add("RetroComputing Reddit", "https://www.reddit.com/r/retrocomputing/", "Retro computing community", "Retro Communities")
add("Apple Fritter", "https://www.applefritter.com/", "Apple I and II community", "Retro Communities")
add("Forum64", "https://www.forum64.de/", "German Commodore community", "Retro Communities")
add("Commodore Scene", "https://commodore.software/", "Commodore software archive", "Retro Communities")

# MATH PUZZLES
add("Project Euler", "https://projecteuler.net/", "Mathematical programming challenges", "Math Puzzles")
add("Brilliant", "https://brilliant.org/", "Math and logic puzzles", "Math Puzzles")
add("Puzzle Prime", "https://puzzleprime.com/", "Math puzzle collection", "Math Puzzles")
add("Brainzilla", "https://www.brainzilla.com/", "Logic math brain teasers", "Math Puzzles")
add("Math is Fun", "https://www.mathsisfun.com/puzzles/", "Fun math puzzle collection", "Math Puzzles")
add("Puzzle Museum", "https://puzzlemuseum.com/", "Interactive math puzzles", "Math Puzzles")
add("John Conway Puzzles", "https://www.johnconway.com/", "Conway puzzle collection", "Math Puzzles")

# GEOGRAPHY
add("Seterra", "https://www.seterra.com/", "Geography quiz games", "Geography")
add("GeoGuessr", "https://www.geoguessr.com/", "Geographic guessing game", "Geography")
add("World Atlas", "https://www.worldatlas.com/", "World geography reference", "Geography")
add("CIA World Factbook", "https://www.cia.gov/the-world-factbook/", "Country intelligence data", "Geography")
add("Nations Online", "https://www.nationsonline.org/", "Country information portal", "Geography")
add("City Population", "https://www.citypopulation.de/", "World city population data", "Geography")
add("Geonames", "https://www.geonames.org/", "World geographical database", "Geography")
add("OpenStreetMap", "https://www.openstreetmap.org/", "Free collaborative world map", "Geography")

# WORD GAMES
add("Wordle", "https://www.nytimes.com/games/wordle/", "Daily word puzzle game", "Word Games")
add("Sporcle Word Games", "https://www.sporcle.com/games/words/", "Word puzzle collection", "Word Games")
add("WordHippo", "https://www.wordhippo.com/", "Word finder thesaurus", "Word Games")
add("FreeRice", "https://freerice.com/", "Vocabulary game charity", "Word Games")
add("Lexulous", "https://www.lexulous.com/", "Online word game community", "Word Games")
add("Scrabble Go", "https://www.scrabblego.com/", "Official Scrabble mobile", "Word Games")
add("7 Little Words", "https://www.7littlewords.com/", "Daily word puzzle", "Word Games")
add("Letterpress", "https://letterpress.xyz/", "Word game", "Word Games")

# TRIVIA
add("Sporcle", "https://www.sporcle.com/", "Trivia quiz collection", "Trivia")
add("JetPunk", "https://www.jetpunk.com/", "Online quiz platform", "Trivia")
add("FunTrivia", "https://www.funtrivia.com/", "Trivia question database", "Trivia")
add("Mental Floss", "https://www.mentalfloss.com/", "Interesting facts quiz", "Trivia")
add("Triviaplenty", "https://www.triviaplenty.com/", "Trivia questions hub", "Trivia")
add("Pub Trivia Questions", "https://www.pubtriviaquestions.com/", "Pub quiz resources", "Trivia")
add("Quizify", "https://quizify.net/", "Trivia quiz generator", "Trivia")
add("Trivia.net", "https://trivia.net/", "Daily trivia questions", "Trivia")

# ESCAPE ROOMS
add("Escape Room Wiki", "https://www.escaperoomwiki.com/", "Escape room database", "Escape Rooms")
add("Room Escape Artist", "https://roomescapeartist.com/", "Escape room reviews news", "Escape Rooms")
add("Escape Room Tips", "https://www.escaperoomtips.com/", "Escape room guides advice", "Escape Rooms")
add("Lock Paper Scissors", "https://lockpaperscissors.com/", "Online escape room directory", "Escape Rooms")
add("Escape Room Era", "https://escaperoomera.com/", "Escape room design blog", "Escape Rooms")
add("Escape Room Addict", "https://escaperoomaddict.com/", "Escape room reviews", "Escape Rooms")
add("Mysterious Package", "https://mysteriouspackage.com/", "Immersive mystery mail", "Escape Rooms")

# JIGSAW PUZZLES
add("Jigsaw Planet", "https://www.jigsawplanet.com/", "Free online jigsaw puzzles", "Jigsaw Puzzles")
add("Jigidi", "https://www.jigidi.com/", "Jigsaw puzzle community", "Jigsaw Puzzles")
add("ePuzzle", "https://www.epuzzle.info/", "Free photo jigsaw puzzles", "Jigsaw Puzzles")
add("TheJigsawPuzzles", "https://www.thejigsawpuzzles.com/", "Free jigsaw puzzle play", "Jigsaw Puzzles")
add("JigZone", "https://www.jigzone.com/", "Online jigsaw game site", "Jigsaw Puzzles")
add("Puzzle Factory", "https://puzzlefactory.com/", "Jigsaw puzzle community", "Jigsaw Puzzles")

# GO GAME
add("OGS", "https://online-go.com/", "Online Go community server", "Go Game")
add("GoQuest", "https://goquest.org/", "Quick Go games platform", "Go Game")
add("Sensei's Library", "https://senseis.xmp.net/", "Go strategy wiki", "Go Game")
add("KGS Go Server", "https://www.gokgs.com/", "Kaya Go server classic", "Go Game")
add("American Go Association", "https://www.usgo.org/", "American Go Association", "Go Game")
add("Go4Go", "https://www.go4go.net/", "Go game database and pro games", "Go Game")
add("Sabaki", "https://sabaki.yjgx.io/", "Go board GUI software", "Go Game")
add("Leela Zero", "https://github.com/leela-zero/leela-zero", "Open-source Go AI", "Go Game")

# 3D & MAKING
add("Thingiverse", "https://www.thingiverse.com/", "3D printable model database", "3D & Making")
add("MyMiniFactory", "https://www.myminifactory.com/", "Curated 3D print models", "3D & Making")
add("Printables", "https://www.printables.com/", "Prusa 3D model community", "3D & Making")
add("Cults 3D", "https://cults3d.com/", "3D model marketplace", "3D & Making")
add("Instructables", "https://www.instructables.com/", "DIY project tutorials", "3D & Making")
add("Make: Magazine", "https://makezine.com/", "Maker community magazine", "3D & Making")
add("Prusa Blog", "https://blog.prusa3d.com/", "3D printing news and guides", "3D & Making")
add("Hubs", "https://www.hubs.com/", "On-demand 3D printing service", "3D & Making")

# HACKER CULTURE
add("Hacker News", "https://news.ycombinator.com/", "Tech news hacker community", "Hacker Culture")
add("Lobsters", "https://lobste.rs/", "Tech link aggregation community", "Hacker Culture")
add("Hacker One", "https://www.hackerone.com/", "Bug bounty platform", "Hacker Culture")
add("DEF CON", "https://defcon.org/", "Hacking conference information", "Hacker Culture")
add("CCC", "https://ccc.de/", "Chaos Computer Club", "Hacker Culture")
add("2600 Magazine", "https://www.2600.com/", "Hacker quarterly magazine", "Hacker Culture")
add("Phrack", "http://phrack.org/", "Hacker zine archive", "Hacker Culture")
add("CTFtime", "https://ctftime.org/", "CTF competition calendar", "Hacker Culture")
add("HackTheBox", "https://www.hackthebox.com/", "Penetration testing platform", "Hacker Culture")

# DEAD MEDIA & OBSOLETE TECH
add("Dead Media Archive", "https://www.deadmedia.org/", "Obsolete media formats", "Dead Media & Obsolete Tech")
add("Format War", "https://formatwar.com/", "Media format history", "Dead Media & Obsolete Tech")
add("Obsolete Technology", "https://obsoletetechnology.net/", "Vintage tech museum", "Dead Media & Obsolete Tech")
add("Vintage Computing", "https://www.vintage-computer.com/", "Classic computer museum", "Dead Media & Obsolete Tech")
add("The Obsolete Skill", "https://theobsoleteskill.com/", "Lost skills documentation", "Dead Media & Obsolete Tech")
add("Floppy Disk Museum", "https://floppydisk.com/", "Floppy disk history", "Dead Media & Obsolete Tech")
add("Total Rewind", "https://www.totalrewind.org/", "Vintage media preservation", "Dead Media & Obsolete Tech")

# BLOGGING
add("WordPress", "https://wordpress.org/", "Open-source blogging platform", "Blogging")
add("Ghost", "https://ghost.org/", "Professional publishing platform", "Blogging")
add("Medium", "https://medium.com/", "Online writing platform", "Blogging")
add("Substack", "https://substack.com/", "Newsletter publishing platform", "Blogging")
add("Write.as", "https://write.as/", "Minimalist writing platform", "Blogging")
add("Bear Blog", "https://bearblog.dev/", "Minimal privacy-focused blog", "Blogging")
add("Mataroa", "https://mataroa.blog/", "Naked blogging platform", "Blogging")

# OFFICE
add("LibreOffice", "https://www.libreoffice.org/", "Free office suite", "Office")
add("OnlyOffice", "https://www.onlyoffice.com/", "Open-source office suite", "Office")
add("Apache OpenOffice", "https://www.openoffice.org/", "Open-source office software", "Office")
add("Zoho Workplace", "https://www.zoho.com/workplace/", "Online office suite", "Office")
add("CryptPad", "https://cryptpad.fr/", "Encrypted office collaboration", "Office")
add("Etherpad", "https://etherpad.org/", "Collaborative document editor", "Office")
add("Cal.com", "https://cal.com/", "Open-source scheduling tool", "Office")
add("Notion", "https://www.notion.com/", "All-in-one workspace", "Office")

# LOST TV & RADIO
add("Archive.org TV News", "https://archive.org/details/tv", "TV news archive collection", "Lost TV & Radio")
add("The Museum of TV", "https://www.museum.tv/", "Television history archive", "Lost TV & Radio")
add("TV Ark", "https://www.tv-ark.org.uk/", "UK television preservation", "Lost TV & Radio")
add("BBC Genome", "https://genome.ch.bbc.co.uk/", "BBC radio listings archive", "Lost TV & Radio")
add("Radio Echoes", "https://radioechoes.com/", "Historic radio recordings", "Lost TV & Radio")
add("Old Time Radio", "https://www.oldtimeradio.com/", "Vintage radio show collection", "Lost TV & Radio")
add("Radio Garden", "https://radio.garden/", "Explore live radio worldwide", "Lost TV & Radio")
add("The Radio Archive", "https://www.theradioarchive.com/", "Old time radio shows", "Lost TV & Radio")
add("TV History", "https://www.tvhistory.tv/", "Television history resources", "Lost TV & Radio")

# INDEPENDENT RADIO
add("SomaFM", "https://somafm.com/", "Listener-supported streaming", "Independent Radio")
add("KFJC", "https://www.kfjc.org/", "Experimental community radio", "Independent Radio")
add("WFMU", "https://wfmu.org/", "Freeform independent radio", "Independent Radio")
add("KEXP", "https://www.kexp.org/", "Independent music radio Seattle", "Independent Radio")
add("KBOO", "https://kboo.fm/", "Portland community radio", "Independent Radio")
add("Radiooooo", "https://radiooooo.com/", "Music radio by decade country", "Independent Radio")
add("Internet Radio", "https://www.internet-radio.com/", "Streaming radio directory", "Independent Radio")
add("Streema", "https://streema.com/", "Worldwide radio directory", "Independent Radio")

# NICHE TOOLS
add("IFTTT", "https://ifttt.com/", "Automation between services", "Niche Tools")
add("Zapier", "https://zapier.com/", "Workflow automation platform", "Niche Tools")
add("n8n", "https://n8n.io/", "Open-source workflow automation", "Niche Tools")
add("Make (Integromat)", "https://www.make.com/", "Visual automation platform", "Niche Tools")
add("Pipedream", "https://pipedream.com/", "Developer workflow platform", "Niche Tools")
add("Datadog", "https://www.datadoghq.com/", "Cloud monitoring platform", "Niche Tools")
add("Sentry", "https://sentry.io/", "Error tracking software", "Niche Tools")
add("OneSignal", "https://onesignal.com/", "Push notification service", "Niche Tools")

# WORLD RADIO
add("BBC World Service", "https://www.bbc.co.uk/worldserviceradio", "International BBC radio", "World Radio")
add("Radio France Internationale", "https://www.rfi.fr/", "French international radio", "World Radio")
add("Deutsche Welle", "https://www.dw.com/", "German international broadcasting", "World Radio")
add("Radio Canada International", "https://www.rcinet.ca/", "Canadian international radio", "World Radio")
add("Voice of America", "https://www.voanews.com/", "US international broadcasting", "World Radio")
add("NHK World", "https://www3.nhk.or.jp/nhkworld/", "Japanese international radio", "World Radio")
add("Shortwave Schedule", "https://shortwaveschedule.com/", "Worldwide shortwave schedules", "World Radio")
add("Radio Netherlands", "https://www.rnw.org/", "Dutch international service", "World Radio")

# 3D PRINTING
add("Prusa3D", "https://www.prusa3d.com/", "Popular 3D printer manufacturer", "3D Printing")
add("Ultimaker", "https://ultimaker.com/", "Professional 3D printing", "3D Printing")
add("Simplify3D", "https://www.simplify3d.com/", "Advanced 3D slicer software", "3D Printing")
add("Cura", "https://ultimaker.com/software/ultimaker-cura", "Open-source 3D slicer", "3D Printing")
add("OctoPrint", "https://octoprint.org/", "3D printer remote control", "3D Printing")
add("Marlin Firmware", "https://marlinfw.org/", "Open-source printer firmware", "3D Printing")
add("RepRap", "https://reprap.org/", "Self-replicating 3D printer wiki", "3D Printing")
add("All3DP", "https://all3dp.com/", "3D printing news and guides", "3D Printing")
add("3DPrinting Industry", "https://3dprintingindustry.com/", "3D printing industry news", "3D Printing")
add("3D Natives", "https://www.3dnatives.com/", "3D printing magazine", "3D Printing")

# DIGITAL HOARDING
add("DataHoarder Reddit", "https://www.reddit.com/r/DataHoarder/", "Data preservation community", "Digital Hoarding")
add("ArchiveTeam", "https://wiki.archiveteam.org/", "Digital preservation group", "Digital Hoarding")
add("M-DISC", "https://www.mdisc.com/", "Long term archival storage", "Digital Hoarding")
add("BorgBackup", "https://www.borgbackup.org/", "Deduplicating backup tool", "Digital Hoarding")
add("Syncthing", "https://syncthing.net/", "Decentralized file sync", "Digital Hoarding")
add("r/DataCurator", "https://www.reddit.com/r/DataCurator/", "Data curation community", "Digital Hoarding")
add("ArchiveBox", "https://archivebox.io/", "Self-hosted web archiver", "Digital Hoarding")
add("Awesome DataHoarding", "https://github.com/simon987/awesome-datahoarding", "Data hoarding tools list", "Digital Hoarding")

# DIAL-UP & BBS CULTURE
add("Telnet BBS Guide", "https://www.telnetbbsguide.com/", "Active telnet BBS list", "Dial-up & BBS Culture")
add("BBS Corner", "https://www.bbscorner.com/", "BBS software and resources", "Dial-up & BBS Culture")
add("16 Colors", "https://16colo.rs/", "ANSI art BBS archives", "Dial-up & BBS Culture")
add("ACiD", "https://www.acid.org/", "ANSI art group", "Dial-up & BBS Culture")
add("Synchronet", "https://www.synchro.net/", "Open-source BBS software", "Dial-up & BBS Culture")
add("Mystic BBS", "https://www.mysticbbs.com/", "Popular BBS door software", "Dial-up & BBS Culture")
add("The Well", "https://www.well.com/", "Historic online community BBS", "Dial-up & BBS Culture")
add("ANSI Art", "https://artpacks.org/", "ANSI art pack repository", "Dial-up & BBS Culture")
add("Dark Domain", "https://www.darkdomain.org/", "BBS art and history", "Dial-up & BBS Culture")
add("BBSCene", "https://bbscene.net/", "BBS scene community", "Dial-up & BBS Culture")
add("BBS Archives", "https://bbsarchive.net/", "Historical BBS preservation", "Dial-up & BBS Culture")

# FANDOM WIKIS
add("Fandom", "https://www.fandom.com/", "Wiki hosting community platform", "Fandom Wikis")
add("Wookieepedia", "https://starwars.fandom.com/", "Star Wars encyclopedia", "Fandom Wikis")
add("Memory Alpha", "https://memory-alpha.fandom.com/", "Star Trek encyclopedia", "Fandom Wikis")
add("Harry Potter Wiki", "https://harrypotter.fandom.com/", "Harry Potter encyclopedia", "Fandom Wikis")
add("Marvel Database", "https://marvel.fandom.com/", "Marvel universe wiki", "Fandom Wikis")
add("DC Database", "https://dc.fandom.com/", "DC universe wiki", "Fandom Wikis")
add("Bulbapedia", "https://bulbapedia.bulbagarden.net/", "Pokemon encyclopedia", "Fandom Wikis")
add("Mario Wiki", "https://www.mariowiki.com/", "Mario franchise encyclopedia", "Fandom Wikis")
add("Zelda Wiki", "https://zelda.fandom.com/", "Legend of Zelda wiki", "Fandom Wikis")
add("Elder Scrolls Wiki", "https://elderscrolls.fandom.com/", "Elder Scrolls wiki", "Fandom Wikis")

# BRAIN TEASERS
add("BrainDen", "https://brainden.com/", "Logic puzzles collection", "Brain Teasers")
add("Aha! Puzzles", "https://ahapuzzles.com/", "Brain teaser puzzles games", "Brain Teasers")
add("BrainBashers", "https://www.brainbashers.com/", "Puzzles brain teasers games", "Brain Teasers")
add("Riddles.com", "https://www.riddles.com/", "Riddle collection database", "Brain Teasers")
add("PuzzlersWorld", "https://puzzlersworld.com/", "Puzzle collection site", "Brain Teasers")
add("Fun With Puzzles", "https://www.funwithpuzzles.com/", "Logic puzzle variety", "Brain Teasers")
add("Lateral Puzzles", "https://lateralpuzzles.com/", "Lateral thinking puzzles", "Brain Teasers")
add("Logic Puzzles", "https://logic.puzzleworld.org/", "Classic logic puzzles", "Brain Teasers")

# NATURE CAMS
add("Explore.org", "https://explore.org/", "Live animal cams network", "Nature Cams")
add("Monterey Bay Aquarium", "https://www.montereybayaquarium.org/animals/live-cams", "Live aquarium cams", "Nature Cams")
add("San Diego Zoo Cams", "https://zoo.sandiegozoo.org/live-cams", "San Diego zoo live cams", "Nature Cams")
add("Panda Cam", "https://nationalzoo.si.edu/webcams/panda-cam", "Smithsonian panda cam", "Nature Cams")
add("African Wildlife Cam", "https://www.africanwildlifecam.com/", "Live African safari cam", "Nature Cams")
add("Cornell Lab Bird Cams", "https://www.allaboutbirds.org/cams/", "Live bird nest cameras", "Nature Cams")
add("Georgia Aquarium", "https://www.georgiaaquarium.org/webcam/", "Georgia aquarium live cams", "Nature Cams")
add("NC Zoo Cams", "https://www.nczoo.org/live-cams", "North Carolina zoo cams", "Nature Cams")
add("Bear Cam", "https://bearcam.net/", "Alaskan brown bear cam", "Nature Cams")

# SPACE CAMS
add("ISS Live", "https://www.nasa.gov/multimedia/nasatv/iss.html", "International Space Station live", "Space Cams")
add("SOHO Solar Observatory", "https://soho.nascom.nasa.gov/", "Solar and heliospheric observatory", "Space Cams")
add("SDO Solar Dynamics", "https://sdo.gsfc.nasa.gov/", "Solar dynamics observatory images", "Space Cams")
add("JunoCam", "https://www.missionjuno.swri.edu/junocam", "Jupiter mission camera images", "Space Cams")
add("Mars Curiosity Rover", "https://mars.nasa.gov/msl/multimedia/raw/", "Curiosity rover raw images", "Space Cams")
add("Mars Perseverance", "https://mars.nasa.gov/mars2020/multimedia/raw/", "Perseverance rover raw images", "Space Cams")
add("JSatTrack", "https://www.n2yo.com/", "Satellite tracking live", "Space Cams")
add("ESA Web TV", "https://www.esa.int/ESA_Multimedia/ESA_Web_TV", "ESA live space events", "Space Cams")

# LANGUAGE & ETYMOLOGY
add("Etymonline", "https://www.etymonline.com/", "Online etymology dictionary", "Language & Etymology")
add("Wiktionary", "https://en.wiktionary.org/", "Free multilingual dictionary", "Language & Etymology")
add("Merriam-Webster", "https://www.merriam-webster.com/", "American dictionary", "Language & Etymology")
add("Oxford Dictionary", "https://www.oed.com/", "Oxford English Dictionary", "Language & Etymology")
add("The Word Detective", "https://www.word-detective.com/", "Word origins column", "Language & Etymology")
add("World Wide Words", "https://www.worldwidewords.org/", "English etymology worldwide", "Language & Etymology")
add("Phrase Finder", "https://www.phrases.org.uk/", "Phrase meanings origins", "Language & Etymology")

# DRONE RACING
add("Drone Racing League", "https://thedroneracingleague.com/", "Professional drone racing", "Drone Racing")
add("MultiGP", "https://www.multigp.com/", "Multi-rotor drone racing league", "Drone Racing")
add("Rotorbuilds", "https://rotorbuilds.com/", "FPV drone builds community", "Drone Racing")
add("FPV Reddit", "https://www.reddit.com/r/fpv/", "FPV drone community", "Drone Racing")
add("BetaFPV", "https://betafpv.com/", "FPV drone manufacturer", "Drone Racing")
add("DJI FPV", "https://www.dji.com/fpv", "DJI FPV drone system", "Drone Racing")
add("Oscar Liang", "https://oscarliang.com/", "FPV drone tutorials guides", "Drone Racing")
add("FPV Knowledge", "https://fpvknowledge.com/", "Drone racing knowledge base", "Drone Racing")
add("Rotor Riot", "https://rotorriot.com/", "FPV drone racing community", "Drone Racing")
add("iFlight", "https://www.iflight.com/", "FPV drone frame maker", "Drone Racing")

# AMATEUR ROCKETRY
add("SpaceX", "https://www.spacex.com/", "Private spaceflight company", "Amateur Rocketry")
add("NASA Rocketry", "https://www.nasa.gov/rocketry/", "NASA rocketry resources", "Amateur Rocketry")
add("Rocketry Forum", "https://www.rocketryforum.com/", "Amateur rocket community", "Amateur Rocketry")
add("Apogee Rockets", "https://www.apogeerockets.com/", "Model rocketry supplies", "Amateur Rocketry")
add("Estes Rockets", "https://estesrockets.com/", "Model rocket manufacturer", "Amateur Rocketry")
add("Tripoli Rocketry", "https://www.tripoli.org/", "High power rocketry organization", "Amateur Rocketry")
add("NAR", "https://www.nar.org/", "National Association of Rocketry", "Amateur Rocketry")
add("BPS Space", "https://www.bps.space/", "Experimental amateur rocketry", "Amateur Rocketry")

# LIMINAL & DREAMS
add("Liminal Archives", "https://liminal-archives.wikidot.com/", "Liminal space fiction and lore", "Liminal & Dreams")
add("Backrooms Wiki", "https://backrooms.fandom.com/", "Backrooms liminal horror fiction", "Liminal & Dreams")
add("Dreamviews", "https://www.dreamviews.com/", "Lucid dreaming community", "Liminal & Dreams")
add("LD4All", "https://ld4all.com/", "Lucid dreaming techniques", "Liminal & Dreams")
add("DreamJournal", "https://dreamjournal.net/", "Online dream journal community", "Liminal & Dreams")
add("World Dream Bank", "https://worlddreambank.org/", "Dream symbolism database", "Liminal & Dreams")
add("The Liminality", "https://the-liminality-gallery.neocities.org/", "Liminal space gallery", "Liminal & Dreams")
add("Subreddit LiminalSpace", "https://www.reddit.com/r/LiminalSpace/", "Liminal space images", "Liminal & Dreams")

# CURIATED LISTS extra
add("Awesome Lists", "https://github.com/sindresorhus/awesome", "Awesome list of awesome lists", "Curated Lists")
add("Awesome Selfhosted", "https://awesome-selfhosted.net/", "Self-hosted software list", "Curated Lists")
add("Awesome Privacy", "https://awesome-privacy.xyz/", "Privacy tools list", "Curated Lists")
add("Track Awesome", "https://www.trackawesomelist.com/", "Track awesome list updates", "Curated Lists")

# ===== SAVE =====
print(f"New links to add: {added}")

links.extend(new_links_list)
with open(LINKS_FILE, 'w', encoding='utf-8') as f:
    json.dump(links, f, ensure_ascii=False, indent=2)
with open(JS_FILE, 'w', encoding='utf-8') as f:
    f.write(f'const linksData = {json.dumps(links, ensure_ascii=False)};\n')
print(f"Saved: {len(links)} total links ({added} new)")
