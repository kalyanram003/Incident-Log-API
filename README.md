# Incident Log API

A Flask-based REST API for managing incident logs. This project provides a robust backend system for tracking and managing incidents.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## Project Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/kalyanram003/Incident-Log-API.git
   cd Incident_log_api
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate.bat

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   - Create a `.env` file in the root directory
   - Configure the following environment variables:
     ```
     FLASK_APP=run.py
     FLASK_ENV=development
     DATABASE_URL=sqlite:///instance/app.db
     ```

5. **Database Setup**
   ```bash
   # Initialize the database
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. **Seed the Database (Optional)**
   ```bash
   python seed.py
   ```

## Running the Application

1. **Start the Development Server**
   ```bash
   python run.py
   ```
   The server will start at `http://localhost:5000`

2. **API Endpoints**
   - `GET /`: Welcome message
   - `GET /home`: Welcome message

## Project Structure

```
Incident_log_api/
├── app/                  # Main application package
├── instance/            # Instance-specific files
├── migrations/          # Database migration files
├── venv/               # Virtual environment
├── app.py              # Main application file
├── config.py           # Configuration settings
├── requirements.txt    # Project dependencies
├── run.py             # Application entry point
└── seed.py            # Database seeding script
```

## Development

- The application uses Flask as the web framework
- SQLAlchemy for database operations
- Flask-Migrate for database migrations
- Python-dotenv for environment variable management

