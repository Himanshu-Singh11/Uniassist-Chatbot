# 🎓 UniAssist - AI-Powered University Assistant Chatbot

UniAssist is a modern, responsive, and professional AI-powered chatbot designed to help students, parents, and visitors find information about the university easily. It provides answers regarding admissions, courses, fees, placements, scholarships, and general campus infrastructure.

---

## 🎯 Key Features

- **💬 Modern Native Chat Interface**: Built using Streamlit's native `st.chat_input` and `st.chat_message` components with custom role avatars (`🎓` for UniAssist, `👤` for the user).
- **🎛️ Interactive Welcome Dashboard**: Features a 2x2 grid of container cards allowing users to click and search topics (Admissions, Courses, Campus Life, Financial Support) instantly with a single click.
- **🇮🇳 Localized Indian Context**: Mapped completely to the Indian education ecosystem:
  - Currencies formatted in Indian Rupees (₹).
  - Prerequisites aligned with Class 12th Boards, JEE Main, CAT, and GATE.
  - Placements linked to top recruiters like TCS, Infosys, Wipro, and Cognizant.
  - Location and directions set to Knowledge Park, Noida, Uttar Pradesh.
  - Financial aid options integrated with the National Scholarship Portal (NSP) and Vidya Lakshmi education loans.
- **⚡ General Q&A Matching**: Pre-configured with dynamic keyword matching to handle common questions:
  - **Campus Details**: 150-acre green campus size and Metro connectivity details.
  - **Sports**: Facilities including a Cricket Stadium, Football Ground, Basketball courts, and Gym.
  - **Campus Amenities**: Canteens, mess schedules, 24/7 medical clinics, central library, and 1 Gbps Wi-Fi connectivity.
  - **Security**: Strict anti-ragging measures and 24/7 CCTV surveillance.

---

## 📁 Project Structure

```bash
Uniassist-Chatbot/
├── app.py           # Streamlit app interface, styling, and keyword routing logic
├── Courses.py       # Indian university programs, facilities, events, and aid database
├── requirements.txt # Project Python dependencies (streamlit, etc.)
├── .gitignore       # Exclusions for virtual environments, caches, and system files
└── Logo/
    └── uniassist_logo.jpg # App branding & logo icon
```

---

## ⚙️ Setup & Installation

### Prerequisites
Make sure you have Python 3.9+ installed on your system.

### 1. Clone the Repository
```bash
git clone https://github.com/Himanshu-Singh11/Uniassist-Chatbot.git
cd Uniassist-Chatbot
```

### 2. Create and Activate a Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Chatbot

Launch the application locally with the following command:
```bash
streamlit run app.py
```
Open your browser and navigate to `http://localhost:8501` to chat with UniAssist!
