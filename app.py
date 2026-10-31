from flask import Flask, render_template

app = Flask(__name__)

ANNOUNCEMENTS = [
    {
        "title": "2026 Admission Intake Now Open",
        "date": "15 Oct 2026",
        "summary": "Applications for undergraduate and postgraduate programmes are now being accepted for the upcoming academic year.",
    },
    {
        "title": "Research Expo 2026 Call for Abstracts",
        "date": "21 Oct 2026",
        "summary": "Faculty members and students are invited to submit innovative research abstracts for the annual expo.",
    },
    {
        "title": "New Student Orientation Week",
        "date": "02 Nov 2026",
        "summary": "Freshers will participate in a week-long orientation covering academic advising, facilities and campus life.",
    },
]

PROGRAMS = [
    {
        "name": "Business Administration",
        "icon": "📊",
        "description": "Develop strategic leadership, financial insight and entrepreneurship skills for the modern economy.",
    },
    {
        "name": "Computer Science",
        "icon": "💻",
        "description": "Explore software engineering, data science and digital innovation through project-based learning.",
    },
    {
        "name": "Health Sciences",
        "icon": "🩺",
        "description": "Train future professionals with hands-on practice, research excellence and patient-centred care.",
    },
]

FACULTIES = [
    {
        "name": "Faculty of Engineering",
        "departments": ["Computer Engineering", "Civil Engineering", "Electrical Engineering"],
        "students": "3,200",
    },
    {
        "name": "Faculty of Business & Law",
        "departments": ["Accounting", "Economics", "Business Administration"],
        "students": "2,760",
    },
    {
        "name": "Faculty of Health Sciences",
        "departments": ["Nursing", "Public Health", "Medical Laboratory Science"],
        "students": "2,340",
    },
    {
        "name": "Faculty of Arts & Humanities",
        "departments": ["Communication Studies", "Psychology", "English Literature"],
        "students": "1,980",
    },
]

STATS = [
    {"label": "Students", "value": "18,500+"},
    {"label": "Staff Members", "value": "1,240"},
    {"label": "Academic Programs", "value": "68"},
    {"label": "Research Labs", "value": "34"},
]


@app.route("/")
def home():
    return render_template(
        "index.html",
        announcements=ANNOUNCEMENTS,
        programs=PROGRAMS,
        stats=STATS,
        faculties=FACULTIES,
    )


@app.route("/student-login")
def student_login():
    return render_template(
        "auth.html",
        page_title="Student Login",
        role="Student",
        portal_message="Access your academic portal, fees, timetable and course information.",
        feature_list=[
            "View class timetable",
            "Check examination results",
            "Submit assignments",
            "Track fee statements",
        ],
    )


@app.route("/staff-login")
def staff_login():
    return render_template(
        "auth.html",
        page_title="Staff Login",
        role="Staff",
        portal_message="Manage teaching schedules, attendance and student performance records.",
        feature_list=[
            "Manage course records",
            "Review student attendance",
            "Access staff portal tools",
            "Coordinate academic activities",
        ],
    )


@app.route("/admin-login")
def admin_login():
    return render_template(
        "auth.html",
        page_title="Administrator Login",
        role="Administrator",
        portal_message="Monitor admissions, staffing, financial operations and institutional planning.",
        feature_list=[
            "Approve admissions",
            "Manage budgets and approvals",
            "Track institutional reports",
            "Coordinate policy updates",
        ],
    )


@app.route("/student-dashboard")
def student_dashboard():
    dashboard_cards = [
        {"title": "Current GPA", "value": "3.82", "meta": "Semester 1"},
        {"title": "Credits Completed", "value": "78", "meta": "of 120"},
        {"title": "Upcoming Classes", "value": "05", "meta": "This week"},
        {"title": "Fee Balance", "value": "$1,240", "meta": "Due in 12 days"},
    ]
    return render_template(
        "dashboard.html",
        page_title="Student Dashboard",
        role="Student",
        cards=dashboard_cards,
        quick_links=["My Courses", "Examination Results", "Library Portal", "Academic Calendar"],
    )


@app.route("/staff-dashboard")
def staff_dashboard():
    dashboard_cards = [
        {"title": "Teaching Load", "value": "4 Courses", "meta": "This term"},
        {"title": "Attendance Rate", "value": "96%", "meta": "Average"},
        {"title": "New Messages", "value": "18", "meta": "From students"},
        {"title": "Office Hours", "value": "09:00-12:00", "meta": "Mon - Thu"},
    ]
    return render_template(
        "dashboard.html",
        page_title="Staff Dashboard",
        role="Staff",
        cards=dashboard_cards,
        quick_links=["Student Records", "Schedule", "Attendance", "Department Announcements"],
    )


@app.route("/announcements")
def announcements():
    return render_template("list-page.html", page_title="University Announcements", items=ANNOUNCEMENTS, type_label="Announcements")


@app.route("/admissions")
def admissions():
    return render_template(
        "info-page.html",
        page_title="Admissions",
        intro="Join a vibrant academic community that blends innovation, mentorship and opportunity.",
        points=[
            "Applications open for undergraduate, postgraduate and diploma programmes.",
            "Admission review includes academic records, supporting documents and programme fit.",
            "Scholarships and fee waivers are available for eligible students.",
            "International students receive guidance on visa and enrollment support.",
        ],
    )


@app.route("/faculties")
def faculties():
    return render_template("faculties.html", page_title="Faculties & Departments", faculties=FACULTIES)


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact Us")


if __name__ == "__main__":
    app.run(debug=True)
    