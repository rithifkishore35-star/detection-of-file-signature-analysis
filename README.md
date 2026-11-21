# 🛡️ FileGuard – Suspicious File Type Detection & Digital Forensic Verification System
### Modern 3D Cybersecurity Forensic Laboratory

> **An advanced, immersive 3D cybersecurity web application built with Python, Streamlit, and Three.js (WebGL).**  
> FileGuard protects users against disguised malicious payloads, deceptive double extensions, and file spoofing by analyzing true low-level file signatures (magic bytes) against declared extensions.

---

## 🌟 Key Features

- **Cybersecurity Dark Theme**:
  - Dark navy blue and pitch black gradient background.
  - Glowing neon cyan (`#00F0FF`), purple (`#A855F7`), and electric blue (`#3B82F6`) visual effects.
  - Ambient cybersecurity elements: animated circuit patterns, sweeping holographic laser line, cascading binary code streams, and floating security icons.
- **Interactive 3D Holographic Laboratory**:
  - Interactive 3D crystal shield with central metallic padlock.
  - Orbiting cyan and violet neon energy containment rings.
  - Floating 3D format badges (`📄 PDF`, `⚙️ EXE`, `🖼️ IMG`, `</> CODE`).
  - **Mouse-Responsive Parallax**: Smooth real-time 3D camera tracking reacting to cursor movement.
  - Built-in Canvas 3D fallback for 100% offline and cross-browser reliability.
- **3D Holographic Scanning Chamber**:
  - Real-time animated cyber-file prism with vertical laser scanning sweep.
  - Live multi-stage forensic inspection telemetry.
- **Dynamic 3D Result Holograms**:
  - 🟢 **Safe Format Match**: Glowing emerald shield with verified format aura.
  - 🔴 **Suspicious Mismatch**: Warning ruby shield with pulsing alert core.
  - 🟠 **Unknown / Unsupported**: Amber alert shield for unverified byte signatures.
- **Deep Forensic Detection Engine**:
  - Magic byte header inspection covering 35+ formats (PE Executables, ELF, PDF, OOXML, legacy Office OLE, images, media, archives).
  - ZIP inner container inspection for true modern Office formats (`.docx`, `.xlsx`, `.pptx`).
  - **Double Extension Attack** detection (e.g., `payroll.docx.exe`).
  - **Unicode Right-to-Left Override (RLO / U+202E)** deceptive spoofing detection.
  - SHA-256 and MD5 cryptographic checksum calculation.
- **Multi-Format Export**:
  - Plain Text (`.txt`), Markdown (`.md`), and JSON (`.json`) forensic audit reports.

---

## 📁 Project Structure

```text
fileguard/
├── .streamlit/
│   ├── config.toml        # Streamlit dark theme & server configuration
│   └── secrets.toml       # Local secrets template (ignored by Git)
├── app.py                 # Main Streamlit web application & multi-page navigation
├── detector.py            # Deep binary signature detection & spoofing engine
├── glitter.py             # 60 FPS cyber particle engine, binary streams & laser
├── report.py              # Multi-format forensic audit report generator (TXT, MD, JSON)
├── three_hero.py          # Interactive Three.js WebGL 3D engine & Canvas fallback
├── styles.css             # Cybersecurity Dark Theme CSS & animations
├── requirements.txt       # Production dependencies (streamlit, pillow)
├── push_to_github.bat     # One-click GitHub push helper script
├── run.bat                # Windows local run script
├── .gitignore             # Git ignore patterns
└── README.md              # Project documentation & deployment guide
```

---

## 🚀 Local Installation & Run

### 1. Clone Repository & Navigate
```bash
git clone https://github.com/rithifkishore35-star/detection-of-file-signature-analysis.git
cd detection-of-file-signature-analysis
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch Web Application
```bash
streamlit run app.py
```
Open **`http://localhost:8503`** in your browser.

---

## ☁️ Deploy to Streamlit Community Cloud (Free)

1. Push this repository to **[GitHub](https://github.com/rithifkishore35-star/detection-of-file-signature-analysis)**.
2. Go to **[share.streamlit.io](https://share.streamlit.io/)** and sign in with GitHub.
3. Click **"New app"**.
4. Select your repository: `rithifkishore35-star/detection-of-file-signature-analysis`.
5. Branch: `main`.
6. Main file path: `app.py`.
7. Click **"Deploy!"**.
Your 3D cybersecurity app will be live on a public URL!

---

## 🔒 Security Disclaimer
Format verification confirms whether a file's declared extension aligns with its internal header signature. A matching format does not guarantee the file is free of embedded malicious macros, exploits, or payload scripts. Use FileGuard alongside robust endpoint antivirus solutions.
