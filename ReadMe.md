# URL Shortener Web Application

A full-stack web application that allows users to shorten long URLs, manage their links, and securely access their data. Built with Python (Flask), PostgreSQL, and modern web development best practices.

---

## Features

- User registration and login with secure password hashing
- Session-based authentication for protected routes
- URL shortening using SHA-256 hashing algorithm
- Persistent storage of user and URL data in PostgreSQL
- RESTful API endpoints for creating and retrieving URLs
- Redirection from short URL to original URL
- Error handling and input validation

---

## Tech Stack

- **Backend:** Python, Flask, Flask-Session, Flask-CORS
- **Database:** PostgreSQL
- **Environment Management:** python-dotenv
- **Other:** Docker (optional), VS Code

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/url-shortener.git
cd url-shortener
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory and add:

```
SECRET_KEY=your_secret_key
DATABASE_URL=postgresql://username:password@localhost:5432/yourdbname
```

### 5. Set Up the Database

- Create a PostgreSQL database and user.
- Run the SQL schema to create the required tables (e.g., `users`, `url`).

### 6. Run the Application

```bash
python src/app.py
```

The app will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## API Endpoints

### Authentication

- `POST /auth/register`  
  Register a new user.  
  **Body:** `{ "username": "...", "email": "...", "password": "..." }`

- `POST /auth/login`  
  Login user.  
  **Body:** `{ "email": "...", "password": "..." }`

### URL Shortening

- `POST /url/create`  
  Create a short URL (requires authentication).  
  **Body:** `{ "original_url": "https://..." }`

- `GET /url/<short_code>`  
  Redirects to the original URL.

---

## Project Structure

```
URLProject/
│
├── config/
│   └── db_config.py
├── src/
│   ├── app.py
│   ├── Auth.py
│   └── URL.py
├── requirements.txt
├── .env
└── README.md
```

---


## Author

- [Venkatesh](https://github.com/venky-gondu)
