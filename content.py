"""Owner-editable portfolio content. Paths are relative to this standalone app."""

PROFILE = {
    "name": "Renzo Pogoy",
    "role": "3rd Year Computer Science Student",
    "focus": "Aspiring AI Engineer & Full-Stack Developer",
    "program": "Computer Science",
    "institution": "Cebu Institute of Technology – University",
    "location": "Cebu, Philippines",
    "course": "CSIT 349 · Applied AI",
    "year": "3rd Year",
    "section": "F2",
    "github": "",
    "linkedin": "",
    "email": "ensoo1713@gmail.com",
    "portrait": "assets/images/picmine.png",
    "intro": "I am a 3rd Year Computer Science student at Cebu Institute of Technology – University (Section F2) aspiring to become an AI Engineer and Full-Stack Developer, dedicated to building intelligent, ambient, and practical software solutions.",
}

STORY = {
    "Background": "I am Renzo Pogoy, a 3rd Year Computer Science student at Cebu Institute of Technology – University (Section F2) in Cebu, Philippines. I started programming with C and C++, exploring memory, data structures, and algorithms. As I progressed in my studies, I became deeply interested in artificial intelligence, modern web technologies, and engineering practical digital solutions.",
    "Education": "I study Computer Science at Cebu Institute of Technology – University. My foundational coursework in programming, data structures, and algorithms guides how I approach complex software engineering problems, systems programming, and machine learning challenges.",
    "What I Like Building": "I am enthusiastic about building intelligent interfaces, dependable tools, and software that addresses community and real-world needs. I enjoy developing full-stack applications with Python, Next.js, and TypeScript, building native desktop systems with Rust and Tauri, and exploring applied AI integrations.",
    "My Learning Journey": "I began with core programming fundamentals and expanded into collaborative development and competitive hackathons. With Team StarIsda, I contributed to Parola, which achieved Top 5 Finalist at the 2026 DOST AI Fest. That experience fueled my passion for AI engineering, teamwork, and building high-impact technology.",
}

PROJECTS = [
    {
        "id": "padulong",
        "title": "PADULONG",
        "platform": "Web",
        "platform_label": "Web Application · Mobile-Optimized",
        "featured": True,
        "summary": "Verified LTFRB fare engine, multi-modal route planning, and offline driver flashcards for Metro Cebu transit.",
        "description": "Metro Cebu public transit navigator designed for daily commuters, featuring verified jeepney and bus routing, official LTFRB Region VII fare calculations, landmark search, and offline-ready 'Pakita sa Driver' flashcards.",
        "problem": "Public transit routes across Metro Cebu rely heavily on informal local landmarks rather than standardized street addresses, making route selection, fare calculation, and communicating with drivers difficult during crowded commutes.",
        "audience": "Metro Cebu commuters, university students, and visitors navigating local jeepney, modern PUV, and MyBus transit networks.",
        "capabilities": [
            "Verified LTFRB Region VII fare engine (₱14.00 official base fare & student concessions)",
            "120+ active Cebu PUJ and PUV routes (Traditional Jeepneys, Modern BEEPs, MyBus airport shuttles)",
            "Pakita sa Driver Flashcard: High-contrast driver display card with clear Cebuano phrases ('Lugar lang, Boss!')",
            "Multi-modal route mapping connecting major transfer hubs at Colon, IT Park, Ayala, and SM City",
        ],
        "role": "Solo developer, designing the intuitive commute interface and connecting the Next.js frontend to the Python FastAPI routing backend.",
        "tools": ["Next.js", "TypeScript", "FastAPI", "Python", "Gemini API", "Leaflet", "Tailwind CSS"],
        "approach": "Decouple route optimization and natural language queries into a high-performance Python FastAPI service while Next.js presents clean, mobile-first directions and offline driver cards.",
        "status": "In active development",
        "outcome": "Demonstrated working transit navigator prototype with 120+ routes, LTFRB tariff calculations, and offline flashcards.",
        "image": "assets/images/projects/padulong.png",
    },
    {
        "id": "framely",
        "title": "FRAMELY",
        "platform": "Web",
        "platform_label": "Web Creative Studio · In-Browser",
        "featured": True,
        "summary": "Local creative studio turning raw recordings into launch-ready demo clips and store decks.",
        "description": "In-browser creative studio that wraps screen recordings in realistic hardware frames (MacBook Pro, iPhone, Android), choreographs 60 FPS pan-and-zoom motion, and generates panoramic App Store screenshot listings—rendered 100% client-side with zero server uploads, zero watermarks, and zero cost.",
        "problem": "Solo developers and indie creators need professional launch videos and App Store screenshot listings, but traditional video editors are complex, and web services impose watermarks, subscriptions, or require uploading private media to third-party servers.",
        "audience": "Indie developers, software creators, and designers preparing launch demos, social media teasers, and store screenshot listings.",
        "capabilities": [
            "Realistic hardware frame wrapping (MacBook Pro, iPhone 16 Pro, Android)",
            "60 FPS keyframe motion: smooth camera pans, tilts, zooms, and cursor choreography",
            "Panoramic multi-slide App Store screenshot generator",
            "100% private in-browser rendering via Web APIs (MediaRecorder, HTML5 Canvas) and ZIP export",
        ],
        "role": "Frontend developer and UI designer, implementing the interactive canvas editor, GSAP motion timeline, and store screenshot composer.",
        "tools": ["Next.js 15", "React 19", "TypeScript", "Tailwind CSS", "Fabric.js", "GSAP", "JSZip"],
        "approach": "Execute all image composition, timeline scrubbing, and video frame capture entirely in the user's browser, eliminating backend hosting costs while guaranteeing absolute user privacy.",
        "status": "Production-ready local studio",
        "outcome": "High-performance client-side studio capable of generating 1080p 60 FPS product demo videos and App Store listing suites instantly.",
        "image": "assets/images/projects/framely.png",
    },
    {
        "id": "project_notch",
        "title": "PIP (PROJECT_NOTCH)",
        "platform": "Desktop",
        "platform_label": "Windows Desktop Companion · Native Layer",
        "featured": True,
        "summary": "A lightweight, ambient Windows 11 desktop companion layer featuring an interactive canvas mascot (Pip) and quick-access utility drawers.",
        "description": "An ambient desktop operating layer engineered specifically for Windows 11/10 that rests seamlessly along the top-center screen bezel. Built with Tauri 2, Rust, and Svelte 5, it remains quiet and non-intrusive when idle, expanding on hover into an expressive companion with quick utilities, media controls, app launcher, and an interactive mascot.",
        "problem": "Desktop utility apps often clutter the taskbar or consume heavy background resources (Electron bloat), lacking ambient awareness and delightful, lightweight interactions.",
        "audience": "Windows power users, developers, and students wanting a fast, ambient, zero-bloat companion that integrates native system controls with personality.",
        "capabilities": [
            "Ambient screen-bezel notch mode (336×60 px) that expands smoothly into contextual drawers",
            "Interactive procedural robotic companion ('Pip') with real-time 60 FPS gaze tracking and squash-and-stretch physics",
            "System media transport integration (GSMTC) for real-time music playback control",
            "Quick-access utility drawers: Apps Dock, Clipboard History, Focus Timer, Battery, and Downloads monitor",
            "Zero-telemetry, memory-efficient native Rust backend utilizing Win32 Event Hooks",
        ],
        "role": "Full-stack desktop developer, building the native Rust backend integrating Win32 APIs and crafting the Svelte 5 frontend with custom HTML5 Canvas mascot rendering.",
        "tools": ["Tauri 2", "Rust", "Svelte 5", "TypeScript", "Vite", "Win32 APIs", "HTML5 Canvas"],
        "approach": "Leverage Tauri 2 and native Win32 system event hooks in Rust for sub-1% CPU usage during idle, combined with reactive Svelte 5 runes and procedural canvas physics for fluid 60 FPS motion on interaction.",
        "status": "In active development",
        "outcome": "Ultra-lightweight Windows companion layer with ambient UI, responsive system event listeners, and an expressive companion character.",
        "image": "assets/images/projects/project_notch.png",
    },
]

COMPETITIONS = [
    {"title": "DOST Western Visayas 2026 AI Fest Hackathon", "year": "2026", "recognition": "Top 5 Finalist", "details": "With Team StarIsda for PAROLA. This is team recognition."},
    {"title": "Philippine Startup Challenge XI", "year": "2026", "recognition": "Top 25 Regional Qualifier", "details": "Team StarIsda / PAROLA; selected from 243 entries across 23 schools in Central Visayas. Regional event date listed in the portfolio: October 24, 2026, Bai Hotel, Mandaue City."},
    {"title": "Data, AI & Policy APAC Hackathon: Financial Health Frontiers", "year": "2026", "recognition": "Accepted to Phase 2", "details": "Documented acceptance to Phase 2; no later result supplied."},
    {"title": "Knowles Engineering Innovation Hackathon", "year": "2026", "recognition": "Accepted", "details": "Industry and academe event. Acceptance is the documented status; no award supplied."},
]

SKILL_GROUPS = {
    "Programming Languages": {
        "Python": "Applied AI integrations, backend FastAPI web services, and hackathon prototypes",
        "TypeScript": "Full-stack web application development and typed architectures",
        "Rust": "Native system programming, Win32 event hooks, and Tauri 2 backend architecture",
        "C": "Foundations in memory management, data structures, and algorithms",
        "C++": "Object-oriented systems, memory structures, and algorithmic problem solving",
        "Java": "Object-oriented programming, data structures, and software design principles",
    },
    "Web & Backend": {
        "Tailwind CSS": "Modern responsive styling and custom design systems",
        "Next.js": "Server-side rendering, API routing, and full-stack web applications",
        "React": "Component architecture, interactive state management, and modern UI engineering",
        "Svelte 5": "Modern reactive runes ($state, $derived) and high-performance UI components",
        "FastAPI": "High-performance Python backend REST APIs",
    },
    "Desktop & Creative Tools": {
        "Fabric.js": "Interactive HTML5 canvas object manipulation and rendering",
        "GSAP": "Hardware-accelerated timeline motion, keyframe animation, and easing",
        "HTML5 Canvas": "Procedural 60 FPS graphics, physics-based mascot rendering, and gaze tracking",
        "Tauri 2": "Ultra-lightweight, memory-efficient native desktop application runtime",
    },
    "Data & Storage": {
        "Supabase": "Cloud database management, authentication, and backend services",
        "PostgreSQL": "Relational database querying and data persistence",
        "SQLite": "Embedded local relational database storage",
        "AsyncStorage": "Local client state and preferences storage",
    },
    "AI & Native Integrations": {
        "Gemini API": "Generative AI workflows and intelligent prompt engineering",
        "Win32 APIs": "Native Windows hooks (GSMTC media controls, clipboard listener, power telemetry)",
        "Leaflet": "Interactive geospatial maps and route visualization",
        "SMS Gateway": "Plain-text mobile integrations for accessible offline reach",
    },
}

SKILL_RATINGS = {
    "Tailwind CSS": 5,
    "Python": 4,
    "TypeScript": 4,
    "Next.js": 4,
    "React": 4,
    "Svelte 5": 4,
    "Fabric.js": 4,
    "GSAP": 4,
    "HTML5 Canvas": 4,
    "Gemini API": 4,
    "Rust": 3,
    "FastAPI": 3,
    "Tauri 2": 3,
    "C": 3,
    "C++": 3,
    "Java": 3,
    "Supabase": 3,
    "PostgreSQL": 3,
    "SQLite": 3,
    "AsyncStorage": 3,
    "Win32 APIs": 3,
    "Leaflet": 3,
    "SMS Gateway": 3,
}

SKILLS_DATA = [
    {
        "Skill": skill,
        "Category": category,
        "Self-Assessment (1-5)": SKILL_RATINGS.get(skill, 3),
        "Practical Application & Context": evidence,
    }
    for category, technologies in SKILL_GROUPS.items()
    for skill, evidence in technologies.items()
]

# Backward-compatibility alias
SKILL_PROFICIENCY = SKILLS_DATA

# Aesthetic Core Competencies & Tools Data (Unrated)
COMPETENCIES_CATALOG = [
    {
        "Domain": category,
        "Tool / Technology": skill,
        "Practical Application & Project Scope": evidence,
    }
    for category, technologies in SKILL_GROUPS.items()
    for skill, evidence in technologies.items()
]

DOMAIN_SUMMARIES = [
    {
        "Domain": "Programming Languages",
        "Tools & Frameworks": list(SKILL_GROUPS["Programming Languages"].keys()),
        "Tool Count": len(SKILL_GROUPS["Programming Languages"]),
        "Practical Scope & Engineering Focus": "Applied AI integrations, typed web architectures, native Win32/Tauri systems, low-level memory & algorithmic foundations.",
    },
    {
        "Domain": "Web & Backend",
        "Tools & Frameworks": list(SKILL_GROUPS["Web & Backend"].keys()),
        "Tool Count": len(SKILL_GROUPS["Web & Backend"]),
        "Practical Scope & Engineering Focus": "Modern reactive UI design systems, full-stack SSR web applications, and high-performance Python REST APIs.",
    },
    {
        "Domain": "Desktop & Creative Tools",
        "Tools & Frameworks": list(SKILL_GROUPS["Desktop & Creative Tools"].keys()),
        "Tool Count": len(SKILL_GROUPS["Desktop & Creative Tools"]),
        "Practical Scope & Engineering Focus": "Procedural 60 FPS graphics, canvas physics, hardware-accelerated timeline animations, and native desktop runtime.",
    },
    {
        "Domain": "Data & Storage",
        "Tools & Frameworks": list(SKILL_GROUPS["Data & Storage"].keys()),
        "Tool Count": len(SKILL_GROUPS["Data & Storage"]),
        "Practical Scope & Engineering Focus": "Cloud database management, authentication, relational schema queries, and embedded local storage.",
    },
    {
        "Domain": "AI & Native Integrations",
        "Tools & Frameworks": list(SKILL_GROUPS["AI & Native Integrations"].keys()),
        "Tool Count": len(SKILL_GROUPS["AI & Native Integrations"]),
        "Practical Scope & Engineering Focus": "Generative AI workflows, native Windows system hooks, geospatial route planning, and offline mobile SMS.",
    },
]

