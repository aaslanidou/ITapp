ITapp Dashboard

# Description
**ITapp** is a Django application for monitoring computers in different rooms and buildings.  
You can view IP addresses, computer names, Bria numbers, status (OK / WARNING / REPLACE), and notes.

The dashboard displays rooms and computers as **draggable boxes**, allowing you to visually arrange them on the room layout.  

# Features
- CRUD operations for **Buildings, Rooms, and Computers**
- Drag-and-drop for computer boxes
- Double-click to view computer details
- Color-coded status (green / orange / red)
- Pop-up confirmation for deletions
- Responsive rooms with different sizes
- Search computers by IP or PC name
  
# Prerequisites
- Python 3.12+
- Django 6.x
- Git
  
# Installation Instructions

1. Clone the repository:  git clone https://github.com/aaslanidou/ITapp.git
2. Create a virtual environment:  python -m venv venv
3. Activate the virtual environment:  venv\Scripts\activate  -> Windows   , source venv/bin/activate -> Linux / Mac
4. Install dependencies: pip install -r requirements.txt
5. Create and apply database migrations:  python manage.py makemigrations
python manage.py migrate
6. Create a superuser (optional, for admin access):  python manage.py createsuperuser
7. Run the development server: python manage.py runserver
8. Open the browser at: http://127.0.0.1:8000

Notes
The venv/ folder is not included in the repository
All cache files and the database db.sqlite3 are ignored via .gitignore
The application works best in a modern browser




