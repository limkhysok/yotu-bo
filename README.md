yotu-bo/
├── main.py                # App Entry Point (App initialization & Execution)
├── core/                  # Core Application Logic
│   ├── models/            # Data Structures (What we are working with)
│   │   ├── upload_task.py # Video/Status object definitions
│   │   └── settings.py    # Configuration objects
│   ├── services/          # Business Logic (The "Managers")
│   │   ├── uploader.py    # The High-level Upload Orchestrator
│   │   └── browser.py     # Selenium Lifecycle Manager
│   ├── utils/             # Helper Functions (The "Tools")
│   │   ├── vision.py      # PyAutoGUI/OpenCV detection helpers
│   │   └── system.py      # File system/Process (taskkill) helpers
│   └── ui/                # UI Components (The "View")
│       ├── main_window.py # Main Shell (Navbar + Sidebar)
│       ├── project_tab.py # The Automation control panel
│       └── views/         # Smaller reusable widgets
├── assets/                # Static Resources
│   ├── fonts/             # Custom typography
│   ├── icons/             # App & Navbar icons
│   └── screenshots/       # Images for PyAutoGUI detection
├── uploads/               # Input folder for .mp4 files
├── logs/                  # persistent log files
└── requirements.txt