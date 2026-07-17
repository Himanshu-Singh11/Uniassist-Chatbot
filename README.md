# 🎓 UniAssist — AI-Powered University Assistant Chatbot

UniAssist is a modern, professional AI-powered chatbot built with **Python + Streamlit**, designed to help students, parents, and visitors instantly find information about the university — admissions, courses, fees, placements, scholarships, campus life, and more.

---

## 🎯 Key Features

- **💬 Native Chat Interface** — Built with Streamlit's `st.chat_input` and `st.chat_message` with custom role avatars (`🎓` UniAssist · `👤` User).
- **🎛️ Interactive Welcome Dashboard** — 2×2 grid of clickable cards (Admissions, Courses, Campus Life, Financial Support) that instantly populate the chat.
- **🔍 Smart Keyword Matching** — Handles natural-language queries for:
  - Admissions, eligibility, deadlines, documents
  - Undergraduate & postgraduate programs (B.Tech, MBA, MCA, M.Tech…)
  - Fees, scholarships, education loans, NSP / Vidya Lakshmi
  - Placements, recruiters (TCS, Infosys, Wipro, Cognizant), packages
  - Campus amenities: canteen, hostel, gym, library, clinic, Wi-Fi
  - Sports: Cricket Stadium, Football Ground, Basketball courts
  - Safety: anti-ragging policy, 24/7 CCTV surveillance
- **🇮🇳 India-Localised Context** — ₹ currency, JEE/CAT/GATE references, NSP portal, Noida campus directions & Metro connectivity.
- **⚡ Zero-Config VS Code Run** — Press the **▶️ Play button** in VS Code and the chatbot opens in your browser automatically — no extra setup.

---

## 📁 Project Structure

```
Uniassist-Chatbot/
│
├── app.py                  # Main Streamlit app — UI, styling & response logic
│
├── data/
│   ├── __init__.py
│   └── courses.py          # University programs, facilities, events & financial aid data
│
├── assets/
│   └── logo.jpg            # App branding & logo
│
├── .vscode/
│   └── launch.json         # VS Code Run & Debug configuration
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python **3.9+**
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/Himanshu-Singh11/Uniassist-Chatbot.git
cd Uniassist-Chatbot
```

### 2. Create & Activate a Virtual Environment
```bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Chatbot

### Option A — VS Code (Recommended)
Open the project in VS Code and press the **▶️ Play button** (or `F5`).  
The chatbot will launch silently and open automatically in your browser at `http://localhost:8501`.

### Option B — Terminal
```bash
python app.py
```

### Option C — Direct Streamlit CLI
```bash
streamlit run app.py
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.9+ |
| Web Framework | Streamlit |
| Styling | Custom CSS (injected via `st.markdown`) |
| Data | Pure Python dictionaries (`data/courses.py`) |
| Version Control | Git + GitHub |

---

## 📸 Screenshots

> Launch the app and open `http://localhost:8501` to see UniAssist in action.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
