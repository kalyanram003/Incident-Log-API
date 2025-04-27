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
   git clone <repository-url>
   cd Incident_log_api
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

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

## API Endpoints

### Base URL
```
http://localhost:5000
```

### Endpoints

| HTTP Method | Endpoint | Description | Request Body | Response |
|------------|----------|-------------|--------------|----------|
| GET | `/` | Welcome message and API documentation | - | JSON with API info |
| GET | `/incidents` | Fetch all incidents | - | JSON array of incidents |
| POST | `/incidents` | Create a new incident | JSON: `{ "title": string, "description": string, "severity": "Low"/"Medium"/"High" }` | JSON of created incident |
| GET | `/incidents/<int:id>` | Fetch a specific incident by its ID | - | JSON of incident |
| DELETE | `/incidents/<int:id>` | Delete a specific incident by its ID | - | 204 No Content |

### Example Requests

1. **Create Incident**
   ```bash
   # Using curl
   curl -X POST http://localhost:5000/incidents -H "Content-Type: application/json" -d "{\"title\":\"Server Down\",\"description\":\"Main server is not responding\",\"severity\":\"High\"}"

   # Using PowerShell
   $body = @{
       title = "Server Down"
       description = "Main server is not responding"
       severity = "High"
   } | ConvertTo-Json
   Invoke-RestMethod -Uri "http://localhost:5000/incidents" -Method Post -Body $body -ContentType "application/json"
   ```
   **Postman:**
   - Method: POST
   - URL: `http://localhost:5000/incidents`
   - Headers: `Content-Type: application/json`
   - Body (raw JSON): Same as curl data

2. **Get All Incidents**
   ```bash
   # Using curl
   curl http://localhost:5000/incidents

   # Using PowerShell
   Invoke-RestMethod -Uri "http://localhost:5000/incidents" -Method Get
   ```
   **Postman:**
   - Method: GET
   - URL: `http://localhost:5000/incidents`

3. **Get Specific Incident**
   ```bash
   # Using curl
   curl http://localhost:5000/incidents/1

   # Using PowerShell
   Invoke-RestMethod -Uri "http://localhost:5000/incidents/1" -Method Get
   ```
   **Postman:**
   - Method: GET
   - URL: `http://localhost:5000/incidents/1`

4. **Delete Incident**
   ```bash
   # Using curl
   curl -X DELETE http://localhost:5000/incidents/1

   # Using PowerShell
   Invoke-RestMethod -Uri "http://localhost:5000/incidents/1" -Method Delete
   ```
   **Postman:**
   - Method: DELETE
   - URL: `http://localhost:5000/incidents/1`

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

## NOTE
- Although my core strength lies in Java and Spring Boot, I completed the assignment in Python and Flask to stay aligned with the instructions. I am highly adaptable and can quickly work across multiple backend stacks.
