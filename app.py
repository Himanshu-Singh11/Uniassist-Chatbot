

# UniAssist - AI-Powered University Assistant Chatbot
# A friendly, conversational AI designed to help students, parents, and visitors
# with all university-related queries including admissions, courses, fees, scholarships, etc.

import streamlit as st
import re
from Courses import undergraduate_programs, graduate_programs, university_facilities, campus_events, financial_aid



# University Database Configuration
UNIVERSITY_DATA = {
    "admissions": {
        "undergraduate": {
            "requirements": [
                "Class 12th Board Exam Passing Certificate",
                "Minimum aggregate score of 60% in Class 12th",
                "JEE Main or State Entrance Exam score card (for B.Tech)",
                "Character and Migration Certificates",
                "Passport size photographs & ID proof (Aadhaar Card)"
            ],
            "deadlines": {
                "Phase 1 (Early Bird)": "May 31",
                "Phase 2 (Regular)": "June 30",
                "Phase 3 (Late Admission)": "July 31"
            },
            "application_fee": "₹1,000"
        },
        "graduate": {
            "requirements": [
                "Bachelor's degree from a recognized university",
                "Minimum aggregate of 50% in Graduation",
                "Valid CAT / GATE / XAT score card",
                "Statement of Purpose (SOP)",
                "Migration Certificate",
                "Resume/CV"
            ],
            "deadlines": {
                "Phase 1 (Regular)": "June 15",
                "Phase 2 (Late Admission)": "July 15"
            },
            "application_fee": "₹1,500"
        }
    },
    "courses": {
        "undergraduate": [
            "Computer Science (B.Tech)", "Business Administration (BBA)", "Engineering (B.Tech)", 
            "Psychology (B.Sc)", "Biology (B.Sc)", "Mathematics (B.Sc)", "English Literature (B.A.)",
            "Economics (B.A.)", "Political Science (B.A.)", "Art & Design (B.Des)"
        ],
        "graduate": [
            "MBA", "Master of Computer Science (M.Tech)", "Master of Engineering (M.Tech)",
            "Master of Psychology (M.Sc)", "PhD in Biology", "Master of Education (M.Ed)"
        ]
    },
    "fees": {
        "undergraduate": {
            "tuition_per_semester": "₹1,50,000",
            "room_and_board": "₹50,000 (Hostel & Mess)",
            "books_and_supplies": "₹10,000",
            "total_annual": "₹4,20,000"
        },
        "graduate": {
            "tuition_per_credit": "₹8,000",
            "typical_credits_per_semester": 18,
            "room_and_board": "₹50,000 (Hostel & Mess)",
            "books_and_supplies": "₹15,000"
        }
    },
    "scholarships": [
        {
            "name": "Merit-cum-Means Scholarship",
            "amount": "Up to ₹50,000 per year",
            "requirements": "Class 12th score above 85% and annual family income below ₹6 Lakhs",
            "deadline": "August 31"
        },
        {
            "name": "Post-Matric Scholarship Scheme (Govt. of India)",
            "amount": "Full Tuition Fee Waiver",
            "requirements": "Belonging to SC/ST/OBC category, family income below ₹2.5 Lakhs",
            "deadline": "September 30"
        },
        {
            "name": "National Scholarship Portal (NSP) Schemes",
            "amount": "Up to ₹20,000 per year",
            "requirements": "Applied through NSP, satisfying specific state/central guidelines",
            "deadline": "October 31"
        }
    ],
    "contact": {
        "admissions_office": "admissions@university.edu.in",
        "phone": "+91 120 4567890, +91 98765 43210",
        "address": "12, Knowledge Park, Sector 62, Noida, Uttar Pradesh, India - 201301",
        "website": "www.university.edu.in"
    }
}

def format_program_details(name: str, info: dict, level: str) -> str:
    """Format program information details professionally"""
    response = f"### 🎓 {name} ({level} Program)\n\n"
    response += f"📝 **Description:** {info['description']}\n\n"
    response += f"⏳ **Duration:** {info['duration']}  |  🎯 **Credits Required:** {info['credits']}\n\n"
    
    response += "🔬 **Prerequisites:**\n"
    for prereq in info['prerequisites']:
        response += f"- {prereq}\n"
    response += "\n"
    
    response += "📚 **Core Courses:**\n"
    for course in info['core_courses']:
        response += f"- {course}\n"
    response += "\n"
    
    response += "💼 **Career Opportunities:**\n"
    for path in info['career_paths']:
        response += f"- {path}\n"
        
    return response

def check_specific_program(query_lower: str) -> str or None:
    """Check if the user query refers to a specific academic program"""
    # Graduate programs first (longer strings)
    for prog_name, info in graduate_programs.items():
        if prog_name.lower() in query_lower:
            return format_program_details(prog_name, info, "Graduate")
            
    # Undergraduate programs
    for prog_name, info in undergraduate_programs.items():
        if prog_name.lower() in query_lower:
            return format_program_details(prog_name, info, "Undergraduate")
            
    # Partial matching and abbreviation support
    if 'computer science' in query_lower or ' cs ' in f" {query_lower} ":
        return format_program_details("Computer Science", undergraduate_programs["Computer Science"], "Undergraduate")
    if 'business' in query_lower or 'management' in query_lower:
        if 'mba' in query_lower:
            return format_program_details("MBA", graduate_programs["MBA"], "Graduate")
        return format_program_details("Business Administration", undergraduate_programs["Business Administration"], "Undergraduate")
    if 'engineering' in query_lower:
        if 'master' in query_lower or 'grad' in query_lower:
            return format_program_details("Master of Engineering", graduate_programs["Master of Engineering"], "Graduate")
        return format_program_details("Engineering", undergraduate_programs["Engineering"], "Undergraduate")
    if 'psychology' in query_lower:
        return format_program_details("Psychology", undergraduate_programs["Psychology"], "Undergraduate")
    if 'mba' in query_lower:
        return format_program_details("MBA", graduate_programs["MBA"], "Graduate")
        
    return None

def handle_facilities_query(query_lower: str) -> str:
    """Handle queries about campus facilities and student housing"""
    response = "### 🏢 Campus Life & Facilities\n\n"
    
    if 'housing' in query_lower or 'dorm' in query_lower:
        response += "**🏠 Student Housing & Dining:**\n"
        for item in university_facilities['housing']:
            response += f"- {item}\n"
    elif 'academic' in query_lower or 'lab' in query_lower or 'library' in query_lower or 'workshop' in query_lower:
        response += "**🔬 Academic Facilities:**\n"
        for item in university_facilities['academic']:
            response += f"- {item}\n"
    elif 'support' in query_lower or 'advising' in query_lower or 'counseling' in query_lower:
        response += "**🤝 Student Support Services:**\n"
        for item in university_facilities['support_services']:
            response += f"- {item}\n"
    else:
        # Full list in structured sections
        response += "Here is an overview of our state-of-the-art facilities:\n\n"
        response += "**🔬 Academic & Labs:**\n"
        for item in university_facilities['academic']:
            response += f"- {item}\n"
        response += "\n**🏠 Student Housing & Dining:**\n"
        for item in university_facilities['housing']:
            response += f"- {item}\n"
        response += "\n**💪 Recreation & Life:**\n"
        for item in university_facilities['student_life']:
            response += f"- {item}\n"
        response += "\n**🤝 Support & Advising:**\n"
        for item in university_facilities['support_services']:
            response += f"- {item}\n"
            
    return response

def handle_events_query(query_lower: str) -> str:
    """Handle queries about campus activities and social events"""
    response = "### 📅 Campus Events & Activities\n\n"
    response += "Our campus is full of life and exciting events! Here are the activities scheduled throughout the academic year:\n\n"
    
    response += "**🎈 Social & Cultural Events:**\n"
    for item in campus_events['social']:
        response += f"- {item}\n"
    response += "\n**🏫 Academic Symposiums:**\n"
    for item in campus_events['academic']:
        response += f"- {item}\n"
    response += "\n**💼 Professional Networking:**\n"
    for item in campus_events['professional']:
        response += f"- {item}\n"
        
    return response

def handle_financial_aid_query(query_lower: str) -> str:
    """Handle queries about work-study, student loans, and aid programs"""
    response = "### 💰 Financial Aid & Support Options\n\n"
    response += "We offer comprehensive financial aid options to make your education affordable:\n\n"
    
    # Work study details
    ws = financial_aid['work_study']
    response += f"**💼 Work-Study Program:**\n"
    response += f"- **Overview:** {ws['description']}\n"
    response += f"- **Hourly Rate:** {ws['hourly_rate']}\n"
    response += f"- **Typical Work Hours:** {ws['hours_per_week']}\n"
    response += f"- **How to Apply:** {ws['application_process']}\n\n"
    
    # Loans details
    loans = financial_aid['loans']
    response += f"**🏦 Student Loans:**\n"
    response += f"- **Federal Loans:** {loans['federal_loans']}\n"
    response += f"- **Private Options:** {loans['private_loans']}\n"
    response += f"- **Repayment Terms:** {loans['repayment']}\n\n"
    
    response += "🏆 For merit-based or need-based scholarships, ask me about **scholarships**! 😊"
    return response

GENERAL_QUESTIONS = [
    {
        "keywords": ["size", "area", "acre", "acres", "big", "spread", "campus size"],
        "response": "🏫 Our campus is spread across a lush green **150 acres** in Noida, Uttar Pradesh. It features modern academic blocks, multiple sports fields, student hostels, and beautifully landscaped gardens, providing a perfect environment for learning."
    },
    {
        "keywords": ["ground", "grounds", "play", "playground", "cricket", "football", "sports", "basketball", "tennis", "badminton", "stadium", "gym", "gymnasium"],
        "response": "🏏 **Sports Facilities & Grounds:**\nWe have excellent sports infrastructure, including:\n- A professional **Cricket Stadium** and a full-sized **Football Ground**.\n- Floodlit **Basketball**, **Tennis**, and **Volleyball courts**.\n- An indoor sports complex for **Badminton**, **Table Tennis**, and **Squash**.\n- A fully-equipped modern **Gymnasium** inside the Student Activity Center."
    },
    {
        "keywords": ["placement", "placements", "job", "jobs", "salary", "package", "recruit", "recruiter", "recruiters", "company", "companies", "career", "package", "packages"],
        "response": "💼 **Placements & Career Opportunities:**\nOur university has a stellar placement record:\n- **Placement Rate**: Over 95% placement rate consistently.\n- **Top Recruiters**: Top tech companies like TCS, Infosys, Wipro, Cognizant, HDFC Bank, ICICI Bank, and DRDO/ISRO for research tracks.\n- **Highest Package**: ₹45 LPA (Lakhs Per Annum) in the Computer Science branch.\n- **Average Package**: ₹6.5 LPA across all departments.\n- **Placement Cell**: Dedicated team conducting mock interviews, resume workshops, and regular campus placement drives."
    },
    {
        "keywords": ["hostel", "hostels", "stay", "accommodation", "dorm", "dorms", "room", "rooms", "boarding"],
        "response": "🏠 **Hostel & Stay Facilities:**\nWe offer comfortable residential options on campus:\n- **Separate Hostels**: Independent buildings for boys and girls with biometric security.\n- **Room Options**: Double and triple sharing rooms, with options for Air Conditioning (AC) or standard cooling.\n- **Mess & Dining**: Multi-cuisine mess serving nutritious vegetarian and non-vegetarian meals.\n- **Amenities**: 24/7 power backup, high-speed Wi-Fi, laundry services, and a general store for daily essentials."
    },
    {
        "keywords": ["food", "canteen", "canteens", "cafeteria", "dining", "cafe", "cafes", "eat", "mess"],
        "response": "🍔 **Food & Dining Options:**\n- **Main Hostels Mess**: Nutritious meals served four times a day.\n- **Central Cafeteria**: Serving a variety of Indian, Chinese, and Continental dishes at student-friendly prices.\n- **Food Court**: Outlets of popular chains and local cafes for snacks and beverages.\n- **Night Canteen**: Open until 2:00 AM for late-night study sessions."
    },
    {
        "keywords": ["library", "libraries", "book", "books", "reading"],
        "response": "📚 **Central Library:**\n- **Resources**: Over 1,00,000 physical books, national/international journals, and a massive digital library database.\n- **Facilities**: 24/7 access during exams, air-conditioned reading halls, computer terminals, and group discussion rooms."
    },
    {
        "keywords": ["medical", "health", "hospital", "doctor", "doctors", "clinic", "sick", "ambulance", "medicine"],
        "response": "🏥 **Medical Services:**\n- **On-campus Clinic**: Open 24/7 with qualified doctors and nursing staff.\n- **Ambulance Service**: Round-the-clock emergency transport facility.\n- **Tie-ups**: Affiliated with major hospitals in Noida for advanced care."
    },
    {
        "keywords": ["wifi", "internet", "net", "wi-fi", "connection"],
        "response": "📶 **Wi-Fi & Connectivity:**\n- The entire campus is fully Wi-Fi enabled, including hostels, academic blocks, cafeteria, and sports grounds, with a high-speed 1 Gbps fiber internet backbone."
    },
    {
        "keywords": ["location", "map", "reach", "direction", "directions", "where", "noida", "metro", "bus", "transport"],
        "response": "📍 **Location & Connectivity:**\n- **Address**: 12, Knowledge Park, Sector 62, Noida, Uttar Pradesh, India - 201301.\n- **By Metro**: The nearest metro station is Noida Sector 62 (Blue Line), just 5 minutes away by auto-rickshaw.\n- **By Bus/Auto**: Well connected by local bus networks and 24/7 auto/cab services."
    },
    {
        "keywords": ["safe", "safety", "ragging", "security", "guard", "cctv"],
        "response": "🛡️ **Safety & Zero Tolerance for Ragging:**\n- **Anti-Ragging**: We have a strict zero-tolerance policy. The Anti-Ragging Committee ensures a safe environment.\n- **Security**: 24/7 CCTV monitoring across campus and security personnel at all entry/exit gates."
    }
]

def get_response(user_query: str) -> str:
    """Generate appropriate response based on user query"""
    query_lower = user_query.lower()
    
    # Helper to check if keyword matches on word boundaries
    def match_word(kw: str) -> bool:
        # Special case: check for full word match for very short greetings like 'hi' or 'hey'
        if kw in ['hi', 'hey']:
            return bool(re.search(r'\b' + re.escape(kw) + r'\b', query_lower))
        # General case: match if the keyword starts at a word boundary (e.g. 'admission' matches 'admissions')
        return bool(re.search(r'\b' + re.escape(kw), query_lower))
        
    # 1. Greeting responses (use exact word boundaries to prevent matching 'hi' in 'scholarships' or 'history')
    if any(re.search(r'\b' + re.escape(word) + r'\b', query_lower) for word in ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening']):
        return "👋 Hello! I'm UniAssist, your friendly university assistant! I'm here to help you with admissions, courses, fees, scholarships, and any other university-related questions. What can I help you with today? 😊"
    
    # 2. Financial Aid/Work study/Loans specifically
    if any(match_word(word) for word in ['work study', 'work-study', 'loan', 'loans', 'financial aid']):
        return handle_financial_aid_query(query_lower)

    # 3. Specific program query check (runs before generic course queries)
    prog_details = check_specific_program(query_lower)
    if prog_details:
        return prog_details
        
    # 4. Contact queries (checked early to override other categories if contact info is specifically requested)
    if any(match_word(word) for word in ['contact', 'phone', 'email', 'address', 'office']):
        return handle_contact_query(query_lower)
        
    # 5. General campus life & infrastructure Q&A queries (placements, Wi-Fi, grounds, size, libraries, medical)
    for q in GENERAL_QUESTIONS:
        if any(match_word(kw) for kw in q["keywords"]):
            return q["response"]

    # 6. Admissions queries
    if any(match_word(word) for word in ['admission', 'apply', 'application', 'requirements', 'deadline']):
        return handle_admissions_query(query_lower)
    
    # 7. Course queries (generic)
    if any(match_word(word) for word in ['course', 'program', 'major', 'degree', 'study']):
        return handle_course_query(query_lower)
    
    # 8. Fee queries
    if any(match_word(word) for word in ['fee', 'cost', 'tuition', 'price', 'expensive', 'money']):
        return handle_fee_query(query_lower)
    
    # 9. Scholarship queries (generic)
    if any(match_word(word) for word in ['scholarship', 'grant', 'funding', 'money help']):
        return handle_scholarship_query(query_lower)
    
    # 10. Facilities/Campus Life (generic overview)
    if any(match_word(word) for word in ['facility', 'facilities', 'housing', 'dorm', 'library', 'gym', 'dining', 'campus life', 'campus']):
        return handle_facilities_query(query_lower)
        
    # 11. Events/Activities
    if any(match_word(word) for word in ['event', 'events', 'activities', 'social', 'club', 'clubs', 'sports']):
        return handle_events_query(query_lower)
    
    # 12. General help
    if any(match_word(word) for word in ['help', 'what can you do', 'assist']):
        return get_help_response()
    
    # Default response for unclear queries
    return "I'd be happy to help! Could you please clarify what specific information you're looking for? For example, are you asking about:\n\n" \
           "• 📚 **Admissions** - requirements, deadlines, application process\n\n" \
           "• 🎓 **Courses** - available programs and degrees\n\n" \
           "• 🏢 **Campus Life** - facilities, housing, and events\n\n" \
           "• 💰 **Fees** - tuition, costs, and financial aid\n\n" \
           "• 🏆 **Scholarships** - scholarships, loans, and work-study\n\n" \
           "• 📞 **Contact** - how to reach university offices\n\n" \
           "Just let me know what interests you! 😊"

def handle_admissions_query(query: str) -> str:
    """Handle admissions-related queries"""
    if 'undergraduate' in query or 'bachelor' in query:
        return format_admissions_info('undergraduate')
    elif 'graduate' in query or 'master' in query or 'phd' in query:
        return format_admissions_info('graduate')
    else:
        return "**🎓 Admissions Information**\n\nI can help you with both undergraduate and graduate admissions. Which level are you interested in?\n\n• **Undergraduate** - Bachelor's degree programs\n\n• **Graduate** - Master's and PhD programs\n\nJust let me know which one you'd like to learn about! 😊"

def format_admissions_info(level: str) -> str:
    """Format admissions information for display"""
    data = UNIVERSITY_DATA['admissions'][level]
    
    response = f"**🎓 {level.title()} Admissions Information**\n\n"
    response += "**📋 Requirements:**\n\n"
    for req in data['requirements']:
        response += f"• {req}\n"
    
    response += f"\n**📅 Application Deadlines:**\n\n"
    for term, deadline in data['deadlines'].items():
        response += f"• {term.title()}: {deadline}\n"
    
    response += f"\n**💰 Application Fee:** {data['application_fee']}\n\n"
    response += "**💡 Next Steps:**\n\n"
    response += "1. Review all requirements carefully\n"
    response += "2. Prepare your documents\n"
    response += "3. Submit your application before the deadline\n"
    response += "4. Check your email for updates\n\n"
    response += "Would you like more details about any specific requirement? 😊"
    
    return response

def handle_course_query(query: str) -> str:
    """Handle course-related queries"""
    response = "**📚 Available Programs**\n\n"
    
    response += "**🎓 Undergraduate Programs:**\n\n"
    for course in UNIVERSITY_DATA['courses']['undergraduate']:
        response += f"• {course}\n"
    
    response += "\n**🎓 Graduate Programs:**\n\n"
    for course in UNIVERSITY_DATA['courses']['graduate']:
        response += f"• {course}\n"
    
    response += "\n**💡 Interested in a specific program?**\n\n"
    response += "I can provide detailed information about:\n\n"
    response += "• Program requirements\n"
    response += "• Course curriculum\n"
    response += "• Career opportunities\n"
    response += "• Faculty information\n\n"
    response += "Just let me know which program interests you! (e.g. *'Tell me about Computer Science'*) 😊"
    
    return response

def handle_fee_query(query: str) -> str:
    """Handle fee-related queries"""
    response = "**💰 Fee Structure**\n\n"
    
    response += "**🎓 Undergraduate Costs (per year):**\n\n"
    ug_fees = UNIVERSITY_DATA['fees']['undergraduate']
    response += f"• Tuition: {ug_fees['tuition_per_semester']} per semester\n"
    response += f"• Room & Board: {ug_fees['room_and_board']}\n"
    response += f"• Books & Supplies: {ug_fees['books_and_supplies']}\n"
    response += f"• **Total Annual Cost: {ug_fees['total_annual']}**\n\n"
    
    response += "**🎓 Graduate Costs:**\n\n"
    grad_fees = UNIVERSITY_DATA['fees']['graduate']
    response += f"• Tuition: {grad_fees['tuition_per_credit']} per credit hour\n"
    response += f"• Typical Load: {grad_fees['typical_credits_per_semester']} credits per semester\n"
    response += f"• Room & Board: {grad_fees['room_and_board']}\n"
    response += f"• Books & Supplies: {grad_fees['books_and_supplies']}\n\n"
    
    response += "**💡 Financial Aid Available:**\n\n"
    response += "• Scholarships and grants\n"
    response += "• Work-study programs\n"
    response += "• Student loans\n"
    response += "• Payment plans\n\n"
    response += "Would you like information about financial aid options? 😊"
    
    return response

def handle_scholarship_query(query: str) -> str:
    """Handle scholarship-related queries"""
    response = "**🏆 Available Scholarships**\n\n"
    
    for i, scholarship in enumerate(UNIVERSITY_DATA['scholarships'], 1):
        response += f"**{i}. {scholarship['name']}**\n\n"
        response += f"💰 Amount: {scholarship['amount']}\n"
        response += f"📋 Requirements: {scholarship['requirements']}\n"
        response += f"📅 Deadline: {scholarship['deadline']}\n\n"
    
    response += "**💡 Application Tips:**\n\n"
    response += "• Start early - some deadlines are months in advance\n"
    response += "• Read requirements carefully\n"
    response += "• Prepare strong essays and recommendations\n"
    response += "• Apply to multiple scholarships\n\n"
    response += "Would you like help with the application process for any specific scholarship? 😊"
    
    return response

def handle_contact_query(query: str) -> str:
    """Handle contact-related queries"""
    contact = UNIVERSITY_DATA['contact']
    
    response = "**📞 Contact Information**\n\n"
    response += f"📧 **Admissions Office:** {contact['admissions_office']}\n"
    response += f"📞 **Phone:** {contact['phone']}\n"
    response += f"🌐 **Website:** {contact['website']}\n"
    response += f"📍 **Address:** {contact['address']}\n\n"
    response += "**💡 Office Hours:**\n\n"
    response += "• Monday - Friday: 9:00 AM - 5:00 PM\n"
    response += "• Saturday: 10:00 AM - 2:00 PM\n"
    response += "• Sunday: Closed\n\n"
    response += "**📝 Quick Response:**\n\n"
    response += "For fastest response, email us with your specific question!\n\n"
    response += "Is there anything specific you'd like to ask about? 😊"
    
    return response

def get_help_response() -> str:
    """Provide help information"""
    response = "**🤖 How I Can Help You**\n\n"
    response += "I'm UniAssist, your friendly university assistant! Here's what I can help you with:\n\n"
    response += "**🎓 Admissions**\n\n"
    response += "• Application requirements\n"
    response += "• Deadlines and important dates\n"
    response += "• Application process guidance\n\n"
    response += "**📚 Academic Programs**\n\n"
    response += "• Available courses and degrees\n"
    response += "• Program requirements\n"
    response += "• Career opportunities\n\n"
    response += "**💰 Financial Information**\n\n"
    response += "• Tuition and fees\n"
    response += "• Scholarship opportunities\n"
    response += "• Financial aid options\n\n"
    response += "**📞 University Services**\n\n"
    response += "• Contact information\n"
    response += "• Office locations and hours\n"
    response += "• Campus facilities\n\n"
    response += "**💡 Just ask me anything!**\n\n"
    response += "I'm here to make your university experience smooth and enjoyable. What would you like to know? 😊"
    
    return response





# Initialize session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Page configuration
st.set_page_config(
    page_title="UniAssist - University Assistant Chatbot",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="expanded"
)

def main():
    """Main UniAssist application"""
    # Inject Custom Premium Styles
    custom_css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    /* Welcome dashboard card styling */
    .welcome-container {
        background: linear-gradient(135deg, rgba(239, 246, 255, 0.8) 0%, rgba(219, 234, 254, 0.4) 100%);
        border-radius: 16px;
        padding: 2.2rem;
        border: 1px solid rgba(191, 219, 254, 0.6);
        backdrop-filter: blur(10px);
        margin-top: 1rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px -2px rgba(59, 130, 246, 0.05);
    }
    .welcome-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1.2rem;
        margin-top: 1.5rem;
    }
    @media (max-width: 600px) {
        .welcome-grid {
            grid-template-columns: 1fr;
        }
    }
    .welcome-card {
        background: white;
        border-radius: 12px;
        padding: 1.2rem;
        border: 1px solid rgba(229, 231, 235, 0.9);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03);
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .welcome-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 12px -3px rgba(59, 130, 246, 0.1);
        border-color: rgba(147, 197, 253, 0.8);
    }
    .welcome-card h4 {
        margin-top: 0;
        margin-bottom: 0.4rem;
        color: #1E40AF;
        font-size: 1.05rem;
        font-weight: 600;
        display: flex;
        align-items: center;
        gap: 0.4rem;
    }
    .welcome-card p {
        color: #4B5563;
        font-size: 0.88rem;
        margin-bottom: 0;
        line-height: 1.4;
    }
    
    /* Buttons in sidebar */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        border: 1px solid rgba(120, 120, 120, 0.2);
        background-color: white;
        color: #1F2937 !important;
        transition: all 0.2s ease;
        text-align: left;
        padding: 0.5rem 1rem;
        font-size: 0.9rem;
    }
    .stButton>button:hover {
        background-color: #F9FAFB;
        border-color: #3B82F6;
        color: #3B82F6 !important;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    # Header section
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image('./Logo/uniassist_logo.jpg', width=110)
    with col2:
        st.title("UniAssist Chatbot")
        st.subheader("Your AI-Powered University Assistant")

    st.markdown("---")

    # Sidebar section
    with st.sidebar:
        st.image('./Logo/uniassist_logo.jpg', width=130)
        st.markdown("## 🎯 Quick Help")
        st.markdown("Click any topic below to ask UniAssist instantly:")
        
        if st.button("📚 What courses do you offer?"):
            st.session_state.chat_history.append(("user", "What courses do you offer?"))
            response = get_response("What courses do you offer?")
            st.session_state.chat_history.append(("assistant", response))
            st.rerun()
        
        if st.button("💰 What are the tuition fees?"):
            st.session_state.chat_history.append(("user", "What are the tuition fees?"))
            response = get_response("What are the tuition fees?")
            st.session_state.chat_history.append(("assistant", response))
            st.rerun()
        
        if st.button("🎓 What are the admissions requirements?"):
            st.session_state.chat_history.append(("user", "What are the admissions requirements?"))
            response = get_response("What are the admissions requirements?")
            st.session_state.chat_history.append(("assistant", response))
            st.rerun()
        
        if st.button("🏆 What scholarships are available?"):
            st.session_state.chat_history.append(("user", "What scholarships are available?"))
            response = get_response("What scholarships are available?")
            st.session_state.chat_history.append(("assistant", response))
            st.rerun()
            
        if st.button("🏢 Tell me about Campus Life"):
            st.session_state.chat_history.append(("user", "Tell me about Campus Life"))
            response = get_response("Tell me about Campus Life")
            st.session_state.chat_history.append(("assistant", response))
            st.rerun()
        
        if st.button("📞 How can I contact admissions?"):
            st.session_state.chat_history.append(("user", "How can I contact admissions?"))
            response = get_response("How can I contact admissions?")
            st.session_state.chat_history.append(("assistant", response))
            st.rerun()
        
        st.markdown("---")
        st.markdown("### 💡 Tips")
        st.markdown("""
• Type a course name directly to see prerequisites (e.g. *'Computer Science'* or *'MBA'*)
• Ask about housing, campus events, work-study or student loans
• Feel free to type in your own language or natural questions
""")
        
        st.markdown("---")
        if st.button("🗑️ Clear Chat History", type="secondary"):
            st.session_state.chat_history = []
            st.rerun()

    # Display welcome dashboard if there is no chat history
    if not st.session_state.chat_history:
        st.markdown("""
        <div class="welcome-container" style="margin-bottom: 1.5rem;">
            <h3 style='margin-top: 0; color: #1E3A8A;'>👋 Welcome to UniAssist!</h3>
            <p style='margin-bottom: 0;'>I am your university assistant chatbot, here to help students, parents, and visitors find information easily. Explore any of the topics below to get started:</p>
        </div>
        """, unsafe_allow_html=True)
        
        # 2x2 grid of cards using Streamlit columns and containers
        grid_col1, grid_col2 = st.columns(2)
        
        with grid_col1:
            with st.container(border=True):
                st.markdown("#### 🎓 Admissions Guidance")
                st.markdown("<p style='color: #4B5563; font-size: 0.9rem; min-height: 50px;'>Requirements, application deadlines, and fee details for undergrad and grad students.</p>", unsafe_allow_html=True)
                if st.button("Explore Admissions ➡️", key="card_admissions", use_container_width=True):
                    st.session_state.chat_history.append(("user", "What are the admissions requirements?"))
                    response = get_response("What are the admissions requirements?")
                    st.session_state.chat_history.append(("assistant", response))
                    st.rerun()
            
            st.write("") # Spacer
            
            with st.container(border=True):
                st.markdown("#### 🏢 Campus Life & Amenities")
                st.markdown("<p style='color: #4B5563; font-size: 0.9rem; min-height: 50px;'>On-campus hostels, student dining options, libraries, labs, and recreation.</p>", unsafe_allow_html=True)
                if st.button("Discover Campus Life ➡️", key="card_campus", use_container_width=True):
                    st.session_state.chat_history.append(("user", "Tell me about Campus Life"))
                    response = get_response("Tell me about Campus Life")
                    st.session_state.chat_history.append(("assistant", response))
                    st.rerun()
                    
        with grid_col2:
            with st.container(border=True):
                st.markdown("#### 📚 Degree Programs")
                st.markdown("<p style='color: #4B5563; font-size: 0.9rem; min-height: 50px;'>Detailed prerequisites, course curriculums, durations, and career pathways.</p>", unsafe_allow_html=True)
                if st.button("View Programs ➡️", key="card_programs", use_container_width=True):
                    st.session_state.chat_history.append(("user", "What courses do you offer?"))
                    response = get_response("What courses do you offer?")
                    st.session_state.chat_history.append(("assistant", response))
                    st.rerun()
            
            st.write("") # Spacer
            
            with st.container(border=True):
                st.markdown("#### 💰 Financial Support")
                st.markdown("<p style='color: #4B5563; font-size: 0.9rem; min-height: 50px;'>University merit scholarships, central scheme grants, work-study, and student loans.</p>", unsafe_allow_html=True)
                if st.button("Check Financial Aid ➡️", key="card_finance", use_container_width=True):
                    st.session_state.chat_history.append(("user", "What scholarships are available?"))
                    response = get_response("What scholarships are available?")
                    st.session_state.chat_history.append(("assistant", response))
                    st.rerun()

        st.markdown("""
        <p style='margin-top: 1.5rem; margin-bottom: 2rem; font-size: 0.9rem; color: #4B5563;'>
            💡 <em>Try typing: <strong>"Tell me about the Computer Science program"</strong> or click one of the quick topics in the sidebar to get started!</em>
        </p>
        """, unsafe_allow_html=True)

    # Render conversation history using native chat interface
    for role, message in st.session_state.chat_history:
        avatar = "🎓" if role == "assistant" else "👤"
        with st.chat_message(role, avatar=avatar):
            st.markdown(message)

    # Capture new message input
    if user_input := st.chat_input("Ask me anything about the university..."):
        # Append user message
        st.session_state.chat_history.append(("user", user_input))
        
        # Process and append AI response
        response = get_response(user_input)
        st.session_state.chat_history.append(("assistant", response))
        
        # Force rerun to display immediately
        st.rerun()

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; font-size: 0.85rem; padding-bottom: 2rem;'>
        <p>UniAssist - Making university information accessible and friendly! 🎓</p>
        <p>Contact Office of Admissions: admissions@university.edu | Phone: (555) 123-4567</p>
    </div>
    """, unsafe_allow_html=True)

# Run the application
if __name__ == "__main__":
    import sys
    import subprocess

    if "streamlit" not in sys.argv[0]:
        # Launched with plain Python (e.g. VS Code Play button).
        # Spawn Streamlit as a separate child process to avoid
        # "Runtime instance already exists" errors.
        sys.exit(subprocess.call([
            sys.executable, "-m", "streamlit", "run", __file__,
            "--server.port=8501",
            "--browser.gatherUsageStats=false"
        ]))
    else:
        # Launched correctly via: streamlit run app.py
        main()