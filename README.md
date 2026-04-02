Municipal Fault Reporting System
A web-based municipal fault reporting and tracking system built with Django, designed to help residents report infrastructure issues, monitor resolution progress, and communicate with city service departments — all from one place.

📋 Overview
The City Services Portal allows residents to report infrastructure faults such as potholes, water leaks, electrical outages, illegal dumping, and more. Reports are submitted with GPS-pinned locations, photos, priority levels, and contact details. Residents can track their reports through a personalised dashboard and communicate with a built-in AI assistant for guidance.
This project was developed as part of an HCI (Human-Computer Interaction) course, with an iterative design process informed by AI-assisted usability evaluation, user-centred design principles, and accessibility considerations.

Features

🗺️ Fault Reporting

Select from 8 issue types: Pothole, Water Leak, Drainage, Electricity, Street Light, Graffiti, Illegal Dumping, Other
Interactive Leaflet.js map — click to place a pin or use GPS
Auto-fills street address via reverse geocoding (OpenStreetMap Nominatim) when using "Use My Location"
Priority selector: Low / Medium / High / Critical — with colour dot and text label for accessibility
Drag-and-drop photo upload (up to 5 photos, 5MB each)
Preferred resolution date
Inline form validation with field-level error messages
Save as draft or submit
Confirmation banner with unique tracking reference after successful submission

📊 Dashboard

View all submitted reports with status badges (Submitted / Assigned / In Progress / Completed / Reopened)
Live stats: Total, In Progress, Pending, Completed
Search, filter by status, issue type, priority, and date
Collapsible Advanced Filters panel to reduce cognitive load
Sort by newest, oldest, priority, or status
Escalate active reports or reopen completed ones
Progress bar shown on In Progress reports
"Ask Assistant" button per report — opens chatbot pre-loaded with a question about that specific report

📞 Service Contacts

Emergency contacts: 24/7 Call Centre, Toll-Free Line, SMS
Department contacts: Water, Electricity, Waste, Roads, Street Lighting
Operating hours card
Emergency safety banner (SAPS 10111, Ambulance 10177)
All phone numbers are tappable (tel: / sms: links)

🏠 Home Page

Welcome bar
Hero section with quick-report shortcuts
Live stats (reports submitted, resolved, avg. resolution time, active)
Feature highlights, how-it-works steps
Community section: recent reports feed + resident testimonials (hidden until data exists)
Bottom CTA banner

🤖 AI Chatbot Assistant

Floating chatbot on all four pages
Page-aware context (different system prompts per page)
Quick suggestion pills for common questions
Typing indicator, conversation history
"Ask Assistant" on dashboard cards pre-fills a question about that report's status

🛠️ Tech Stack
LayerTechnologyBackendPython / DjangoFrontendHTML, CSS, Vanilla JS (no frontend framework)MapLeaflet.js + OpenStreetMap tilesGeocodingOpenStreetMap Nominatim (reverse geocoding)AI ChatbotAnthropic Claude API (via Django proxy)FontsDM Sans + DM Mono (Google Fonts)StylingCustom CSS with design tokens (CSS variables)

🚀 Getting Started
Prerequisites

Python 3.10+
pip

Installation
bash# Clone the repository
git clone https://github.com/OneOfAKind-1/HCI.git
cd HCI/municipal_project

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
Environment Setup
Create a .env file in the project root:
envSECRET_KEY=your-django-secret-key
DEBUG=True
ANTHROPIC_API_KEY=sk-ant-your-key-here
Update settings.py to read the key:
pythonimport os
ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY')
Run
bashpython manage.py migrate
python manage.py runserver
Visit http://127.0.0.1:8000/

📁 Project Structure
municipal_project/
├── templates/
│   ├── base.html              # Shared nav + chatbot widget
│   ├── home.html              # Home page
│   ├── report_fault.html      # Fault report form
│   ├── dashboard.html         # Resident dashboard
│   └── services.html          # Service contacts
├── static/
│   └── ...                    # Static assets
├── views.py                   # Django views + chatbot proxy
├── urls.py                    # URL routing
├── models.py                  # ServiceReport model
└── settings.py


♿ Accessibility

Priority levels use colour dot + text label (not colour alone)
Status badges use dot + text
All interactive elements have aria-label attributes
aria-live regions for inline validation errors and chatbot messages
role attributes on map, dialogs, and navigation
Mobile-responsive across all pages






👤 Author
OneOfAKind-1
github.com/OneOfAKind-1
