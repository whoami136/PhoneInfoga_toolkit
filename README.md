# PhoneInfoga_toolkit
An advanced, modular OSINT investigation toolkit designed for terminal-based reconnaissance. Featuring a high-performance multi-threaded engine, ALIEN-INTEL provides unified, real-time analysis for target nodes with a clean, professional aesthetic.
# ALIEN-INTEL V.OMEGA

A modular, high-performance OSINT investigation toolkit designed for terminal-based reconnaissance. ALIEN-INTEL provides unified, multi-threaded analysis for target nodes with a clean, minimalist, white/grey interface.

![Version](https://img.shields.io/badge/Version-V.OMEGA-white)
![Build](https://img.shields.io/badge/Status-Operational-green)

---

## 🛠 Features
*   **Modular Architecture:** Easily extend capabilities by adding new modules in the `modules/` directory.
*   **Multi-Threaded Engine:** Parallel execution of all modules for high-speed data retrieval.
*   **Unified Interface:** A consistent, minimalist UI built with `Rich` for a professional experience.
*   **Persistent Archiving:** Automatically logs investigations to `case_archive.json` and `investigation.log`.
*   **Zero-Bloat Design:** Clean, efficient code structure for rapid deployment.

---

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone git@github.com:whoami136/PhoneInfoga_toolkit.git
   cd PhoneInfoga_toolkit
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   echo "NUMVERIFY_API_KEY=your_actual_key_here" > .env
   💻 Usage
   Run the engine from the root directory:

   Bash
   python3 main.py
Enter your target node when prompted:
Target Node > +8801XXXXXXXXXX
📁 Project Structure
Plaintext
.
├── main.py              # Core orchestration engine
├── modules/             # Intelligence modules
├── output/              # Log files & session data
├── requirements.txt     # Dependency list
└── .env                 # API Credentials (hidden)
⚠️ Disclaimer
This tool is for educational and authorized testing purposes only. The creator assumes no liability for misuse. Always ensure you have permission to perform OSINT activities on the target provided.

Created by: whoami136
